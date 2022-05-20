'''
This script provides the solution
for Question 2 of Assignment 3
'''

import sys
import time
from pathlib import Path

# Python imports
import numpy as np

# Add the Utils Module
p = Path(__file__).parents[2]
sys.path.append(str(p))

# Utils module imports
from Utils.colors import red
from Utils.plt_creator import plt_creator

# Initialise time
start_time = time.time()

# Get samples
N_samples = 10000
Samples = np.random.rand(N_samples)

# Stop timer
end_time = time.time()

# Initialise plot
plt = plt_creator(
    title="Random Numbers from package", 
    xLabel="x", 
    yLabel="Prob. Density",
    xMargin=0.02, 
    yMargin=0.02
)

# Plot params
npoints = 30

# Histogram
plt.hist(Samples, density=True, bins = npoints)

# Uniform pdf
plt.plot(
    [0., 1.], 
    [1., 1.], 
    color = red, 
    linestyle = '--', 
    linewidth=2
)

plt.savefig("Results/np_RNG.png")

print("Time taken to generate %s random uniform deviates is %2f ms"%(N_samples, (end_time-start_time)*1000))