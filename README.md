# daily_fusion_code
Daily coding practice for fusion and plasma physics: numerical methods and algorithms in Python, MATLAB/Simulink and Fortran, with theory notes and feedback.

## How it works
- A new exercise appears in `exercises/` every day by 08:00 (Amsterdam time).
- Each exercise folder has a PDF named after the folder, with the task and the theory in one easy-to-read file. It also has the same content as `README.md` (task) and `THEORY.md` (theory), plus a starter file.
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
| Sun | NUM, longer, plus one topic from the week | Python |

- **Normal size:** weekdays take 20–40 min, weekends 60–90 min.
- **Exam mode** (on until 8 Nov 2026): weekdays take 10–15 min and weekends 20–30 min, and Friday is a MATLAB script instead of Simulink.
- **Mastery:** a topic counts as mastered once your solution gets **Correct**. **Partly correct** or **Not yet** brings the topic back as a short retry.
- **Progress:** `LOG.md` lists every exercise, its topic IDs and its status.
- **Rules:** `AGENTS.md` has the rules the daily run follows. Edit it to change the schedule, exam mode or anything else.

## Notes on checking
- **Python:** run with Python 3 and NumPy. Only use other libraries if the task allows them.
- **Fortran:** compiled with `gfortran`.
- **MATLAB:** run in GNU Octave, so stick to core MATLAB (no toolboxes) unless the task says otherwise.
- **Simulink:** the model is reviewed but can't be simulated. Also commit the plot or exported output the task asks for.
