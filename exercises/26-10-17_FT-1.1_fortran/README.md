# D-T fusion energy: your first Fortran program
**Sat 17 Oct 2026 · Fortran · FT-1.1 · Week 1 · ~25 min**

In a D-T reaction, a deuteron and a triton fuse into a helium-4 nucleus and a neutron:

$$\mathrm{D} + \mathrm{T} \;\to\; {}^4\mathrm{He} + n + Q$$

The released energy $Q$ comes from the mass that goes missing, $Q = \Delta m\, c^2$. You'll write a complete Fortran program that computes $Q$ and the energy in one kilogram of D-T fuel, and see why every Fortran program starts with `implicit none`.

New to Fortran? Read [the theory PDF](26-10-17_FT-1.1_fortran_theory.pdf) first.

## Tasks
The starter `solution.f90` already declares all physical constants (masses in u, unit conversions). Don't change them.

1. **Compile and run the skeleton** as it is:
   ```
   gfortran -Wall -fcheck=all solution.f90 -o solution
   ./solution
   ```
   It prints one line. From now on: edit, recompile, rerun.
2. **Mass defect and $Q$.** Declare `real(dp)` variables `dm` and `Q`. Compute
   $$\Delta m = (m_\mathrm{D} + m_\mathrm{T}) - (m_\mathrm{He} + m_n), \qquad Q = \Delta m \cdot 931.494\ \mathrm{MeV/u}$$
   and print both with labels (`print *, 'Q (MeV) =', Q`).
3. **Energy per kilogram.** Declare `n_per_kg` and `E_kg`. One reaction consumes one D and one T, so the number of reactions in 1 kg of fuel is $1 / \big((m_\mathrm{D}+m_\mathrm{T})\cdot u_\mathrm{kg}\big)$. Compute it and $E_\mathrm{kg} = n_\mathrm{per\,kg}\cdot Q \cdot (\text{J per MeV})$ in J/kg, and print both.
4. **Why `implicit none`?** Copy `solution.f90` to `typo.f90` and misspell `E_kg` in its `print` line only (e.g. `E_gk`). (a) Compile it: what does the compiler say? (b) Delete the `implicit none` line, compile and run: what happens? Answer in the two comment lines at the bottom of `solution.f90`; don't commit `typo.f90`.

## Check yourself
$Q \approx 17.59$ MeV and $E_\mathrm{kg} \approx 3.37\times10^{14}$ J/kg, roughly ten million times the energy in a kilogram of coal.

## Submit
Commit and push `solution.f90` (not the compiled binary).
