# time: ?? min
# Heating a plasma: Euler's method, second try (NUM-4.1, retry)
# Run:  python3 solution.py
import numpy as np

P = 10.0    # heating power, MW
TAU = 2.0   # energy confinement time, s   (W comes out in MJ)


def exact_energy(t):
    """Exact solution of dW/dt = P - W/TAU with W(0) = 0. Given: don't change."""
    return P * TAU * (1 - np.exp(-t / TAU))


def euler_energy(dt, t_end):
    """Integrate dW/dt = P - W/TAU from W(0) = 0 to t_end with explicit Euler.
    Returns the arrays t and W (n + 1 points: start and end included)."""
    n = 0                              # TODO 1a: number of steps (a whole number!)
    t = np.linspace(0, t_end, n + 1)   # n steps need n + 1 points
    W = np.zeros(n + 1)                # W[0] = 0 is the initial condition
    for k in range(n):                 # n steps: k = 0, 1, ..., n - 1
        W[k + 1] = 0.0                 # TODO 1b: one Euler step from W[k]
    return t, W


def main():
    t_end = 4.0
    prev_err = None
    for dt in [1.0, 0.5, 0.25, 0.125]:
        t, W = euler_energy(dt, t_end)
        err = 0.0                      # TODO 2a: absolute error at t_end
        if prev_err is None:
            print(f"dt = {dt:5.3f} s   error = {err:.4f} MJ")
        else:
            ratio = 0.0                # TODO 2b: previous error / this error
            print(f"dt = {dt:5.3f} s   error = {err:.4f} MJ   ratio = {ratio:.3f}")
        prev_err = err


if __name__ == "__main__":
    main()

# TODO 3: complete the sentence.
# Halving dt divides the error by about ___, so Euler's method is of order ___.
