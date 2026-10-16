# daily_fusion_code
Daily coding practice for fusion and plasma physics: numerical methods and algorithms in Python, MATLAB/Simulink and Fortran, with theory notes and feedback.

## How it works
- A new exercise appears in `exercises/` every day just after midnight (Amsterdam time).
- Each exercise folder has a PDF named after the folder, with the task and the theory in one easy-to-read file. It also has the same content as `README.md` (task) and `THEORY.md` (theory), plus a starter file.
- Write your solution in the starter file, then commit and push.
- The next run checks every solved exercise that has no feedback yet. It writes `FEEDBACK.md` in that folder and emails a short summary.
- Late is fine. An exercise gets checked whenever you push it.
- Want a re-check after fixing something? Delete that folder's `FEEDBACK.md` and push.
- `LOG.md` lists every exercise with its status.

## Weekly schedule
| Day | Language | Size |
|-----|----------|------|
| Mon | Python | ~20–30 min |
| Tue | MATLAB | ~20–30 min |
| Wed | Fortran | ~20–30 min |
| Thu | Python | ~20–30 min |
| Fri | Simulink | ~20–30 min |
| Sat | Fortran | ~1–1.5 h |
| Sun | Python | ~1–1.5 h |

Topics mix numerical methods and programming fundamentals (data structures, algorithms), and get harder week by week.

## Notes on checking
- **Python:** run with Python 3 and NumPy. Only use other libraries if the task allows them.
- **Fortran:** compiled with `gfortran`.
- **MATLAB:** run in GNU Octave, so stick to core MATLAB (no toolboxes) unless the task says otherwise.
- **Simulink:** the model is reviewed but can't be simulated. Also commit the plot or exported output the task asks for.
