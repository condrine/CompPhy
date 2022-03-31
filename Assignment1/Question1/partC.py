'''
This script provides the solution for 
part (C) of Question 1 of Assignment 1
'''

import sys
import os

# Add the Utils Module
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path.replace("Assignment1/Question1", ""))

# Python imports
import numpy as np

# Utils module imports
from Utils.int_routines import rk4
from Utils.colors import blue
from Utils.plt_creator import plt_creator

# Solver
from solver import solver

# Simutaion constants
N = 10000
t0 = 0
tf = 100

# Initial Conditions
u1 = [1.1,-0.1]
u2 = [1.09, -0.1]

# A = 0.5, alpha = 0.5
theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, 0.5, 0.5, 1.)
theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, 0.5, 0.5, 1.)

plt1 = plt_creator(
    title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
    xLabel=r't',
    yLabel=r'$\Delta\theta$', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
plt1.savefig("Results/partC1_Dtht.png")


# A = 0.9, alpha = 0.5
theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, 0.5, 0.9, 1.)
theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, 0.5, 0.9, 1.)

plt1 = plt_creator(
    title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
    xLabel=r't',
    yLabel=r'$\Delta\theta$', 
    xMargin=0.02, 
    yMargin=0.02
)

plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
plt1.savefig("Results/partC2_Dtht.png")


# A = 1.07, alpha = 0.5
theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, 0.5, 1.07, 1.)
theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, 0.5, 1.07, 1.)

plt1 = plt_creator(
    title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
    xLabel=r't',
    yLabel=r'$\Delta\theta$', 
    xMargin=0.02, 
    yMargin=0.02
)

plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
plt1.savefig("Results/partC3_Dtht.png")


# A = 1.1, alpha = 0.5
theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, 0.5, 1.1, 1.)
theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, 0.5, 1.1, 1.)

plt1 = plt_creator(
    title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
    xLabel=r't',
    yLabel=r'$\Delta\theta$', 
    xMargin=0.02, 
    yMargin=0.02
)

plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
plt1.savefig("Results/partC4_Dtht.png")
