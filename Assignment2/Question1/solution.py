'''
This script provides the solution 
for Question 1 of Assignment 2
'''

import sys
from pathlib import Path

# Python imports
import numpy as np
from math import sqrt, pi

# Add the Utils Module
p = Path(__file__).resolve().parents[2]
sys.path.append(str(p))

# Utils module imports
from Utils.int_routines import rk4
from Utils.colors import blue
from Utils.plt_creator import plt_creator

# Local imorts
from solver import solver


# Initial Parameters for Code
xf = sqrt(22**2 + 3.36**2)
yf = 2.14
theta1 = 30*pi/180
theta2 = 45*pi/180
h = 1e-3
tol = 1e-5

# Part A
v0 = 70*1000/3600   # initial velocity in m/s
theta = solver(v0, theta1, theta2, xf, yf, h, tol, rk4)
print("Launching angle for part A is (in degrees) :", theta*180/pi)

# Part B
N = 50  # Number of velocity points
V = np.linspace(70, 85, N)*1000/3600
Sol = np.vectorize(solver)
Theta = Sol(V, theta1, theta2, xf, yf, h, tol, rk4)*180/pi

# plot
plt1 = plt_creator(
    title="Launching Angle vs v", 
    xLabel="v (km/hr)", 
    yLabel=r'$\theta (\degree s)$', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(V*3600/1000, Theta, linewidth=1, color= blue)
plt1.savefig("Results/theta_vs_v.png")

