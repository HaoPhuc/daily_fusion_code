# How small is small? Machine epsilon
**Mon 19 Oct 2026 · Python · NUM-1.1 · Level 1 · Week 2 · ~15 min**

A computer stores a number like $1.0$ or $10^{20}$ with only about 16 significant digits. Today you measure that limit yourself: the **machine epsilon** $\varepsilon$, the smallest relative change a 64-bit float can still see. Then you check what it means for a plasma with $10^{20}$ ions. Every error estimate later in the NUM track rests on this number.

New to floating-point numbers? Read [the theory PDF](2026-10-19_NUM-1.1_theory.pdf) first.

## Syntax you'll need
```python
x = 1.0
while x > 0.1:            # repeat as long as the condition is True
    x = x / 2             # 1.0 -> 0.5 -> 0.25 -> ...
count = count + 1         # add one to a counter
a == b                    # True or False
print(f"{x:.6e}")         # scientific notation, 6 decimals
```

## Tasks
1. **Find $\varepsilon$ by halving** in `machine_epsilon()`. TODO 1a: the `while` condition, "$1.0 + \varepsilon/2$ is still bigger than $1.0$". TODO 1b: halve `eps`.

   *Hint:* the loop stops at the last `eps` for which adding it to $1.0$ still changes the result. Compare your value with NumPy's line printed under it.
2. **Adding one ion to $10^{20}$** in `main()`. TODO 2a: estimate the gap between $N = 10^{20}$ and the next float as $N\varepsilon$. TODO 2b: test whether `N + added` is still equal to `N`. TODO 2c: complete the sentence at the bottom of the file.

   *Hint:* for 2b, `==` already gives `True` or `False`, so `same = (N + added == N)` needs no `if`.

## Check yourself
You should get $\varepsilon \approx 2.22 \times 10^{-16}$, and `N + 1 == N` prints `True`.

## Submit
Commit and push `solution.py`. Optional: replace `??` on its first line with how long it took you (e.g. `# time: 15 min`).

*If you have time:* try `1e308 * 10` and `np.exp(-800.0)` and look up both results in the theory note.
