# Heating a plasma: Euler's method, second try
**Sun 18 Oct 2026 · Python · NUM-4.1 · Level 1 · Week 1 · ~20 min**

A retry of Euler's method with a new problem. When the heating switches on, the energy $W$ stored in a tokamak plasma rises until the heating power $P$ balances the losses $W/\tau_E$:

$$\frac{dW}{dt} = P - \frac{W}{\tau_E}, \qquad W(0) = 0$$

Take $P = 10$ MW and $\tau_E = 2$ s, so $W$ is in MJ. The starter file has the whole program; you fill in five short `TODO` gaps and see how Euler's error shrinks with $\Delta t$.

New to Euler's method? Read [the theory](26-10-18_NUM-4.1-retry_python.pdf) first; it ends with the three bugs from last time.

## Syntax you'll need
```python
n = round(7.5 / 2.5)      # round() gives a whole number (int): 3
x = np.zeros(n + 1)       # array of n + 1 zeros
for k in range(n):        # k = 0, 1, ..., n - 1
    x[k + 1] = x[k] + 2   # fill the next slot from the current one
x[-1]                     # last element of an array
abs(a - b)                # absolute value
```

## Tasks
1. **Euler step** in `euler_energy(dt, t_end)`. TODO 1a: the number of steps `n`. TODO 1b: one Euler step, $W_{k+1} = W_k + \Delta t \left(P - W_k/\tau_E\right)$.
2. **Error and ratio** in `main()`. TODO 2a: the absolute error at `t_end`, $|W_\text{Euler} - W_\text{exact}|$ (`exact_energy` is given). TODO 2b: the previous error divided by this one.

   *Hint:* `W` holds the whole time history; you only want its last value.
3. **Conclusion.** Look at the ratio column and complete the sentence in the comment at the bottom of the file.

## Check yourself
For $\Delta t = 1$ s, Euler gives $W(4\,\text{s}) = 18.75$ MJ against the exact $17.29$ MJ, so the error is about $1.457$ MJ.

## Submit
Commit and push `solution.py`. Optional: replace `??` on its first line with how long it took you (e.g. `# time: 20 min`).
