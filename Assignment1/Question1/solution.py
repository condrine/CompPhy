'''
This script provides the solution for 
part (A) of Question 1 of Assignment 1
'''

import sys
import os

# Python imports
import numpy as np

# Add the Utils Module
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path.replace("Assignment1/Question1", ""))

# Utils module imports
from Utils.int_routines import rk4
from Utils.colors import blue
from Utils.plt_creator import plt_creator

# Local imorts
from solver import solver

# Simutaion constants
N = 10000
t0 = 0
tf = 100

# Part A
# alpha = 0.5, A = 0, omega = 2/3
u = [1.1, -0.1]
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.5, 0., 2/3)
plt1 = plt_creator(
    title="Damped Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partA_PHSP.png")

# Part B
u = [1.1, -0.1]

# alpha = 0.5, A = 0.5, omega = 2/3
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.5, 0.5, 2/3)
plt1 = plt_creator(
    title="Damped Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partB1_PHSP.png")


# alpha = 0.5, A = 0.9, omega = 2/3
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.5, 0.9, 2/3)
plt1 = plt_creator(
    title="Damped Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partB2_PHSP.png")


# alpha = 0.5, A = 1.07, omega = 2/3
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.5, 1.07, 2/3)
plt1 = plt_creator(
    title="Damped Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partB3_PHSP.png")

# alpha = 0.5, A = 1.1, omega = 2/3
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.5, 1.1, 2/3)
plt1 = plt_creator(
    title="Damped Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1.savefig("Results/partB4_PHSP.png")


# Part C
u1 = [1.1,-0.1]
u2 = [1.09, -0.1]

# alpha = 0.5, A = 0.5, omega = 2/3
theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, 0.5, 0.5, 2/3)
theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, 0.5, 0.5, 2/3)

plt1 = plt_creator(
    title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
    xLabel=r't',
    yLabel=r'$\Delta\theta$', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
plt1.savefig("Results/partC1_Dtht.png")


# alpha = 0.5, A = 0.9, omega = 2/3
theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, 0.5, 0.9, 2/3)
theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, 0.5, 0.9, 2/3)

plt1 = plt_creator(
    title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
    xLabel=r't',
    yLabel=r'$\Delta\theta$', 
    xMargin=0.02, 
    yMargin=0.02
)

plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
plt1.savefig("Results/partC2_Dtht.png")


# alpha = 0.5, A = 1.07, omega = 2/3
theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, 0.5, 1.07, 2/3)
theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, 0.5, 1.07, 2/3)

plt1 = plt_creator(
    title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
    xLabel=r't',
    yLabel=r'$\Delta\theta$', 
    xMargin=0.02, 
    yMargin=0.02
)

plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
plt1.savefig("Results/partC3_Dtht.png")


# alpha = 0.5, A = 1.1, omega = 2/3
theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, 0.5, 1.1, 2/3)
theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, 0.5, 1.1, 2/3)

plt1 = plt_creator(
    title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
    xLabel=r't',
    yLabel=r'$\Delta\theta$', 
    xMargin=0.02, 
    yMargin=0.02
)

plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
plt1.savefig("Results/partC4_Dtht.png")