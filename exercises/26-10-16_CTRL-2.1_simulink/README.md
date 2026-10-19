# Coil current: a first-order system in Simulink
**Fri 16 Oct 2026 · Simulink · Week 1 · ~35 min**

A tokamak's poloidal-field coils are driven by power supplies, and to first order each coil is an RL circuit. When the supply switches on a voltage $V_0$, the coil current obeys

$$L\,\frac{dI}{dt} = V_0 - R\,I, \qquad I(0) = 0$$

You'll build this as a block diagram, then run it with Simulink's Euler solver to see yesterday's stability limit in a new setting.

New to Simulink or time constants? Read [the theory](26-10-16_CTRL-2.1_simulink.pdf) first.

## Tasks
Parameters are in `params.m`: `L = 0.02` H, `R = 0.1` Ω, `V0 = 50` V, `t_stop = 1.5` s. Run it before simulating (or call it from the model's InitFcn callback, see the theory).

1. **Build `model.slx`.** Use only these blocks: Step, Sum, Gain, Integrator, To Workspace (plus a Scope if you like).
   - Step: step time `0`, initial value `0`, final value `V0`.
   - Integrator output is `I`, initial condition `0`.
   - Use the variable names `L`, `R`, `V0` in the block parameters, not typed-in numbers.
   - To Workspace: variable name `I_out`, save format **Timeseries**.
   - Stop time `t_stop`.
2. **Accurate run.** Solver: variable-step `ode45`, *Max step size* `0.01`. Run it.
3. **Write `analysis.m`** that:
   - runs `params`, then simulates with `out = sim('model');`
   - plots `I(t)` from Simulink together with the analytic solution (derive it yourself) on one axis,
   - reads off from the simulation: the final current, and the time at which $I$ first reaches 63.2 % of the final current,
   - then re-runs the model with the fixed-step `ode1` solver for step sizes `h = 0.05, 0.3, 0.5` s and prints `I` at `t_stop` for each,
   - saves the figure as `output.png` (second subplot: the three `ode1` runs, use markers so you can see the steps).
4. **Answer in `answers.md`** (a few lines):
   - the measured time constant and how it compares to the formula,
   - what happens for each `h`, and the largest `h` for which `ode1` is stable here. Derive that limit by hand, don't just read it off the plot.

## Check yourself
- `ode45`: $I(0.2\ \text{s}) \approx 316$ A.
- `ode1`, `h = 0.05`: $I(0.2\ \text{s}) \approx 341.8$ A.

## Submit
Commit and push `model.slx`, `analysis.m`, `output.png` and `answers.md`.
