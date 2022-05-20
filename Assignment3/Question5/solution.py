'''
This script provides the solution
for Question 5 of Assignment 3
'''

import sys
from pathlib import Path
from turtle import color

# Python imports
import numpy as np
from math import pi
from scipy.stats import norm

# Add the Utils Module
p = Path(__file__).parents[2]
sys.path.append(str(p))

# Utils module imports
from Utils.colors import red
from Utils.plt_creator import plt_creator


# Initialise RNG
rng = np.random.default_rng()

# Gaussian (Box-Muller)
def Gaussian(mu, sigma, N):
    R1 = rng.uniform(size = int(N/2)+1)
    R2 = rng.uniform(size = int(N/2)+1)

    z1 = np.sqrt(-2*np.log(R1))*np.cos(2*pi*R2)*sigma + mu
    z2 = np.sqrt(-2*np.log(R2))*np.sin(2*pi*R1)*sigma + mu

    return np.concatenate((z1, z2))[:N]

# Get samples
Samples = Gaussian(0, 1, 10000)

# Initialise plot
plt = plt_creator(
    title="Gaussian (Box-Muller)", 
    xLabel="x", 
    yLabel="Prob. Density",
    xMargin=0.02, 
    yMargin=0.02
)

# Plot params
Range = (-3,3)
npoints = 30
x_space = np.linspace(Range[0], Range[1], npoints)

# Histogram
plt.hist(Samples, density=True, range=Range, bins=npoints)

# Gaussian pdf
plt.plot(
    x_space, 
    norm.pdf(x_space), 
    color=red, 
    linestyle = '--', 
    linewidth=2
)

plt.savefig("Results/BM.png")
