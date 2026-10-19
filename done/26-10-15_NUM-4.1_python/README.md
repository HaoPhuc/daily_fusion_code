# Tritium decay with Euler's method
**Thu 15 Oct 2026 · Python · Week 1 · ~25 min**

Tritium, the fuel stored next to a D-T reactor, decays with a half-life of 12.32 years. The number of nuclei follows

$$\frac{dN}{dt} = -\lambda N, \qquad \lambda = \frac{\ln 2}{t_{1/2}}$$

You'll solve this ODE with the explicit Euler method and measure how the error depends on the time step.

New to Euler's method? Read [the theory](26-10-15_NUM-4.1_python.pdf) first.

## Tasks
Fill in `solution.py`. Use only `numpy` and `math`, not `scipy`.

1. `decay_rate(half_life)`: return $\lambda$.
2. `euler_decay(N0, lam, dt, t_end)`: integrate from t = 0 to t_end with explicit Euler, using a loop. Return two NumPy arrays `t` and `N` that include both the start and the end point. You can assume `t_end / dt` is a whole number.
3. `exact_decay(N0, lam, t)`: return the analytic solution at times `t` (works for a number or an array).
4. `main()`: take N0 = 1e6, t_end = 50 years, and dt = 5, 2.5, 1.25, 0.625 years. For each dt, print:
   - dt
   - the relative error at `t_end`, $|N_\text{euler} - N_\text{exact}| \,/\, N_\text{exact}$
   - the ratio of the previous error to this one (skip it for the first row)

## Check yourself
Your relative error for dt = 5 should be about 0.39.
Look at the ratio column and add one comment line at the bottom of `solution.py` saying what it tells you about Euler's method.

## Submit
Commit and push `solution.py`.
