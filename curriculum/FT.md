# FT — Fortran and HPC

**Days:** Wednesday, Saturday (longer) · **Language:** Fortran 2008, free-form `.f90`, built with `gfortran`

From a first Fortran program to the three layers of HPC: fast code on one core (mostly memory efficiency), OpenMP threads on one machine, then MPI across machines. Numerical content reuses methods from the NUM track, so methods learned in Python get ported to Fortran.

Status: ✅ mastered · 🔁 not mastered yet · 🟡 posted, waiting for your solution · ⬜ not started

## 1. Fortran basics
- 🟡 **FT-1.1** Program structure, `implicit none`, compiling and running
- ⬜ **FT-1.2** Types and kinds (`real64`), integer-division pitfalls
- ⬜ **FT-1.3** Control flow: `if`, `do`, `do while`, `exit`/`cycle`
- ⬜ **FT-1.4** Formatted output and reading input

## 2. Arrays
- ⬜ **FT-2.1** Static and allocatable arrays
- ⬜ **FT-2.2** Array syntax, slicing and intrinsics (`sum`, `maxval`, `matmul`, `dot_product`)
- ⬜ **FT-2.3** Column-major storage
- ⬜ **FT-2.4** 2D arrays and loop order

## 3. Procedures and modules
- ⬜ **FT-3.1** Functions and subroutines; `intent`
- ⬜ **FT-3.2** Modules and `use`
- ⬜ **FT-3.3** Multi-file builds with a Makefile
- ⬜ **FT-3.4** Passing procedures as arguments (e.g. a generic integrator)

## 4. Scientific programs
- ⬜ **FT-4.1** Writing data files and plotting them in Python
- ⬜ **FT-4.2** Derived types (e.g. a particle type)
- ⬜ **FT-4.3** Porting an RK4 particle pusher from Python
- ⬜ **FT-4.4** Testing against analytic solutions

## 5. Speed on one core (HPC layer 1)
- ⬜ **FT-5.1** Timing code with `system_clock`
- ⬜ **FT-5.2** Memory hierarchy and caches: the loop-order experiment
- ⬜ **FT-5.3** Compiler optimisation flags
- ⬜ **FT-5.4** Vectorisation (SIMD) basics
- ⬜ **FT-5.5** Arithmetic intensity and the roofline model
- ⬜ **FT-5.6** Calling Fortran from Python with `f2py`

## 6. OpenMP (HPC layer 2)
- ⬜ **FT-6.1** `!$omp parallel do`
- ⬜ **FT-6.2** Private vs shared variables; race conditions
- ⬜ **FT-6.3** Reductions
- ⬜ **FT-6.4** Scheduling and load balance
- ⬜ **FT-6.5** Speedup, Amdahl's law and strong scaling

## 7. MPI (HPC layer 3)
- ⬜ **FT-7.1** Ranks and a first MPI program
- ⬜ **FT-7.2** Point-to-point: send and receive
- ⬜ **FT-7.3** Collectives: broadcast and reduce
- ⬜ **FT-7.4** 1D domain decomposition with halo exchange (heat equation)
- ⬜ **FT-7.5** Strong vs weak scaling
