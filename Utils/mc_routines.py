# Script Containing Monte-Carlo Methods

# Python imports
import numpy as np

# Initialise RNG
rng = np.random.default_rng()

# Acceptance-Rejection sampling method
def AcptRejSample(range, height, dist):

    # create new sample point
    x = rng.uniform(low=range[0], high=range[1])

    # Accept/Reject the sample point
    while (dist(x) < rng.uniform()*height):
        x = rng.uniform(low=range[0], high=range[1])

    return x


# Metropolis Algorithm
def metropolis(theta_i, proposal, target, ndim):
    theta = theta_i
    while (all(theta==theta_i)):
        temp = proposal(theta_i)
        theta = temp if all(target(temp)/target(theta_i) > rng.uniform(size = ndim)) else theta_i
    return theta
