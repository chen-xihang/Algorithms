def monte_carlo_pi(run):
    import numpy as np

    x = np.random.uniform(0, 1, run)
    y = np.random.uniform(0, 1, run)

    dist = x**2+y**2
    denom = sum(dist<1)

    ans = denom/run * 4

    return float(ans)

monte_carlo_pi(100)
monte_carlo_pi(1000)

def monte_carlo_pi_antithetic(run):
    import numpy as np

    x = np.random.uniform(0, 1, run)
    y = np.random.uniform(0, 1, run)
    x = np.concatenate((x, 1-x))
    y = np.concatenate((y, 1-y))

    dist = x**2+y**2
    denom = sum(dist<1)

    ans = denom/run * 2

    return float(ans)

monte_carlo_pi_antithetic(100)
monte_carlo_pi_antithetic(1000)