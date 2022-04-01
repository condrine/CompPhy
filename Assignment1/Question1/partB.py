'''
This script provides the solution for 
part (B) of Question 1 of Assignment 1
'''

import sys
import os

# Add the Utils Module
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path.replace("Assignment1/Question1", ""))

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
u = [1.1, -0.1]


# A = 0.5, alpha = 0.1
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.1, 0.5, 1.)
plt1 = plt_creator(
    title="Damped Driven Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partB1_PHSP.png")


# A = 0.9, alpha = 0.1
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.1, 0.9, 1.)
plt1 = plt_creator(
    title="Damped Driven Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partB2_PHSP.png")


# A = 1.07, alpha = 0.1
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.1, 1.07, 1.)
plt1 = plt_creator(
    title="Damped Driven Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partB3_PHSP.png")


# A = 1.1, alpha = 0.1
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.1, 1.1, 1.)
plt1 = plt_creator(
    title="Damped Driven Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partB4_PHSP.png")