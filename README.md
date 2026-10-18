# daily_fusion_code
Daily coding practice for fusion and plasma physics: numerical methods and algorithms in Python, MATLAB/Simulink and Fortran, with theory notes and feedback.

<!-- progress:start -->
![Progress](progress.svg)

Per-topic status (✅ 🔁 🟡 ⬜) is in each file in [`curriculum/`](curriculum/).
<!-- progress:end -->

## How it works
- A new exercise appears in `exercises/` every day by 08:00 (Amsterdam time).
- Each exercise folder has two PDFs plus a starter file:
  - `<folder>.pdf`: the task and the theory in one easy-to-read file;
  - `<folder>_theory.pdf`: the theory on its own, to keep as study notes.
- `README.md` is the task as text, which GitHub shows on the folder page. The theory sources are kept in `theory/`; you don't need to open them.
- Write your solution in the starter file, then commit and push.
- The next run checks every solved exercise that has no feedback yet. It writes `FEEDBACK.md` in that folder and emails a short summary.
- Late is fine. An exercise gets checked whenever you push it.
- Want a re-check after fixing something? Delete that folder's `FEEDBACK.md` and push.

## Curriculum
Exercises follow four tracks in a fixed order, so each topic builds on the last. The full topic lists are in `curriculum/`.

| Day | Track | Language |
|-----|-------|----------|
| Mon | [NUM: numerical methods](curriculum/NUM.md), following Tao Pang's *Computational Physics* | Python |
| Tue | [CTRL: signals and control](curriculum/CTRL.md), building up to extremum seeking | MATLAB |
| Wed | [FT: Fortran and HPC](curriculum/FT.md) | Fortran |
| Thu | [DSA: data structures and algorithms](curriculum/DSA.md) | Python |
| Fri | CTRL | Simulink |
| Sat | FT, longer | Fortran |
| Sun | NUM, longer (every second Sunday: a review exercise) | Python |

- **Normal size:** weekdays take 20–40 min, weekends 60–90 min.
- **Exam mode** (on until 8 Nov 2026): weekdays take 10–15 min and weekends 20–30 min, and Friday is a MATLAB script instead of Simulink.
- **Mastery:** a topic counts as mastered once your solution gets **Correct**. **Partly correct** or **Not yet** brings the topic back as a short retry.
- **Active recall:** older topics come back about 1 week, 1 month, 3 months and then 6 months after you master them.
  - Most exercises end with a short **Recall** section (about 5 min, closed book) that you answer in `recall.md` without looking at your notes.
  - Every second Sunday is a review exercise that mixes 2–3 older topics.
  - A failed recall brings the topic back a week later.
- **Progress:** the panel at the top and the marks in `curriculum/` update after every run. `LOG.md` lists every exercise, its topic IDs and its status.
- **Rules:** `AGENTS.md` has the rules the daily run follows. Edit it to change the schedule, exam mode or anything else.

## Notes on checking
- **Python:** run with Python 3 and NumPy. Only use other libraries if the task allows them.
- **Fortran:** compiled with `gfortran`.
- **MATLAB:** run in GNU Octave, so stick to core MATLAB (no toolboxes) unless the task says otherwise.
- **Simulink:** the model is reviewed but can't be simulated. Also commit the plot or exported output the task asks for.

## License
[MIT](LICENSE). Feel free to reuse the curriculum, the exercises or the tools for your own practice.
