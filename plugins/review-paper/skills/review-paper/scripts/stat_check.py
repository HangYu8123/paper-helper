#!/usr/bin/env python3
"""Check manually transcribed results. See stat_check.md for the CSV format."""

import argparse
import csv
import json
import math
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path


def number(row, key):
    text = row.get(key, '').strip()
    if not text:
        raise ValueError(f'missing {key}')
    value = Decimal(text)
    if not value.is_finite():
        raise ValueError(f'{key} must be finite')
    return value


def integer(row, key, minimum=0):
    value = number(row, key)
    if value != int(value) or (minimum is not None and value < minimum):
        raise ValueError(f'invalid integer for {key}')
    return int(value)


def rounding_interval(value):
    left = Fraction(value)
    half_unit = Fraction(10) ** value.as_tuple().exponent / 2
    return left - half_unit, left + half_unit


def observed_interval(row, key):
    value = number(row, key)
    exact = row.get(f'{key}_exact', '').strip().lower()
    if exact not in ('', 'yes', 'no'):
        raise ValueError(f'{key}_exact must be yes or no')
    return (Fraction(value), Fraction(value)) if exact == 'yes' else rounding_interval(value)


def intersects(first, second):
    return max(first[0], second[0]) <= min(first[1], second[1])


def gamma_upper(shape, x):
    """Regularized upper incomplete gamma, with a direct upper-tail branch."""
    if x == 0:
        return 1.0
    scale = math.exp(shape * math.log(x) - x - math.lgamma(shape))
    if x < shape + 1:
        term = total = 1 / shape
        for step in range(1, 10001):
            term *= x / (shape + step)
            total += term
            if term <= 2e-15 * total:
                return 1 - scale * total
    else:
        initial = x + 1 - shape

        def coefficients(step):
            return step * (shape - step), initial + 2 * step

        return scale / continued_fraction(initial, coefficients)
    raise ValueError('gamma series did not converge')


def continued_fraction(initial, coefficients):
    """Evaluate b0 + a1/(b1 + ...) with the modified Lentz algorithm."""
    tiny = 1e-300

    def nonzero(value):
        return value if abs(value) >= tiny else math.copysign(tiny, value)

    result = numerator = nonzero(initial)
    denominator = 0.0
    for step in range(1, 10001):
        a, b = coefficients(step)
        denominator = 1 / nonzero(b + a * denominator)
        numerator = nonzero(b + a / numerator)
        factor = numerator * denominator
        result *= factor
        if abs(factor - 1) <= 2e-15:
            return result
    raise ValueError('continued fraction did not converge')


def beta_lower(a, b, x, complement):
    if x == 0 or complement == 0:
        return float(complement == 0)
    reflected = x > (a + 1) / (a + b + 2)
    if reflected:
        a, b, x, complement = b, a, complement, x

    def coefficients(step):
        m = step // 2
        if step % 2:
            value = -(a + m) / (a + 2 * m) * (a + b + m) / (a + 2 * m + 1)
        else:
            value = m / (a + 2 * m) * (b - m) / (a + 2 * m - 1)
        return value * x, 1.0

    scale = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                     + a * math.log(x) + b * math.log(complement))
    probability = scale / a / continued_fraction(1.0, coefficients)
    return 1 - probability if reflected else probability


def probabilities(kind, row):
    tail = row.get('tail', '').strip().lower()
    if tail not in (('upper',) if kind in ('chi2', 'f') else ('upper', 'lower', 'two-sided')):
        raise ValueError('missing or unsupported test tail')
    if kind != 'z':
        df = float(number(row, 'df'))
        if not math.isfinite(df) or df <= 0:
            raise ValueError('df must be finite and positive')
    if kind == 'f':
        df2 = float(number(row, 'df2'))
        if not math.isfinite(df2) or df2 <= 0:
            raise ValueError('df2 must be finite and positive')
    adjustment = row.get('adjustment', '').strip().lower()
    if adjustment not in ('none', 'bonferroni'):
        raise ValueError('missing or unsupported adjustment')
    comparisons = integer(row, 'comparisons', 1) if adjustment == 'bonferroni' else 1

    def probability(stat):
        stat = float(stat)
        if not math.isfinite(stat):
            raise ValueError('statistic is outside the supported numerical range')
        if kind == 'chi2':
            p = gamma_upper(df / 2, stat / 2)
        elif kind == 'f':
            ratio = stat * (df / df2)
            x = 1 / (1 + ratio)
            p = beta_lower(df2 / 2, df / 2, x, 1 - x if ratio >= 1 else ratio / (1 + ratio))
        elif kind == 'z':
            sign = -1 if tail == 'lower' else 1
            p = (math.erfc(abs(stat) / math.sqrt(2)) if tail == 'two-sided'
                 else math.erfc(sign * stat / math.sqrt(2)) / 2)
        else:
            relative = abs(stat) / math.sqrt(df)
            ratio = relative * relative
            x = 1 / (1 + ratio)
            two_sided = beta_lower(df / 2, 0.5, x, 1 - x if ratio >= 1 else ratio / (1 + ratio))
            p = two_sided if tail == 'two-sided' else two_sided / 2
            if (tail == 'upper' and stat < 0) or (tail == 'lower' and stat > 0):
                p = 1 - p
        if not math.isfinite(p) or p < -1e-12 or p > 1 + 1e-12:
            raise ValueError('probability could not be evaluated reliably')
        return max(0.0, min(1.0, comparisons * p))

    lo, hi = observed_interval(row, 'stat')
    if kind in ('chi2', 'f'):
        if number(row, 'stat') < 0:
            raise ValueError('test statistic must be nonnegative')
        lo = max(0, lo)
    candidates = [probability(lo), probability(hi)]
    if tail == 'two-sided' and lo < 0 < hi:
        candidates.append(probability(0))
    return min(candidates), max(candidates)


def reported_probability(row):
    text = row.get('reported', '').strip().replace('≤', '<=').replace('≥', '>=')
    for operator in ('<=', '>=', '<', '>', '='):
        if text.startswith(operator):
            value = number({'p': text[len(operator):]}, 'p')
            break
    else:
        operator = '='
        value = number({'p': text}, 'p')
    if not 0 <= value <= 1:
        raise ValueError('reported probability must be between 0 and 1')
    value_exact = Fraction(value)
    if operator in ('<', '<='):
        return 0, value_exact, True, operator == '<='
    if operator in ('>', '>='):
        return value_exact, 1, operator == '>=', True
    lo, hi = rounding_interval(value)
    return max(0, lo), min(1, hi), True, True


def decision(lo, hi, lo_included, hi_included, alpha, rule):
    if hi < alpha or (hi == alpha and (rule == '<=' or not hi_included)):
        return 'significant'
    if lo > alpha or (lo == alpha and (rule == '<' or not lo_included)):
        return 'nonsignificant'
    return 'indeterminate'


def check_test(kind, row):
    lo, hi = probabilities(kind, row)
    rlo, rhi, left_closed, right_closed = reported_probability(row)
    # Near an endpoint allow floating-point evaluation error, not a paper-side
    # rounding unit. Keep inequalities strict when the boundary is exact.
    lower_match = hi > float(rlo) or (left_closed and math.isclose(hi, float(rlo), rel_tol=1e-12))
    upper_match = lo < float(rhi) or (right_closed and math.isclose(lo, float(rhi), rel_tol=1e-12))
    if rlo == rhi and not (left_closed and right_closed):
        status = 'inconsistent'
    elif ((not left_closed and math.isclose(hi, float(rlo), rel_tol=1e-12))
          or (not right_closed and math.isclose(lo, float(rhi), rel_tol=1e-12))):
        status = 'indeterminate'
    elif not lower_match or not upper_match:
        status = 'inconsistent'
    else:
        status = 'consistent'
    result = {'status': status, 'p_interval': [lo, hi]}
    if row.get('alpha', '').strip():
        alpha = Fraction(number(row, 'alpha'))
        rule = row.get('alpha_rule', '').strip()
        if not 0 < alpha < 1 or rule not in ('<', '<='):
            raise ValueError('alpha in (0,1) and alpha_rule (< or <=) are required for a decision')
        if any(math.isclose(bound, float(alpha), rel_tol=1e-12) for bound in (lo, hi)):
            result['computed_decision'] = 'indeterminate'
        else:
            result['computed_decision'] = decision(lo, hi, True, True, alpha, rule)
        result['reported_decision'] = decision(rlo, rhi, left_closed, right_closed, alpha, rule)
    return result


def check_mean(row):
    mean = number(row, 'reported')
    n = integer(row, 'denominator', 1)
    minimum = integer(row, 'scale_min', None)
    maximum = integer(row, 'scale_max', minimum)
    rounding = row.get('rounding', '').strip()
    if rounding not in ('half_even', 'half_up', 'half_down'):
        raise ValueError('a known rounding convention is required for GRIM')
    lo, hi = rounding_interval(mean)
    first = max(n * minimum, math.ceil(n * lo))
    last = min(n * maximum, math.floor(n * hi))
    unit = hi - lo
    displayed = Fraction(mean) / unit

    def rounds_to_mean(total):
        scaled = Fraction(total, n) / unit
        if rounding == 'half_even':
            return round(scaled) == displayed
        nearest = (math.floor(abs(scaled) + Fraction(1, 2)) if rounding == 'half_up'
                   else math.ceil(abs(scaled) - Fraction(1, 2)))
        return (-nearest if scaled < 0 else nearest) == displayed

    return first <= last and (last - first >= 2 or rounds_to_mean(first) or rounds_to_mean(last))


def check(row):
    if not row.get('page', '').strip():
        raise ValueError('missing page')
    if not row.get('source_span', '').strip():
        raise ValueError('missing source_span')
    kind = row.get('kind', '').strip().lower()
    if kind in ('t', 'z', 'f', 'chi2'):
        return check_test(kind, row)
    if kind == 'grim':
        consistent = check_mean(row)
    elif kind == 'count':
        counts = [integer({'component': value}, 'component') for value in row.get('counts', '').split(';')]
        consistent = sum(counts) == integer(row, 'reported')
    elif kind == 'percent':
        successes = integer(row, 'numerator')
        n = integer(row, 'denominator', 1)
        if successes > n or not 0 <= number(row, 'reported') <= 100:
            raise ValueError('a part-to-whole percentage requires counts and percent within their bounds')
        value = Fraction(100 * successes, n)
        consistent = intersects((value, value), observed_interval(row, 'reported'))
    elif kind == 'pooled_d':
        if row.get('design', '').strip() != 'independent-pooled':
            raise ValueError('pooled d requires an independent, equal-variance two-group t test')
        n1 = integer(row, 'n1', 2)
        n2 = integer(row, 'n2', 2)
        stat = observed_interval(row, 'stat')
        multiplier = math.sqrt(1 / n1 + 1 / n2)
        consistent = intersects(tuple(float(x) * multiplier for x in stat), observed_interval(row, 'reported'))
    else:
        raise ValueError(f'unsupported check kind {kind!r}')
    return {'status': 'consistent' if consistent else 'inconsistent'}


def check_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        rows = csv.DictReader(stream)
        fields = set(rows.fieldnames or ())
        required = {'kind', 'page', 'source_span', 'reported'}
        if required - fields or len(fields) != len(rows.fieldnames):
            raise ValueError('CSV needs unique kind, page, source_span and reported columns')
        for row in rows:
            try:
                if None in row or None in row.values():
                    raise ValueError('row length does not match the CSV header')
                result = check(row)
            except (ArithmeticError, InvalidOperation, ValueError) as error:
                result = {'status': 'indeterminate', 'reason': str(error)}
            yield {'line': rows.line_num, 'source': row, **result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv', type=Path, help='CSV of values verified against their source pages')
    args = parser.parse_args()
    try:
        for result in check_csv(args.csv):
            print(json.dumps(result, ensure_ascii=True, allow_nan=False))
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        parser.exit(2, f'{error}\n')


if __name__ == '__main__':
    main()
