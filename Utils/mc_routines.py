# Script Containing Monte-Carlo Methods

# Python imports
from math import sqrt
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
    prop_arr = []
    while (all(theta==theta_i)):
        temp = proposal(theta_i)
        theta = temp if all(target(temp)/target(theta_i) > rng.uniform(size = ndim)) else theta_i
        prop_arr.append(temp)
    return theta, prop_arr


# Negative Log Likelihood
def log_likelihod(theta, objective, data):
    x, y, y_err = data
    nll_c = np.log(np.sqrt(2*np.pi)*y_err)
    nll = (y-objective(theta, x))*(y-objective(theta, x))/(2*y_err*y_err)
    return -np.sum(nll_c + nll)

# Log Probability
def log_probability(log_likelihood, log_prior):
    return (log_prior + log_likelihood if (np.isfinite(log_prior)) else -np.inf)

 
