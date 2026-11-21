# Embedded search: a light, automatic paper search for another skill

Read this when another skill (such as `review-paper` or `polish-paper`) needs
papers for one of its checks. It is self-contained: do not read the rest of this
skill unless a step below names a file. Do not ask the user about search
settings; decide them as below and state them in one line. The calling skill
keeps its own records and decides what to do with the papers.

## The rules that do not change with depth

- Never list a paper from memory. Every paper was found by a search in this
  session and verified by fetching its canonical record. Every field (title,
  authors, venue, date, affiliation, a number you quote) comes from a fetched
  page, or it is `unknown`.
- Search snippets choose what to open; they never support a claim.
- **Confidential manuscripts.** When the caller says the manuscript is
  confidential (a peer review), search only with public technical terms. Never
  search its title or paste its text into a search engine, web form, or API.
  Skip any version of the manuscript you come across, and do not open it.
- Do not use paywall-bypass services. For a locked paper, try the arXiv version,
  the authors' copy, Semantic Scholar `openAccessPdf`, OpenAlex
  `best_oa_location`, or Unpaywall; otherwise use the abstract page only and
  mark deeper claims `unknown`.

## Settings, decided automatically

| Setting | How to decide |
|---|---|
| Purpose | From the caller: `novelty` (closest existing work), `baselines` (what the work should compare against), `coverage` (what a related-work section should cite), `support` (a source for one claim), or `sota` (the current best on a task). Several can apply. |
| Keywords | From the caller's notes, in public technical terms (see step 1): the problem, each component of the approach, and the evaluation. Add method and benchmark names that the first results use. |
| Date window | A review: public before the submission deadline (later work is context only). A draft being written: the last five years plus foundational work, unless the caller says otherwise. |
| Number of papers | `novelty` or `baselines`: 6–8. `coverage`: 8–12. `support`: 1–3. `sota`: 5–8. |
| Institutions | `reputable` by default: rank and list papers with at least one author at a well-known institution (below). The caller can pass `institutions: any`. |
| Depth | `light` unless the caller asks for more. |
| Extras | None: no result file, relationship graph, classic work, or visualization. |

## Budget

Up to 12 searches and 15 page fetches or API calls, verification included. A
batched call (one arXiv `id_list` request with many ids, one Semantic Scholar
batch) counts once. Stop earlier when two rounds add no new in-scope paper. When
a source answers HTTP 429, an exhausted budget, or a bot check twice, treat it
as unavailable for the rest of the run and use another.

## Procedure

1. **Plan the queries before searching.** Break the work into its parts and
   write one query for each:
   - the **problem** (a broad and a narrow phrasing);
   - **each component of the approach** as its own mechanism. A system that
     "tracks a person with a depth camera, predicts their next action with a
     sequence model, and replans the robot's path around it" has three
     components, and each has its own prior work (person tracking, human action
     prediction, reactive motion planning). Searching only the combination
     misses the work behind each part;
   - the **evaluation** (benchmark, dataset, task, or study design);
   - for `coverage`, one query for a recent **survey** of the area, whose
     section headings show the subareas a related-work section is expected to
     cover.
   Usually six to ten queries in all.
2. **Search.** Run the queries across web search (WebSearch or the platform's
   equivalent) and one scholarly index (the arXiv API for preprints; Crossref,
   DBLP, or Semantic Scholar for published work). In fields where much work
   appears only in ACM or IEEE proceedings, such as HRI and CHI, aim at least one
   query at those proceedings, for example Crossref
   `https://api.crossref.org/works?query.bibliographic=<terms>&filter=from-pub-date:<YYYY>&select=DOI,title,container-title,issued&rows=40`
   and keep the hits whose `container-title` is the venue.
3. **Screen on metadata.** Use title, year, venue, and abstract. Merge versions of
   one paper. Drop the manuscript itself and anything outside the date window.
   Rank by how directly each abstract bears on the caller's question.
4. **Snowball the closest one or two papers.** Read the reference list (the arXiv
   HTML bibliography needs no API quota) and the experiments section. The methods
   those papers compare against are the field's current baseline set. Add
   in-scope papers you had missed. For `baselines`, also report every method
   named in those comparison tables, even the ones you do not open, as "named in
   <paper>, Table N" with the URL of the page you read: the name comes from a
   fetched page, so it is grounded, but say that the method itself was not
   checked.
5. **Verify what you will list.** Confirm the title and date of every arXiv paper
   in one arXiv API call (`https://export.arxiv.org/api/query?id_list=<id1>,<id2>,...`),
   and DOIs through Crossref. Then fetch the full page (the arXiv HTML page gives
   the author block, affiliations, and results) only for the papers whose claims
   or affiliations you will pass on. Take every claim from the paper's own text,
   with its URL. For a review, compare against the version public before the
   deadline: the arXiv abstract page lists each version's date, and
   `arxiv.org/abs/<id>v1` opens the first one.
6. **Institutions** (unless the caller passed `any`). Read this skill's
   `references/topics/institutions/general.md`, plus the one topic file in that
   folder that matches the field (such as `robotics.md`). A paper
   matches when at least one author's affiliation in the paper's own author block
   is on the list, matched on whole names (MIT is not "submit"; the University of
   Washington is not Washington University in St. Louis; a lab counts for its
   parent institution). If the author block gives no affiliation, the paper is
   `unresolved`, which says nothing about its authors.
   For `novelty` and `baselines` checks, a paper that fails only this filter but
   could change the caller's judgment (the same mechanism, or a baseline the work
   must beat) is not dropped silently: list it under "Outside the institution
   filter" with one line on why it matters.
7. **Return** the result below. Write nothing else to disk unless the caller
   names a file.

## What to return

A short header line: purpose, date window, institution setting, searches and
fetches used, and sources that were unavailable.

Then a table, one row per paper, ordered by how much it matters to the caller.
For `coverage`, group the rows under the related-work subsections they belong
to (the survey's headings help name them).

| Paper | Date, venue | Role | Why it matters to the caller | Evidence |
|---|---|---|---|---|
| [Title](canonical link), first author et al. | 2024-08, ICML 2024 | closest work / baseline / related / support | One sentence tied to the caller's claim, with the key number when there is one | URL(s) actually read |

Add an "Institution" column when the filter is on (the matching institution, or
`unresolved`). Then, when they exist:

- **Outside the institution filter** — papers kept for the reason in step 6.
- **Baselines named in the closest papers** (for `baselines`) — the methods in
  their comparison tables that you did not open, each with the table and URL.
- **Discarded** — candidates you looked at and set aside, each with a short
  reason (for example "later than the deadline", "different task").
- **Limits** — what was not checked: unavailable sources, papers read only at
  the abstract, a budget that ran out.
