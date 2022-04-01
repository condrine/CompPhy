'''
This script provides the solution for 
part (A) of Question 2 of Assignment 1
'''

import sys
import os

# Add the Utils Module
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path.replace("Assignment1/Question2", ""))

# Utils module imports
from Utils.int_routines import rk4
from Utils.colors import blue
from Utils.plt_creator import plt_creator

# Local imorts
from solver import solver

def rotation_corr(omega, t):
    return omega*t

# Simulation constants
h = 0.01 # 3.6s
t0 = 0

# first part
theta0 = 77 # degrees
lat = 30 # degrees
elevation = 135 # degrees (45 west)
v0 = 8000 # km/hr

theta_arr, theta_d_arr, r_arr, r_d_arr, i = solver(theta0, lat, v0, elevation, t0, h, rk4)
print(theta_arr[-1]*180/3.14 + rotation_corr(360/24, i*h))
print(i)

