# Gyro-radius: your first MATLAB functions
**Tue 20 Oct 2026 · MATLAB · CTRL-1.1 · Level 1 · Week 2 · ~10 min**

Ions and electrons in a tokamak spiral around the field lines with the **Larmor radius** $r_L$. You compute it for a 10 keV plasma at $B = 5.3$ T, and on the way write your first MATLAB **functions**: named blocks with inputs, outputs and private variables. Every later CTRL exercise is built from them.

New to MATLAB functions? Read [the theory](26-10-20_CTRL-1.1_matlab.pdf) first.

## Syntax you'll need
```matlab
function out = name(in1, in2)   % a function: inputs in (), output named out
  out = in1 * in2;              % assign the output before 'end'
end
y = name(3, 4);                 % call it: y is 12
sqrt(x)    abs(q)    x^2        % square root, absolute value, power
fprintf('r = %.3e m\n', r);     % print in scientific notation, then a newline
```

## Tasks
Work in `solution.m`; run it by typing `solution` in MATLAB or with `octave-cli solution.m`.
1. **Fill in the two local functions** at the bottom of the file. TODO 1a: `v = thermal_speed(T_eV, m)` returns $v = \sqrt{k_B T / m}$, where $k_B T = e\,T_{\text{eV}}$ in joules. TODO 1b: `r = larmor_radius(v, m, q, B)` returns $r_L = \dfrac{m v}{|q| B}$.

   *Hint:* each body is one line that assigns the output (`v = ...;`, `r = ...;`). The deuteron lines already call them.
2. **Use them for the electron, then test the walls between functions.** TODO 2a: two lines, the same two calls as for the deuteron but with `m_e`. TODO 2b: uncomment `disp(v)`, run, read the error, comment it out again and finish the last sentence in the file.

   *Hint:* `thermal_speed` did create a `v`. *Where* does it live?

## Check yourself
Deuteron: $r_L \approx 2.73$ mm. Electron: $r_L \approx 0.045$ mm, about 60 times smaller.

## Submit
Commit and push `solution.m`. Optional: replace `??` on its first line with your time (e.g. `% time: 10 min`).
