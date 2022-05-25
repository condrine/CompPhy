'''
This script provides the solution
for Question 1 of Assignment 3
'''

import sys
import time
from pathlib import Path

# Python imports
import numpy as np

# Add the Utils Module
p = Path(__file__).resolve().parents[2]
sys.path.append(str(p))

# Utils module imports
from Utils.colors import red
from Utils.plt_creator import plt_creator


# Get next sample from Linear Congruential Generator
def getNextLCG(X, m, a, c):
    return (X*a + c)%m

# Fixed params (Numerical Recipies, Press et. al.)
m = pow(2,32)
a = 1664525
c = 1013904223

# Float Params
Xi = 294941317 # Seed

# Initialise time
start_time = time.time()

# Get samples
N_samples = 10000
Samples = [Xi]
for i in range(N_samples-1):
    Samples.append(getNextLCG(Samples[-1], m, a, c))

# Normalise Sample to desired range
Samples = Samples/np.ptp(Samples)

# Stop timer
end_time = time.time()

# Initialise plot
plt = plt_creator(
    title="Random Sampling from LCG", 
    xLabel="x", 
    yLabel="Prob. Density",
    xMargin=0.02, 
    yMargin=0.02
)

# Plot params
npoints = 30

# Histogram
plt.hist(Samples, density=True, bins=npoints)

# Uniform pdf
plt.plot(
    [0., 1.], 
    [1., 1.], 
    color = red, 
    linestyle = '--', 
    linewidth=2
)

plt.savefig("Results/LCG.png")

print("Time taken to generate %s random uniform deviates is %2f ms"%(N_samples, (end_time-start_time)*1000))