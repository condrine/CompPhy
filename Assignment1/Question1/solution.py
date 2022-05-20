'''
This script provides the solution 
for Question 1 of Assignment 1
'''

import sys
from pathlib import Path

# Python imports
import numpy as np

# Add the Utils Module
p = Path(__file__).parents[2]
sys.path.append(str(p))

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
alpha = 0.5
omega = 2/3

# Part A
# A = 0
u = [1.1, -0.1]
A = 0
theta_arr, v_arr = solver(u, rk4, N, t0, tf, alpha, A, omega)
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
A_arr = [0.5, 0.9, 1.07, 1.1]

for i in range(4):
    theta_arr, v_arr = solver(u, rk4, N, t0, tf, alpha, A_arr[i], omega)
    plt1 = plt_creator(
        title="Damped Driven Pendulum PHSP", 
        xLabel=r'$\theta$', 
        yLabel=r'v($\theta$)', 
        xMargin=0.02, 
        yMargin=0.02
    )
    plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
    plt1.savefig("Results/partB%d_PHSP.png"%(i+1))


# Part C
u1 = [1.1,-0.1]
u2 = [1.09, -0.1]

for i in range(4):
    theta_arr_1, v_arr_1 = solver(u1, rk4, N, t0, tf, alpha, A_arr[i], omega)
    theta_arr_2, v_arr_2 = solver(u2, rk4, N, t0, tf, alpha, A_arr[i], omega)

    plt1 = plt_creator(
        title=r'Damped Driven Pendulum $\Delta\theta$ vs t', 
        xLabel=r't',
        yLabel=r'$\Delta\theta$', 
        xMargin=0.02, 
        yMargin=0.02
    )
    plt1.plot(np.linspace(t0, tf, N+1), theta_arr_1-theta_arr_2, linewidth=1, color= blue)
    plt1.savefig("Results/partC%d_Dtht.png" %(i+1))