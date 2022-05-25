'''
This script provides the solution
for Question 9 of Assignment 3
'''

import sys
from pathlib import Path

# Python imports
import numpy as np

# Add the Utils Module
p = Path(__file__).parents[2]
sys.path.append(str(p))

# Utils module imports
from Utils.mc_routines import metropolis, rng
from Utils.colors import red
from Utils.plt_creator import plt_creator

# proposal pdf (walker)
def proposal(theta):
    theta_p = rng.normal(loc = theta, scale=0.2)
    return theta_p

# target distribution
def target(theta):
    pdf = 0.25*((theta > 3) & (theta < 7))
    return pdf

# params
ndim = 1
npoints = 100000
theta_i = np.ones(ndim)*3.1

# sample list
sample = [theta_i]

# sampler
for i in range(npoints):
    sample.append(metropolis(sample[-1], proposal, target, ndim))
sample = sample[1:]

# Initialise plot
plt = plt_creator(
    title="Uniform (Metropolis)", 
    xLabel="x", 
    yLabel="Prob. Density",
    xMargin=0.02, 
    yMargin=0.02
)

# Plot params
Range = (1, 9)
nbins = 40
x_space = np.linspace(Range[0], Range[1], nbins)

# Histogram
plt.hist([A[0] for A in sample], density=True, range=Range, bins=nbins)

# Uniform pdf
plt.plot(
    x_space, 
    target(x_space), 
    color=red, 
    linestyle = '--', 
    linewidth=2
)

plt.savefig("Results/Metropolis.png")
