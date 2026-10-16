# CTRL — Signals and control (MATLAB / Simulink)

**Days:** Tuesday (MATLAB script), Friday (Simulink) · **Language:** core MATLAB, no toolboxes (the checker runs Octave); Simulink on Fridays

Builds from MATLAB basics and dynamic systems through feedback and signal processing to extremum seeking control (dither, demodulation, filtering). Without the Control System Toolbox, compute transfer functions and frequency responses by hand. A topic can be done on either day; Fridays use Simulink where a block diagram makes sense.

Status: ✅ mastered · 🔁 not mastered yet · 🟡 posted, waiting for your solution · ⬜ not started

## 1. MATLAB foundations
- ⬜ **CTRL-1.1** Scripts vs functions; function files and local functions
- ⬜ **CTRL-1.2** Vectors, indexing and logical masks
- ⬜ **CTRL-1.3** Vectorisation vs loops (with timing)
- ⬜ **CTRL-1.4** Plotting well and exporting figures
- ⬜ **CTRL-1.5** Structs for parameters and results

## 2. Dynamic systems
- 🟡 **CTRL-2.1** First-order systems and the time constant *(done early: coil current, Simulink)*
- ⬜ **CTRL-2.2** Second-order systems: natural frequency and damping
- ⬜ **CTRL-2.3** State-space form
- ⬜ **CTRL-2.4** Simulating with `ode45` in a script
- ⬜ **CTRL-2.5** Linearising around an operating point
- ⬜ **CTRL-2.6** Discrete-time systems and sampling a continuous system

## 3. Feedback control
- ⬜ **CTRL-3.1** Open loop vs closed loop
- ⬜ **CTRL-3.2** Proportional control and steady-state error
- ⬜ **CTRL-3.3** PI control (e.g. a density controller)
- ⬜ **CTRL-3.4** Actuator saturation and integrator windup
- ⬜ **CTRL-3.5** PID and filtering the derivative term
- ⬜ **CTRL-3.6** Stability: poles and step-response specs
- ⬜ **CTRL-3.7** Frequency response and Bode plots, computed by hand
- ⬜ **CTRL-3.8** Stabilising an unstable plant (toy plasma vertical position)

## 4. Signals and filtering
- ⬜ **CTRL-4.1** Sampling and aliasing
- ⬜ **CTRL-4.2** Spectra of noisy signals with `fft`
- ⬜ **CTRL-4.3** White noise, SNR and averaging
- ⬜ **CTRL-4.4** Moving average and first-order low-pass filters
- ⬜ **CTRL-4.5** High-pass and band-pass filters
- ⬜ **CTRL-4.6** Phase lag of filters

## 5. Modulation and lock-in detection
- ⬜ **CTRL-5.1** Products of sinusoids (mixing frequencies)
- ⬜ **CTRL-5.2** Lock-in detection: demodulation plus low-pass
- ⬜ **CTRL-5.3** Recovering a small signal buried in noise

## 6. Extremum seeking control
- ⬜ **CTRL-6.1** Estimating a gradient with a dither on a static map
- ⬜ **CTRL-6.2** The basic ESC loop
- ⬜ **CTRL-6.3** Tuning: dither amplitude and frequency, gain, filters
- ⬜ **CTRL-6.4** ESC on a plant with dynamics (time-scale separation)
- ⬜ **CTRL-6.5** ESC with measurement noise
- ⬜ **CTRL-6.6** ESC on a toy reactivity proxy
