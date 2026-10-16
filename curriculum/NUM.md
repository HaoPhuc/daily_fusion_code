# NUM — Numerical methods (Python)

**Days:** Monday, Sunday (longer) · **Language:** Python + NumPy (no SciPy solvers unless the topic says so)

Follows the chapter order of Tao Pang, *An Introduction to Computational Physics* (2nd ed.), so the exercises line up with the book. Each topic is one exercise. Use fusion or plasma examples when they fit naturally.

Status: ✅ mastered · 🔁 not mastered yet · 🟡 posted, waiting for your solution · ⬜ not started

## 1. Numbers and error (foundations)
- ⬜ **NUM-1.1** Floating-point numbers: representation, machine epsilon, overflow/underflow
- ⬜ **NUM-1.2** Round-off vs truncation error; catastrophic cancellation
- ⬜ **NUM-1.3** Order of accuracy and convergence tests on log–log plots

## 2. Approximating a function (Pang ch. 2)
- ⬜ **NUM-2.1** Polynomial interpolation (Lagrange form)
- ⬜ **NUM-2.2** Runge's phenomenon and Chebyshev nodes
- ⬜ **NUM-2.3** Linear least-squares fitting (e.g. a confinement-time scaling law)
- ⬜ **NUM-2.4** Cubic splines
- ⬜ **NUM-2.5** Random number generators: uniform generators, transforming to other distributions

## 3. Numerical calculus (Pang ch. 3)
- ⬜ **NUM-3.1** Finite-difference derivatives and their error
- ⬜ **NUM-3.2** Richardson extrapolation
- ⬜ **NUM-3.3** Trapezoid and Simpson integration
- ⬜ **NUM-3.4** Romberg integration
- ⬜ **NUM-3.5** Bisection
- ⬜ **NUM-3.6** Newton–Raphson and secant methods
- ⬜ **NUM-3.7** Finding minima: golden-section search and gradient descent

## 4. Ordinary differential equations (Pang ch. 4)
- 🟡 **NUM-4.1** Explicit Euler, local vs global error *(done early: tritium decay)*
- ⬜ **NUM-4.2** Systems of ODEs; rewriting higher-order ODEs as first-order systems
- ⬜ **NUM-4.3** Predictor–corrector / Heun (RK2)
- ⬜ **NUM-4.4** Fourth-order Runge–Kutta
- ⬜ **NUM-4.5** Energy drift and symplectic integrators (leapfrog / velocity Verlet)
- ⬜ **NUM-4.6** Charged particle in a magnetic field: the Boris pusher
- ⬜ **NUM-4.7** Stiff equations and implicit Euler
- ⬜ **NUM-4.8** Adaptive step size (embedded RK)
- ⬜ **NUM-4.9** Boundary-value problems: the shooting method
- ⬜ **NUM-4.10** Eigenvalue problems: 1D Schrödinger equation by shooting

## 5. Matrices (Pang ch. 5)
- ⬜ **NUM-5.1** Gaussian elimination
- ⬜ **NUM-5.2** LU decomposition and pivoting
- ⬜ **NUM-5.3** Tridiagonal systems (Thomas algorithm)
- ⬜ **NUM-5.4** Iterative solvers: Jacobi and Gauss–Seidel
- ⬜ **NUM-5.5** Newton's method for nonlinear systems
- ⬜ **NUM-5.6** Eigenvalues by power iteration
- ⬜ **NUM-5.7** Eigenvalue problems in physics: normal modes with `numpy.linalg`

## 6. Spectral analysis (Pang ch. 6)
- ⬜ **NUM-6.1** Discrete Fourier transform from the definition
- ⬜ **NUM-6.2** FFT and its O(N log N) cost
- ⬜ **NUM-6.3** Power spectra, windowing and the Nyquist limit (diagnostic signals)
- ⬜ **NUM-6.4** Gaussian quadrature

## 7. Partial differential equations (Pang ch. 7)
- ⬜ **NUM-7.1** Discretising PDEs; classifying elliptic, parabolic and hyperbolic equations
- ⬜ **NUM-7.2** Relaxation for Laplace/Poisson: Jacobi, Gauss–Seidel, SOR
- ⬜ **NUM-7.3** Heat equation with explicit FTCS; stability limit
- ⬜ **NUM-7.4** Crank–Nicolson
- ⬜ **NUM-7.5** Advection: upwind scheme and the CFL condition
- ⬜ **NUM-7.6** Toy Grad–Shafranov equilibrium on a 2D grid

## 8. Molecular dynamics (Pang ch. 8)
- ⬜ **NUM-8.1** N-body simulation with velocity Verlet
- ⬜ **NUM-8.2** Periodic boundaries and neighbour lists

## 9. Monte Carlo (Pang ch. 10)
- ⬜ **NUM-9.1** Monte Carlo integration and its 1/√N error
- ⬜ **NUM-9.2** Importance sampling
- ⬜ **NUM-9.3** Random walks and diffusion
- ⬜ **NUM-9.4** Metropolis algorithm (2D Ising model)
