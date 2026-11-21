---
name: review-paper
description: Draft or revise a peer review of any research paper in Hang's reviewing style, with an interactive review page where each point includes evidence and can be accepted, edited, or rejected. Use when asked to review, referee, critique, or assess a manuscript, draft reviewer comments, fill a venue's review form, or revise a review from saved decisions. Follow the review guidelines and the writing-style skill, and verify any reference review against the manuscript. When asked to edit a manuscript's text instead, propose the edits on the editing page for accept or reject.
---

# Paper review

The output is a draft for Hang to judge, not a finished review. Hang reads each point in the review page, looks at the evidence right under it, and accepts, edits, or rejects it. So two things matter most. Every point must be correct about the paper, because a wrong claim in a review is unfair to the authors and costs Hang credibility. And every point must show its evidence, so Hang can decide in seconds instead of re-reading the paper.

Apply this workflow to the paper being reviewed. Determine its contributions, terminology, evidence, venue, and review identifier from the supplied materials. Do not carry a previous paper's methods, datasets, results, criticisms, or recommendation into a new review.

## Using this skill

The user's request (in Claude Code, the text after the skill's slash command) names the paper folder or manuscript. If it does not, use the paper already established in the conversation, and ask only for missing input.

This skill runs in Claude Code and in Codex, as a plugin of its own or installed as a standalone skill. `SKILL_DIR` below is the folder that holds this `SKILL.md` (in Claude Code, `${CLAUDE_SKILL_DIR}`); resolve relative paths from it.

It uses other skills of the same collection, shared with the `polish-paper` skill and found by name as described under "Companion skills" below.

| Skill | Needed | Use |
| --- | --- | --- |
| `writing-style` | Yes | Hang's writing style reference, and the rest of its references only when needed (see step 5) |
| `html-templates` | Yes | The review template, and the editing template for edits to a manuscript's text |
| `find-sota-papers` | No | The literature search for the related-work check in step 3, in its light mode |
| `writing-vocabulary` | No | The author's vocabulary, for word choice |

Below, `<html-templates>`, `<find-sota-papers>`, `<writing-vocabulary>`, and `<writing-style>` stand for the folders of these skills.

| What | Where |
| --- | --- |
| Manuscript | The paper PDF in the paper folder. If the folder has several PDFs and it is unclear which is the manuscript, ask. |
| Reference review, optional | Usually `<paper>/review.pdf`, or a file the user names. Treat it as a second opinion to verify against the manuscript. |
| Review rules | [references/guideline.md](references/guideline.md), Hang's guideline for the sections, their order, and the rules for each one |
| Past reviews, optional | `previous_reviews/previous_reviews` in the folder that holds the paper folder, or a file Hang names. They are confidential, so they are not part of this skill. |
| Writing style | Hang's writing style reference, `<writing-style>/writing_style_ref/hangs-writing-style-reference.md`. The rest of `<writing-style>/writing_style_ref/` and `<writing-style>/committee_style_ref/` only when needed (see step 5). When installed, the vocabulary, `<writing-vocabulary>/vocabulary.md`. |
| Review template | `<html-templates>/review_template/`. Its `review.html` header comment (lines 1 to 116) is the specification of `review-data.js`. |
| Editing template | `<html-templates>/edit_template/`. Used only for edits to a manuscript's text (see "Edits to a manuscript's text"). |
| Checker and format example | `SKILL_DIR/review-tools/check_review.js` and [review-data-format.md](review-tools/review-data-format.md), in this skill |
| Output | `<paper>/review/review.html`, an unchanged copy of the template, and `<paper>/review/review-data.js` |

Below, `<review-template>` and `<edit-template>` stand for these two template folders.

### Companion skills

Find a companion skill by its name, in this order:

1. Next to this skill: `../<name>/`, as in a standalone install, or `../../../<name>/skills/<name>/`, as in the repository, where each skill is its own plugin.
2. The folder of the `<name>` skill that the app lists, as when the skills are installed as plugins. In Claude Code, invoke the skill: its SKILL.md names its folder. In Codex, the list of skills gives the path to its SKILL.md.

If a needed skill is in neither place, stop and tell the user which skill to install. If an optional one is missing, continue without it, and say so only where it limits the review.

When Hang asks to revise an existing review, update that review in place, preserving saved decisions and Hang's wording. Before replacing an existing review with a fresh draft, ask whether to replace it or write to `<paper>/review-<YYYYMMDD>/` instead.

Treat the manuscript as confidential, since review copies are marked "For review only". Use public technical terms for searches and keep manuscript text out of web forms, search engines, and external tools. Follow the query rules in step 3.

## Ask the authors, do not explain for them

A review of someone else's paper is an external review, and it is the usual case for this skill. Treat a review as external unless Hang says the paper is Hang's own or a co-author's.

In an external review, do not analyze an observation on the authors' behalf. When a point rests on something the paper shows but does not explain, such as an unexpected result, a gap between two conditions, identical numbers in two rows, or a step that does not seem to follow, state the observation with its location and ask the authors to explain or clarify it. A reviewer's guess at the cause can be wrong, it answers the question for the authors, and the authors may read it as a claim they now have to rebut.

- Write "Table 2 shows a lower success rate for the method in cluttered scenes than in open scenes (p. 6). Please explain what causes this drop, since the claim of robustness to clutter depends on it." Do not write "The drop is likely because the sampler cannot find collision-free grasps in clutter."
- Do not follow an observation with "likely because", "possibly due to", "this suggests that", or "one explanation is". If a possible cause helps Hang judge whether the question is worth asking, put it in the evidence `reason`, marked as untested, and keep the review text to the observation and the question.
- Keep the question tied to what depends on it. Name the claim that the answer affects, as a weakness already does, so the authors know why it is asked.
- Checking is still part of the review. Search the paper, recompute numbers, and work through a derivation before asking, so the question is about what the paper really leaves open and not about something it states. This rule is about what the review text says, not about how much you verify.

The rule applies to the weaknesses, the areas for improvement, and the recommendation. The summary and the strengths describe what the paper establishes and need no questions.

When the paper is Hang's own or a co-author's, an explanation of an observation and a suggested fix are useful, since the author can act on them. Mark such an explanation as a reading, not a finding.

## Workflow

### 1. Read the whole paper

Extract the text with page markers into the scratchpad, then read all of it, including the appendix and any supplement.

```
python SKILL_DIR/scripts/pdf_pages.py <paper>/<manuscript>.pdf <scratchpad>/paper.txt
```

Text extraction scrambles tables and loses figures. Open every page that has a results table or a key figure as an image (for instance with the Read tool and `pages: "5-6"`) and read the numbers from the page image. Any number that goes into the review should come from a table or figure you looked at.

Before using page markers, compare their count with an independent physical page count and verify where the manuscript begins. If counts disagree, re-extract by physical page with a second backend or cite only visually verified pages. Use rendered pages to confirm text-poor pages and damaged table symbols. Record any location whose physical page could not be verified.

While reading, keep notes in `<scratchpad>/notes.md`:

- **Claims**, quoted with location, from the abstract, the contribution list, and the conclusion.
- **Method**, separating what is new from what is taken from earlier work.
- **Evidence for each contribution**, including the analysis and observations behind design or qualitative claims, premises and examples behind conceptual arguments, or proof and assumptions behind theoretical results. For experiments, record environment, workload (scenes, trials, runs, seeds), baselines, metrics, headline numbers, and location.
- **Limitations the authors state themselves.**
- **Open questions**, each an observation the paper does not explain, with its location and the claim that depends on it. In an external review these become questions for the authors, not explanations (see "Ask the authors, do not explain for them").
- **Venue and submission id**, usually in the page header, and the review form options if known.

### 2. Check the claims against the evidence

Read [references/calibration.md](references/calibration.md) before drafting any weakness. It lists the ways earlier drafts went wrong, such as claiming the paper omits something it states, or treating a rough calculation as proof of a discrepancy.

For each central claim in the notes, choose the checks that could establish it or expose a material limit.

- **Derivation.** Trace assumptions, definitions, and each necessary step. A counterexample can disprove a guarantee. A guarantee needs a derivation or proof.
- **Performance.** Inspect the split and selection procedure, metric, test setting and size, uncertainty, and the ablation or controlled comparison that isolates the contribution.
- **Studies with people.** Check the design, assignment or counterbalancing, unit of analysis, and treatment of repeated observations and exclusions.
- **Qualitative findings.** Examine sampling, the path from observations to themes, and contrary evidence.
- **Numbers and scope.** Trace headline values to the rendered tables or figures. Recompute ratios and speedups from matching inputs. For counts, percentages, supported tests, and integer-scale means, follow the [statistics checker instructions](scripts/stat_check.md) and run `python SKILL_DIR/scripts/stat_check.py <scratchpad>/numbers.csv`. Keep the outputs with the notes and check any flagged row against its source. Assess how far each claim extends beyond the tested setting and population.

Keep a technical log in `<scratchpad>/technical-checks.md`. For each attempted check, record the claim, source location, calculation or inspection, consequence for the claim, and disposition (`verified`, `refuted`, or `unresolved`). Record an unexplained observation as an open question. For an external review, ask the authors about it if the answer matters to a claim.

#### Trace a supplied artifact

When the submission supplies an artifact or an anonymous artifact link, choose one headline result with a stated entry point. Trace its effective run configuration through data splitting, filtering, model selection, metric calculation, and aggregation. Check for overrides before attributing a default to the run. Record the artifact version, file and line, and the evidence connecting that path to the result in the technical log. Mark the link unresolved when the run configuration is missing.

Use static inspection for this pilot. Execute submitted code only on Hang's explicit request, in an isolated environment without network access or credentials.

### 3. Look at the closest related work

#### Plan queries and screen results

When the `find-sota-papers` skill is installed, run the search through it. Read `<find-sota-papers>/references/embedded.md` and follow it with this brief: purpose `novelty` and `baselines`; the manuscript is confidential; the date window is "public before the venue's submission deadline"; the problem, each component of the approach, and the evaluation, in public technical terms from the notes; institutions left at its default. It decides the queries and the other settings itself, verifies every paper it returns, and keeps a paper from outside its institution filter when that paper could change a novelty or baseline finding. Copy its table, its discarded candidates, the baselines it found named in the closest papers' comparisons, and its limits into `<paper>/review/related-work.md`, then continue with the full-text reading below. The rules in the rest of this subsection still apply. Without the skill, plan and screen as follows.

Write queries for three perspectives: the problem the paper addresses, the techniques it uses or adapts, and the benchmarks, baselines or study designs it is evaluated with. Write a broad and a narrow query for each, in public technical terms taken from the notes. Do not search the submission’s own title, since that returns its preprint and can reveal the authors.

Screen candidates on metadata before reading any full text. Collect title, year, venue and abstract from a scholarly index such as Semantic Scholar or the arXiv API, and from the field’s proceedings, since much HRI and CHI work is not on arXiv. Merge versions of one paper and drop versions of the submission. Rank the rest by how directly each abstract bears on a stated claim, task or protocol, and pass the shortlist to [TQ-05](#compare-methods-and-claims) and [TQ-03](#verify-baseline-results).

Keep full-text reading at the current two to four papers, so the change is in which papers are read rather than how many. Record each query, where and when it ran, the shortlist, and why each kept paper could change the review, in `<paper>/review/related-work.md`.

Record discarded candidates and their reasons in the same file. Prioritize sources that could settle a material novelty or comparison claim within the shared full-text budget. Record unavailable sources, exhausted budgets, and resulting limits in the evidence. Bound novelty wording to the specific differences the sources support. If web access is unavailable, record the limit and check the sources already supplied.

#### Compare methods and claims

For each shortlisted paper, choose the reading depth. Use the abstract to establish topical relevance. If a review finding depends on its method, result, or protocol, write the question its full text needs to answer before retrieving it. Extract downloaded PDFs with `scripts/pdf_pages.py`. Record the decisive passage and page in each paper in `related-work.md`, and mark the comparison unresolved when a decisive passage is unavailable. Check page locations according to step 1.

For the closest one or two papers, compare the relevant components and their supporting experiments in `related-work.md`. Check the date of each public comparator against the submission deadline and apply the venue's concurrency rule. Treat later or concurrent work as context. Write separate findings about prior existence, demonstrated advantage, and attribution of that advantage. Request an ablation when a material causal attribution depends on it.

#### Verify baseline results

Use the benchmark and baseline queries to trace results that support a material comparative claim. Read the source table and experiment description. For a quoted result, compare with the published value at its reported precision. For a rerun, compare dataset version, split, metric, preprocessing, model variant, and evaluation protocol before interpreting a gap. Record the two locations, settings, reported values, and effect on the claim in `<paper>/review/baselines.md`. Record uncertainty where the source or settings cannot be matched. Ask the authors how the baseline was run when matched settings leave a material gap unexplained.

### 4. Check the reference review, if there is one

List each of its points and decide whether it holds, partly holds, or does not hold (a misreading, already addressed in the paper, or minor). Verify by searching `paper.txt` and by checking the passage, derivation, or table it refers to. Check alleged omissions and errors, the venue, generic praise, and requests for additional analyses. Use verified points in your own words, and record each decision in the `reason` of the related evidence, such as "The reference review's missing-control concern is supported by the study design." List the dropped points, with why, in the evidence of the recommendation.

### 5. Read the rules

- [references/guideline.md](references/guideline.md) in full. It sets the sections, their order, and the rules for each one. Its `@` names refer to the files in the table under "Using this skill".
- Hang's past reviews in full, when they are available (see the table under "Using this skill"). They show Hang's voice and the recommendation template. Without them, use the recommendation form in [references/review-voice.md](references/review-voice.md).
- Hang's writing style reference, `<writing-style>/writing_style_ref/hangs-writing-style-reference.md`: its opening through the Quick reference, then the patterns under Wording preference, Sentence style, and Sentence structure as they come up. When the `writing-vocabulary` skill is installed, read its `vocabulary.md` first and use it for word choice; without it, use the Vocabulary patterns of Hang's reference and the paper's own terms. Dissertation structure, the dissertation's impersonal voice, and the slide and film patterns do not set the style of a peer review.
- [references/review-voice.md](references/review-voice.md), which distills Hang's reviewing voice and the sentence rules from the style reference that apply to reviews.

The Quick reference and the review voice cover ordinary reviews. The rest of the `writing-style` skill is a large source library; open its evidence and review records, or the committee reference, `<writing-style>/committee_style_ref/committee-writing-style-reference.md`, for conventions of published writing, only when Hang disputes a wording choice, when a pattern states a rule without the case at hand, or when Hang asks. Search by heading or pattern name, and read only the entries needed. Hang's current instructions and Hang's reference take precedence over older examples that are casual, verbose, or heavily first person. Use "the authors", the method, or the results as the subject by default. Keep first person for a personal concern, a recommendation, or the requested expertise caveat.

### 6. Draft the five sections

Use the point counts below as pacing defaults. One material weakness can be enough. Explain its effect on the recommendation in the review.

Write the items in this order, with these ids: `summary-1`, `summary-2`, `strength-1` ..., `weakness-1` ..., `improvement-1` ..., `recommendation-1`.

**Summary** (one or two short paragraphs, usually 80 to 140 words total). Summarize the contributions fairly instead of repeating the claimed list. The first paragraph names the problem, approach, and central contribution in about three sentences. Merge claims that are one idea at two levels of detail, and omit implementation details. Hang's summaries open with "In this work, the authors proposed ...". A second paragraph, if needed, gives the evaluation setting and main result in **one or two sentences**, usually no more than 45 words. Omit metric lists, secondary timings, and a repeated novelty judgment. If a quantitative comparison is essential, give one comparison with its measure, baseline, and condition.

**Strengths** (about three to six points). Lead with what is new and why it matters, then what the community gains, then rigor and clarity. Usually use one or two sentences and 25 to 60 words per point, with one supporting fact. Explain what an ablation establishes without reciting its rows. Put exact values, extra conditions, equation checks, and related-work comparisons in the evidence. Do not narrate the review process with "I worked through" or "I checked". Generic praise needs the fact that earns it.

**Weaknesses** (usually three to five points, most important first). Focus on what is really insufficient, such as unclear contributions, insufficient evidence for a claimed contribution, or wrong or very outdated methods. Ignore minor issues, such as typos, one more sensitivity sweep, or a missing citation that changes nothing. Use at most two points of the "more baselines" or "more recent work" kind. Use a restrained and considerate tone, usually two or three sentences and 40 to 90 words. Each point states one concern, gives one decisive example and location, explains which claim it affects, and briefly says what would resolve it. In an external review, a concern that rests on an observation the paper does not explain ends with a question or a request for clarification, not a guess at the cause. Credit what the authors already did or acknowledged. Move additional examples and calculations into the evidence. Use "My largest concern is" only for the point that really drives the recommendation.

**Areas for improvement** (one or two points, usually two or three sentences each). Say what would make the paper better or acceptable with a reasonable workload. This is different from a weakness. A weakness says what is missing or wrong, and an improvement says what to do. Prefer actions that use what the authors already have, offer a cheaper path next to an experiment (such as narrowing a claim), and mark larger work as optional. Do not claim that a piece of work is small unless the paper shows it. Prefer "Please clarify ..." or "The comparison would be stronger with ..." to conversational requests such as "I would love to see ...".

**Overall recommendation** (one paragraph). Follow the template in Hang's past reviews, or the form in [references/review-voice.md](references/review-voice.md) without them. Briefly summarize the review, give the recommendation and its reason in one short sentence, and end with the not-an-expert line, such as "While I am not an expert in this field, I would not argue if my recommendation largely disagrees with other reviewers'." Read and use the venue's own decision options. If the recommendation is a judgment call, say so in its evidence and name the alternative.

Categories (subheadings) are optional on strength, weakness, and improvement points, and only when the section has three or more points. The template header lists the category names.

### 7. Write the evidence for each item

Every item gets one to five evidence objects, which the page shows right after the point.

- `where`: the location, such as "Sec. III, p. 4" or "Table 2, ablation rows, p. 5".
- `text`: what the paper (or the external source) says. Quote exactly, in quotation marks, when quoting.
- `reason`: the step from the evidence to the wording of the point. Put calculations, assumptions, equation checks, detailed ablation values, search limits, and reference-review decisions here, so the review text stays short. Retain these details when shortening a point.
- `source`, which the Connections tab counts:
  - `claims`, `method`, `experiments`, `baselines`, or `presentation` for the paper
  - `prior` or `field` for external work, with `url`
  - `guideline`, `previous`, or `style` for Hang's rules
  - `summary`, `strength`, `weakness`, or `improvement` for another part of this review

The first evidence of a point is usually the paper location that supports it. Cite a rule (`guideline`, `previous`, `style`) only when it explains a choice Hang might question, such as a dropped reference-review point or a hedged word.

### 8. Draft the state machine of the paper

After the five sections, map the argument of the paper, not its pipeline. The specification is in the header comment of `<review-template>/review.html` (the `machine` fields and "How to write the machine"), and [review-data-format.md](review-tools/review-data-format.md) has a worked example. In short:

1. One intuition state, then two to four contribution states, judged as fairly as in the summary.
2. For each contribution, the work states that carry it (modules, derivations, systems, datasets), with `where` and `novel` only on what is new.
3. Use an `evidence` state for a proof, observation, qualitative analysis or worked example that supports the claim. Cite its location and link it from the relevant work or contribution. Use an `experiment` state for an experimental result, with the environment and total workload in `sub`, and transitions from the work it tests, labeled with the result. Set `weak` when the experiment does not isolate that work, is simulation-only for a real-world claim, or is too small.
4. Context states only when they explain the paper or expose an important weakness.

Use about 8 to 16 states, listed by role in that order, and link each state to the review points about it in `points`.

### 9. Verify before writing the files

Reread the draft as a skeptical co-reviewer who wants to catch you being unfair or wrong. Go through the checklist at the end of [references/calibration.md](references/calibration.md). In short, search `paper.txt` for every quote, check every number against the table image, grep for synonyms before writing that the paper does not state something, redo every calculation, make sure each request is proportionate to the recommendation, and, in an external review, make sure no point explains an observation on the authors' behalf. When a point fails, fix or drop it. Do not keep a flawed point and hope Hang catches it.

Use the technical log to try to refute each material finding against the paper and appendix. Check for a matched control, a different aggregation, a qualification, or an assumption that would remove the concern. Update its disposition and carry the verified findings into the review. Where uncertainty affects the recommendation, record the attempted checks and consequential coverage limits in its evidence.

### 10. Write the files and check them

1. Create `<paper>/review/` and copy `<review-template>/review.html` into it unchanged. Copy it fresh each time, since the template is the newest version of the page.
2. Write `<paper>/review/review-data.js`. The first line is a comment naming the venue and submission. Then `window.REVIEW_DATA = { ... }` and a final line with `;`. The part from the first `{` to the last `}` must be strict JSON (double quotes, no trailing commas, no comments), because `writing_style_ref/tools/import_review.py` reads it that way. Set `review_id` to a unique identifier derived from this paper's title or submission id, `generated` to the current local time, and `paper` to `{ "id": ..., "venue": ... }` from the supplied manuscript and review form.
3. Run the checker and fix every error. Check each warning in context. A vocabulary match is a prompt to inspect the sentence. Edit only when the wording impairs accuracy, clarity or the intended voice.

```
node SKILL_DIR/review-tools/check_review.js <paper>/review/review-data.js
```

4. Open the page for Hang, for instance with `Start-Process "<full path>\review.html"` in PowerShell.

### 11. Hand off and wait

Tell Hang, briefly:

- the path of the page, and how many points each section has;
- the recommendation, and the alternative if it was a judgment call;
- the two or three points you are least sure about, so Hang can start there;
- which reference-review points were dropped, in one line;
- for venue form fields the page does not hold (scores, confidence, questions for the authors, limitations), suggested values in the chat if the venue's form needs them, following how Hang filled them in the past reviews, when available;
- if the venue form asks about LLM use in reviewing, that the answer there needs to reflect how this draft was made.

Then wait for Hang's decisions. Do not write a final review elsewhere or submit anything.

## Revising after Hang's decisions

The page's "Save decisions" button writes `<review_id>.decisions.<timestamp>.json` into the page's own folder, `<paper>/review/`, in browsers that can write to a folder (Chrome and Edge). The first save asks Hang to choose that folder once. In other browsers, or when Hang picks "Download instead", the file goes to Downloads. When Hang says the decisions are saved, look in the review folder first, then in Downloads, and take the newest file for this `review_id`. When Hang brings one back, or says which points to change:

- An accepted point stays as it is. A point with `revised_override` takes Hang's text as its new `revised`, since that is Hang's own wording, whether or not Hang accepted it yet. A `comment` is Hang's note on that point, on any status: follow it. On a rejected point it says why, so rewrite the point as it asks, or drop it. A reference with `verdict: "disagree"` and a note means the evidence or the point is wrong, so fix it.
- The top-level `notes` are Hang's notes on the whole review, such as a point to add or a change across sections. Act on each one, and say in the summary how, or why not.
- Read all relevant saved batches in time order, with later decisions taking precedence. Hang's edited wording carries more weight than an acceptance without edits. Do not infer pending decisions unless Hang asks; when asked, record inferred decisions separately from explicit choices and explain the basis. Preserve claims, data, citations, and terms, make each change as narrow as possible, and do not propose a rejected change again without addressing the rejection.
- Keep the ids of unchanged items. The page drops a saved decision only when the text or evidence under it changes, so unchanged points keep their decisions.
- Update `generated`, rerun the checker, and summarize what changed.
- Hang's edits and rejections are the strongest evidence of the reviewing style. If Hang wants them kept, offer to move a decisions file that went to Downloads into the review folder and run `python <writing-style>/writing_style_ref/tools/import_review.py <paper>/review`, and ask before running it, since it changes the shared style reference. An installed copy is replaced on the next install or plugin update, so run it on the repository's copy (`plugins/writing-style/skills/writing-style/`) and update the installation.

## Edits to a manuscript's text

When Hang asks for edits to a document whose source you have, rather than a review (for example Hang's own paper, a co-authored draft, or the text of a response to reviewers), propose them on the editing page so that Hang accepts, rejects, or rewords each one before it is applied.

1. Read `<edit-template>/README.md`. It specifies `items.txt`, the page, the decision batches, and the apply step. Its scripts run on Python 3.8 or newer.
2. Create a review folder inside the document's root folder, such as `<root>/waiting_for_review/<name>/`. Record Hang's request word for word as `@request R1`. Give each edit an `@item` with `type:`, `file:` relative to the root, a `note:` with the reason and the style principle it follows, and `--- original` copied exactly from the source with its `--- revised`. Add `markers: no` under `@review` unless the document defines the `\hang` macro and Hang wants the changes tagged.
3. Word the edits with Hang's writing style reference, especially "Correcting a sentence without rewording it" and "Adding sentences that were not asked for": correct without rewording, keep a correction separate from optional rewording, and check earlier decisions before proposing a change again.
4. Build with `python <edit-template>/build_review.py <root>/waiting_for_review/<name> --root <root>`, fix any passage reported as missing or not unique, and open `review.html` for Hang.
5. After Hang saves a batch, run `python <edit-template>/apply_decisions.py <root>/waiting_for_review/<name> --root <root>` as a dry run, and run it with `--write` when Hang confirms. Only accepted items are applied, with Hang's wording where it was edited.
