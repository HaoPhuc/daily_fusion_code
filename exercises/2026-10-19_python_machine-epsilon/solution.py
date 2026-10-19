# time: ?? min
# How small is small? Machine epsilon (NUM-1.1)
# Run:  python3 solution.py
import numpy as np


def machine_epsilon():
    """Halve eps until adding eps/2 to 1.0 no longer changes it.
    Returns eps and the number of halvings."""
    eps = 1.0
    halvings = 0
    while False:                   # TODO 1a: while 1.0 + eps/2 is still bigger than 1.0
        eps = eps                  # TODO 1b: halve eps
        halvings = halvings + 1
    return eps, halvings


def main():
    eps, halvings = machine_epsilon()
    print(f"my eps    = {eps:.6e}   after {halvings} halvings")
    print(f"numpy eps = {np.finfo(float).eps:.6e}")

    N = 1e20                       # ions in about a cubic metre of plasma
    gap = 0.0                      # TODO 2a: estimated gap between N and the next float
    print(f"gap near N ~ {gap:.3e}   (exact gap from numpy: {np.spacing(N):.3e})")
    for added in [1.0, 1000.0, 100000.0]:
        same = False               # TODO 2b: True if N + added is still equal to N
        print(f"N + {added:8.0f} == N ?  {same}")


if __name__ == "__main__":
    main()

# TODO 2c: complete the sentence.
# Machine epsilon is about ___, so adding fewer than about ___ ions to 1e20 ions changes nothing.
