'''
This script provides the solution
for Question 6 of Assignment 3
'''

import sys
from pathlib import Path

# Python imports
import numpy as np
from math import pi, sqrt

# Add the Utils Module
p = Path(__file__).parents[2]
sys.path.append(str(p))

# Utils module imports
from Utils.colors import red
from Utils.plt_creator import plt_creator


# Distribution
def dist(x):
    return sqrt(2/pi)*np.exp(-0.5*x**2)

# Initialise RNG
rng = np.random.default_rng()

# Rejection sampling
def getNextSample(range, dist=dist):
    x = rng.uniform(low=range[0], high=range[1])
    while (dist(x) < rng.uniform()):
        x = rng.uniform(low=range[0], high=range[1])
    return x

# Get samples
N_samples = 10000
Range = (0,4)
Samples = [getNextSample(Range) for i in range(N_samples)]

# Initialise plot
plt = plt_creator(
    title="Sampling from Rejection Method", 
    xLabel="x", 
    yLabel="Prob. Density",
    xMargin=0.02, 
    yMargin=0.02
)

# Plot params
npoints = 30
x_space = np.linspace(Range[0], Range[1], npoints)

# Histogram
plt.hist(Samples, density=True, range=Range, bins=npoints)

# Dist pdf
plt.plot(
    x_space, 
    dist(x_space), 
    color = red, 
    linestyle = '--', 
    linewidth=2
)

plt.savefig("Results/Rejct.png")

