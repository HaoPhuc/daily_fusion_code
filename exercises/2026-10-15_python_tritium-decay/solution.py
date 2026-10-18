import numpy as np


def decay_rate(half_life):
    """Return the decay constant lambda for a given half-life."""
    raise NotImplementedError


def euler_decay(N0, lam, dt, t_end):
    """Integrate dN/dt = -lam * N with explicit Euler. Return arrays t, N."""
    raise NotImplementedError


def exact_decay(N0, lam, t):
    """Return the analytic solution N(t)."""
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()

# What the ratio column tells me:
