'''
This script provides the solution for 
part (A) of Question 3 of Assignment 1
'''

import sys
import os

# Add the Utils Module
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path.replace("Assignment1/Question3", ""))

# Utils module imports
from Utils.int_routines import rk4

# Local imports
from solver import solver

# Simulation constants
r0 = 20
rf = 0
u0 = [1E-5, 1E-5]
tol = 1E-5
E1 = 0.2
E2 = 0.3
N = 1000

# 1-S meson
E = solver(u0, r0, rf, 0, E1, E2, N, tol, rk4, 0)
print("Mass of 1-S charmonium state is", 2*1.27 + E, "GeV")

# 2-S meson
E = solver(u0, r0, rf, 0, E1, E2, N, tol, rk4, 1)
print("Mass of 2-S charmonium state is", 2*1.27 + E, "GeV")

# 1-P meson
E = solver(u0, r0, rf, 1, E1, E2, N, tol, rk4, 0)
print("Mass of 1-P charmonium state is", 2*1.27 + E, "GeV")