# Check reported numbers

Transcribe values from the rendered source pages into UTF-8 CSV. Preserve trailing zeros, inequality signs, units, and the source location. Use one row per check and leave unused fields blank.

```csv
kind,page,source_span,reported,numerator,denominator,stat,df,tail,adjustment,alpha,alpha_rule
percent,5,Table 2 row A,83.3,25,30,,,,,,
t,7,Section 4.2 paragraph 2,0.05,,,2.10,18,two-sided,none,0.05,<
chi2,8,Table 3 last row,<0.001,,,32.00,2,upper,none,0.05,<
```

```sh
python scripts/stat_check.py numbers.csv
```

Every row requires `kind`, `page`, `source_span`, and `reported`. Add the columns needed by the checks you use.

| `kind` | Additional fields |
| --- | --- |
| `count` | `counts`, a semicolon-delimited list of disjoint component counts. Put the reported total in `reported`. |
| `percent` | `numerator` and `denominator` as integer counts. Put the percent in `reported` without the percent sign. |
| `t`, `z`, `chi2`, `f` | `stat`, `tail`, and `adjustment`. All except `z` need `df`. An `f` test takes numerator `df` and denominator `df2`. Use `upper` for `chi2` and `f`. Use the stated `upper`, `lower`, or `two-sided` tail for `t` and `z`. `adjustment` is `none` or `bonferroni`, which needs the total family size in `comparisons`. Include both `alpha` and `alpha_rule` (`<` or `<=`) to compare decisions. |
| `pooled_d` | `stat` is the signed t statistic, `design` is `independent-pooled`, and `n1` and `n2` are group sizes. Match the sign and group order of the reported, uncorrected Cohen's d. |
| `grim` | `denominator` is the number of equally weighted integer observations, `scale_min` and `scale_max` are inclusive bounds on a contiguous integer scale, and `rounding` is `half_even`, `half_up`, or `half_down`. |

The checker allows half a unit in the last printed digit for rounded values. Enter `stat_exact=yes` for an explicitly exact statistic and `reported_exact=yes` for an explicitly exact percentage or effect size. The p-value `reported` field accepts `=`, `<`, `>`, `<=`, `>=`, `≤`, and `≥`. The tails are computed over the rounding interval of the statistic. The calculations use double precision. Rank tests, standard deviation checks, and other multiple-testing adjustments require separate methods.

Each JSON output line includes the input row and its `consistent`, `inconsistent`, or `indeterminate` status. Test checks also return the implied `p_interval`, and, when supplied with a threshold and rule, the computed and reported significance decisions. An interval that crosses the threshold produces an indeterminate decision. Inspect flagged results against the original table and the stated analysis before using them in a review.
