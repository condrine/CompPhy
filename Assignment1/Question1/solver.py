'''
This script provides a solver routine for
the IVP for Question 1 of Assignment 1.
'''

# Python imports
from math import cos, sin
import numpy as np


# Derivative kernel
def kernel(u, t, alpha=0, A=0, omega=0):
    theta_der = u[1]    # dtheta/dt
    v_der = -sin(u[0]) - alpha*u[1] + A*cos(omega*t)    # dv/dt
    return np.array([theta_der, v_der])

# Solver routine
def solver(u, routine, N, t0, tf, *args, kernel=kernel):
    h = (tf-t0)/N   # step size

    # initialise theta, v arrays
    theta_arr = np.array([u[0]])
    v_arr = np.array([u[1]])

    # iteration loop
    for i in range(0, N):
        u = routine(t0 + i*h, u, h, kernel, *args)
        theta_arr = np.append(theta_arr, u[0])
        v_arr = np.append(v_arr, u[1])
    
    return theta_arr, v_arr

    


