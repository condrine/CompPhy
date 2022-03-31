'''
This script provides the solution for 
part (A) of Question 1 of Assignment 1
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

# Local imorts
from solver import solver
from txtbox import txtbox

# Simutaion constants
N = 10000
t0 = 0
tf = 100
u = [1.1, -0.1]

# Utility function for textbox


# A = 0, alpha = 0
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0., 0., 0.)
plt1 = plt_creator(
    title="Ideal Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1 = txtbox(plt1, 0., 0., 0.)
plt1.savefig("Results/partA1_PHSP.png")

# A = 0, alpha = 0.1
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.1, 0., 0.)
plt1 = plt_creator(
    title="Damped Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1 = txtbox(plt1, 0.1, 0., 0.)
plt1.savefig("Results/partA2_PHSP.png")

# A = 0, alpha = 0.5
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 0.5, 0., 0.)
plt1 = plt_creator(
    title="Damped Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1 = txtbox(plt1, 0.5, 0., 0.)
plt1.savefig("Results/partA3_PHSP.png")

# A = 0, alpha = 1
theta_arr, v_arr = solver(u, rk4, N, t0, tf, 1., 0., 0.)
plt1 = plt_creator(
    title="Damped Pendulum PHSP", 
    xLabel=r'$\theta$', 
    yLabel=r'v($\theta$)', 
    xMargin=0.02, 
    yMargin=0.02
)
plt1.plot(theta_arr, v_arr, linewidth=1, color= blue)
plt1 = txtbox(plt1, 1., 0., 0.)
plt1.savefig("Results/partA4_PHSP.png")