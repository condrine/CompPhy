'''
This script provides the solution 
for Question 2 of Assignment 1
'''

import sys
from pathlib import Path

# Python imports
from math import pi

# Add the Utils Module
p = Path(__file__).resolve().parents[2]
sys.path.append(str(p))

# Utils module imports
from Utils.int_routines import rk4

# Local imorts
from solver import solver

def rotation_corr(omega, t):
    return omega*t

# Simulation constants
h = 0.00001 # 3.6s
t0 = 0
v0 = 8000 # km/hr
elevation = 135 # degrees (180 - value = west)
omega = 2*pi/24

# case 1
print("\ncase 1")
long = 77 # degrees
lat = 8.5 # degrees

u, i = solver(long, lat, v0, omega, elevation, t0, h, rk4)
print("long = %.2f" % (u[0]*180/pi - rotation_corr(omega*180/pi, i*h)) + "E")
print("lat = %.2f"% ((pi/2 - u[2])*180/pi) + "N")


# case 2
print("\ncase 2")
long = 77 # degrees
lat = 30 # degrees

u, i = solver(long, lat, v0, omega, elevation, t0, h, rk4)
print("long = %.2f" % (u[0]*180/pi - rotation_corr(omega*180/pi, i*h)) + "E")
print("lat = %.2f"% ((pi/2 - u[2])*180/pi) + "N")
