# AGENTS.md: rules for the daily run

These are the rules for the scheduled run that checks solutions and posts each day's exercise. Phuc can edit this file to change how the run behaves. The scheduled task prompt supplies only the things that shouldn't sit in a public repo: the git author identity and the email address.

## 1. Mission
Phuc learns to code for fusion / plasma physics and computational research through one exercise per day. Each exercise is real practice (he writes code), comes with a short theory note, and gets honest feedback. Progress follows a fixed curriculum, so topics build on each other with no gaps.

## 2. The learner
Second-year Applied Physics student. Already knows:
- calculus, Taylor series, analytic ODEs, linear algebra and basic physics;
- Python with NumPy, pandas, Matplotlib and SciPy at a user level;
- basic MATLAB.

New to:
- numerical methods as a subject (error, stability, convergence);
- Fortran and Simulink;
- formal data structures and algorithms;
- HPC.

He reads Tao Pang's *An Introduction to Computational Physics* alongside the NUM track. Teach from first principles, explain *why*, be direct, and skip the filler.

## 3. Settings
```yaml
TIMEZONE: Europe/Amsterdam
RUN_TIME: "07:55"            # exercise ready by 08:00
WEEK_1_MONDAY: 2026-10-12    # week numbers count from here
EXAM_MODE_UNTIL: 2026-11-08  # inclusive; short exercises until then (see section 6)
```

## 4. Weekly schedule
| Day | Track | Language | Curriculum |
|-----|-------|----------|------------|
| Mon | NUM | Python | `curriculum/NUM.md` |
| Tue | CTRL | MATLAB | `curriculum/CTRL.md` |
| Wed | FT | Fortran | `curriculum/FT.md` |
| Thu | DSA | Python | `curriculum/DSA.md` |
| Fri | CTRL | Simulink (MATLAB script in exam mode) | `curriculum/CTRL.md` |
| Sat | FT | Fortran (longer) | `curriculum/FT.md` |
| Sun | NUM | Python (longer) | `curriculum/NUM.md` |

## 5. Choosing today's topic
1. Take today's track from the schedule.
2. **Retry first.** If the most recently checked exercise in this track got **Partly correct** or **Not yet**, and that topic hasn't had a retry yet, today is a short retry on the same topic with a new problem. Mark it "(retry)" in LOG.md.
3. **Otherwise, the next new topic.** Pick the earliest topic ID in the track's curriculum that has no exercise yet (check the Topics column of LOG.md). An exercise that is posted but not yet solved doesn't block progress.
4. Normally one topic per exercise. A long weekend exercise outside exam mode may cover two adjacent topics.
5. On Sundays, the exercise also reuses one earlier topic from the past week, from any track, preferring one that isn't mastered yet.
6. Never skip, reorder or invent topics. If a topic needs a method from another track that Phuc hasn't done yet, explain that method in THEORY.md.
7. If a track's curriculum is finished, post a review exercise for that track and say in the email that the track is complete, so Phuc can decide what comes next.

A topic counts as **mastered** once an exercise on it gets the verdict **Correct**.

## 6. Exercise size
| Mode | Weekdays | Sat / Sun | Theory |
|------|----------|-----------|--------|
| Normal | 20–40 min | 60–90 min | 1–2 PDF pages |
| Exam mode (today ≤ `EXAM_MODE_UNTIL`) | 10–15 min | 20–30 min | at most 1 page |

In exam mode:
- each exercise has one small, focused concept;
- the starter file gives more scaffolding;
- Friday's CTRL exercise is a MATLAB script, not a Simulink model.

The times don't include reading the theory.

## 7. Checking solutions
Look at every folder in `exercises/` that has no `FEEDBACK.md`. A folder counts as submitted if `git log --format='%ce' -- <folder>` shows a committer email other than `noreply@anthropic.com`. Skip untouched folders.

For each submitted folder:
- Run the code:
  - Python: `python3`
  - Fortran: `gfortran -Wall -fcheck=all`, then run the binary
  - MATLAB: `octave-cli`. If he used MATLAB-only syntax, judge it by reading.
  - Simulink: you can't simulate. Unzip the `.slx`, read the block-diagram XML, and check the plot or data he committed.
- Compare his results with your own reference solution, written and run in a scratch directory.
- Write `FEEDBACK.md`:
  - first line: the verdict, one of **Correct**, **Partly correct** or **Not yet**;
  - what works (1–3 bullets);
  - problems, each with file and line, why it's wrong, and a hint toward the fix (don't silently rewrite his code);
  - one thing to learn;
  - a short reference solution inside `<details><summary>Reference solution</summary> ... </details>`.
- Set the exercise's status in LOG.md to `checked: <verdict>`.

Never modify his solution files.

## 8. Writing the exercise
Folder: `exercises/YYYY-MM-DD_ddd_lang_slug/` (lang = `python`, `matlab`, `fortran` or `simulink`). If a folder dated today already exists, don't post another one. The folder holds four files.

**`README.md`**, the task. It contains:
- the title (`# ...`);
- a meta line in exactly this format, which the PDF builder reads: `**<Ddd> <D> <Mon> <YYYY> · <Lang> · <TOPIC-ID(s)> · Week <n> · ~<min> min**`;
- 2–4 lines of context;
- a pointer to the theory: "New to X? Read [THEORY.md](THEORY.md) first.";
- numbered tasks with exact function signatures and inputs;
- a **Check yourself** section with 1–2 numbers he should get;
- a **Submit** section saying which files to commit.

Write all math as LaTeX (`$...$`, `$$...$$`), never as plain-text formulas.

**`THEORY.md`**, starting with `# Theory: <topic>`. It covers what's new to him:
- the idea and intuition;
- key formulas with a derivation sketch;
- error, stability or complexity where relevant;
- for new language features, a minimal syntax example that is *not* the solution;
- 2–4 tips or pitfalls.

For NUM topics, name the matching Tao Pang chapter. Teach the concept without giving away the answers. If a topic was covered before, write a short refresher that links the earlier THEORY.md.

**Starter file** with stubs: `solution.py`, `solution.m` or `solution.f90`. For Simulink, a `params.m` instead.

**The PDF**, which is what Phuc actually reads:
1. Run `python3 tools/make_pdf.py exercises/<folder>`.
2. If the script reports math errors, fix the LaTeX and rebuild.
3. Look at every page: run `pdftoppm -r 70 -png`, then open the images. Check there is no raw `$`, nothing is cut off, and the last page isn't nearly empty (if it is, tighten the wording).
4. Don't edit `tools/make_pdf.py` unless it is actually broken.

Before committing:
- verify every "Check yourself" number and every number in THEORY.md with your own reference solution (don't commit the reference solution);
- make sure Python and Fortran starters parse or compile.

Add a row to LOG.md.

## 9. LOG.md
One row per exercise: `| Date | Day | Track | Lang | Topics | Exercise | Status |`
- Topics: topic IDs, plus "(retry)" for retries.
- Status: `open`, or `checked: <verdict>`.

LOG.md is the record of progress. Keep old rows; only change their status.

## 10. Commit and push
1. Stage the files this run created or changed, then `git fetch origin main` and `git rebase origin/main`.
2. Make one commit, using the author identity from the task prompt, with a message like `Feedback: <exercises>; new: <date> <lang> <title>`.
3. Push with `git push origin HEAD:main`.
4. Confirm with `git fetch origin main && git status -sb`.

Never force-push or rewrite history. If the push fails, still send the email and say so at the top.

## 11. Email
Send one short email, in simple HTML plus a plain-text body, to the address in the task prompt.
- **Subject:** `Daily code — <Ddd D Mon>: <title> (<Lang>)`
- **Body:**
  - one line per checked exercise: the name, the verdict in bold, and the main point;
  - or "No new solutions to check.";
  - if 3 or more exercises are open, "<n> exercises still open." (just the count);
  - today's exercise: title, language, topic ID, estimated time, the new concepts in a few words, and a link to the folder on GitHub;
  - finally, "Task + theory attached as PDF."
- **Attachment:** the PDF (base64 via `base64 -w0`).
- If sending fails, create a draft. If the attachment keeps failing, send without it and say the PDF is in the repo.

## 12. When something goes wrong
Never end silently. If the run can't post an exercise (a missing curriculum file, a broken tool, a LOG.md that conflicts with the curriculum), don't guess. Leave the repo consistent, and send the email explaining what stopped and what Phuc should do.
