# Theory: Euler's method, a refresher

A short recap of [the first Euler note](../exercises/2026-10-15_python_tritium-decay/2026-10-15_python_tritium-decay_theory.pdf). In Tao Pang this is chapter 4 (ordinary differential equations), the first section on initial-value problems.

## The method
For $\dfrac{dy}{dt} = f(t, y)$ with $y(0) = y_0$, Euler steps along the current slope:

$$y_{k+1} = y_k + \Delta t\, f(t_k, y_k)$$

Each step drops the $\tfrac12 \Delta t^2 y''$ term of the Taylor series, so its **local error** is $\sim \Delta t^2$. Reaching a fixed time $T$ takes $T/\Delta t$ steps, so the **global error** is $\sim (T/\Delta t)\,\Delta t^2 \sim \Delta t$.

## Reading the order from a table
If the global error behaves like $E \approx C\,\Delta t^{\,p}$, then halving $\Delta t$ gives

$$\frac{E(\Delta t)}{E(\Delta t/2)} \approx \frac{C\,\Delta t^{\,p}}{C\,(\Delta t/2)^{p}} = 2^{p}$$

So a ratio near 2 means $p = 1$, near 4 means $p = 2$, near 16 means $p = 4$.

## Worked example (different numbers, same steps)
A coil with $L = 4$ H and $R = 2\ \Omega$ is switched onto $V = 12$ V: $\dfrac{dI}{dt} = \dfrac{V - RI}{L}$, $I(0) = 0$. With $\Delta t = 0.5$ s:

$$I_1 = 0 + 0.5 \cdot \frac{12 - 2\cdot 0}{4} = 1.5\ \text{A}, \qquad I_2 = 1.5 + 0.5 \cdot \frac{12 - 2\cdot 1.5}{4} = 2.625\ \text{A}$$

The exact value is $I(1\,\text{s}) = 6\,(1 - e^{-0.5}) \approx 2.361$ A. Euler overshoots, because it uses the slope at the start of each step, and the slope keeps decreasing.

## The three bugs from last time
- **Points vs steps.** $n$ steps need $n + 1$ points. `np.linspace(0, t_end, n + 1)`, and its third argument must be an `int`, so compute `n = round(t_end / dt)` first.
- **Loop range.** If each pass writes `W[k + 1]`, the loop is `range(n)`. With `range(n + 1)` the last pass writes past the end (`IndexError`).
- **Array vs element.** `W` is the whole history; `W[-1]` is its last value. Subtracting a whole array where you meant one number gives `ValueError: setting an array element with a sequence`.
