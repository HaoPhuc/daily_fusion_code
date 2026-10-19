**Not yet**

Reported time: more than an hour (stated ~25 min). That's on me, not you: the exercise was sized for someone who already knows the syntax. The next ones are smaller and come with a syntax box.

## What works
- `decay_rate` and `exact_decay` are correct, and `exact_decay` works for numbers and arrays alike.
- The Euler update `N[k+1] = N[k] - lam*N[k]*dt` is exactly right. That's the core idea of the method.
- `main()` has the right plan: loop over `dt`, take the last value, compare with the exact one, divide consecutive errors.

## Problems
The program stops with an error before printing any numbers. There are three small bugs, each hiding the next:

1. **`solution.py`, line 11: `np.linspace(0, t_end, t_end/dt, ...)`.** Python raises `TypeError: 'numpy.float64' object cannot be interpreted as an integer`. The third argument of `linspace` is a *number of points*, so it must be an `int`, and `50/5` is the float `10.0`. There is a second issue on the same line: from 0 to 50 in steps of 5 you need **11** points (0, 5, …, 50), not 10. With 10 points the spacing becomes 50/9 ≈ 5.56, so your `t` array no longer matches the `dt` you use in the update.
   *Hint:* compute the number of steps first with `n = round(t_end / dt)`, then ask `linspace` for `n + 1` points.
2. **Line 14: `for k in range(len(t)):`** On the last pass `k` is the last index, so `N[k+1]` points past the end of the array (`IndexError`). With `n + 1` points there are only `n` steps to take.
   *Hint:* what should the loop range be if each pass fills in `N[k+1]`?
3. **Line 48: `np.abs(N_euler - N_exact)`.** `N_euler` is your whole array of four results, so this is an array, and it can't be stored in the single slot `relative_err[k]` (`ValueError: setting an array element with a sequence`).
   *Hint:* you want only the result for the current `dt`.
4. **Line 27: `N0 = 1 * np.exp(6)`** is $e^6 \approx 403$, not $10^6$. In Python, one million is written `1e6`. (It doesn't change the *relative* error, but the habit matters.)
5. **Line 62:** the conclusion comment is missing. Once the code runs, the ratio column comes out close to 2. That is the whole point of the exercise: see below.

## One thing to learn
**Halving $\Delta t$ halves Euler's error, so Euler is a first-order method:** global error $\approx C\,\Delta t^{1}$. In general, if the ratio of successive errors is $2^p$, the method has order $p$. Today's retry gives you another go at exactly this, with the code structure already written.

Off-by-one errors (point count vs step count, `range(n)` vs `range(n+1)`) are the most common bug in all numerical code, in every language. A good habit: before the loop, write down in a comment how many points and how many steps there are.

<details><summary>Reference solution</summary>

```python
import numpy as np


def decay_rate(half_life):
    return np.log(2) / half_life


def euler_decay(N0, lam, dt, t_end):
    n = round(t_end / dt)              # number of steps
    t = np.linspace(0, t_end, n + 1)   # n + 1 points
    N = np.zeros(n + 1)
    N[0] = N0
    for k in range(n):
        N[k + 1] = N[k] - lam * N[k] * dt
    return t, N


def exact_decay(N0, lam, t):
    return N0 * np.exp(-lam * t)


def main():
    N0, t_end = 1e6, 50.0
    lam = decay_rate(12.32)
    N_ex = exact_decay(N0, lam, t_end)
    prev = None
    for dt in [5, 2.5, 1.25, 0.625]:
        t, N = euler_decay(N0, lam, dt, t_end)
        err = abs(N[-1] - N_ex) / N_ex
        ratio = "" if prev is None else f"{prev / err:.3f}"
        print(f"{dt:6.3f}  {err:.4f}  {ratio}")
        prev = err


if __name__ == "__main__":
    main()

# The ratio tends to 2: halving dt halves the error, so Euler is first order.
```

Output:
```
 5.000  0.3875
 2.500  0.1964  1.973
 1.250  0.0986  1.991
 0.625  0.0494  1.997
```
</details>
