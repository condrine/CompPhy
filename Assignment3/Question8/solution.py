'''
This script provides the solution
for Question 8 of Assignment 3
'''

# Python imports
import numpy as np

# Initialise RNG
rng = np.random.default_rng()

# Get volume from MC integration
def getVol(ndim, npoints):
    accepted = 0

    for i in range(npoints):
        rnd = rng.uniform(size=ndim)
        accepted += 1*(np.sum(rnd*rnd) < 1)
    
    return pow(2, ndim)*accepted/npoints

# Results
npoints = 100000
print("Area of cicle of unit radius is %2f"%getVol(2, npoints))
print("Volume of 10-D sphere of unit radius is %2f"%getVol(10, npoints))