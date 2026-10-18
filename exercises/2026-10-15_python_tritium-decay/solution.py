import numpy as np


def decay_rate(half_life):
    """Return the decay constant lambda for a given half-life."""
    return np.log(2) / half_life


def euler_decay(N0, lam, dt, t_end):
    """Integrate dN/dt = -lam * N with explicit Euler. Return arrays t, N."""
    t = np.linspace(0, t_end, t_end/dt, endpoint = True)
    N = np.zeros(len(t))
    N[0] = N0
    for k in range(len(t)):
        N[k+1] = N[k] - lam*N[k]*dt
    return t, N


def exact_decay(N0, lam, t):
    """Return the analytic solution N(t)."""
    N = N0 * np.exp(-lam*t)
    return N


def main():
    # given constants
    N0 = 1 * np.exp(6)
    half_life = 12.32
    t_end = 50
    dt_all = np.array([5, 2.5, 1.25, 0.625])
    
    # lambda
    lam = decay_rate(half_life)

    # N_exact
    N_exact = exact_decay(N0, lam, t_end)

    # Calculate N_euler for every dt
    N_euler = np.zeros(len(dt_all))
    relative_err = np.zeros(len(dt_all))
    ratio = np.zeros(len(dt_all))
    k = -1
    for dt in dt_all:
        print("dt: ", dt)
        k += 1
        N_euler[k] = euler_decay(N0, lam, dt, t_end)[1][-1]
        #relative error
        relative_err[k] = np.abs(N_euler - N_exact) / N_exact
        print("The relative error at t_end: ", relative_err[k])
        #ratio
        if k == 0:
            continue
        else:
            ratio[k] = relative_err[k-1] / relative_err[k]
            print("The ratio of the previous error to this one: ", ratio[k])


if __name__ == "__main__":
    main()

# What the ratio column tells me:
## This is a bit too hard for me at the moment. It took more than an hour, but it was really fun, I just can't find enough time now.