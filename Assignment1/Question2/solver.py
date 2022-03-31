'''
This script provides a solver routine for
the IVP for Question 2 of Assignment 1.
'''

# Python imports
from math import cos, sin, pi
import numpy as np

# define constants
g = 127008 # km/h^2
R = 6371 #km

# Derivative kernel
def kernel(u, t):
    theta_der = u[1]                # dtheta/dt
    r_der = u[3]                    # dr/dt
    theta_dder = -2*u[3]*u[1]/u[2]  # d^2theta/dt^2
    r_dder =  -g + u[2]*u[1]*u[1]   # d^2r/dt^2
    return np.array([theta_der, theta_dder, r_der, r_dder])

# return radius of disc whose plane particle moves in
def R_disc(lat):
    return R*cos(lat*pi/180)

# Solver routine
def solver(theta0, lat, v0, elevation, t0, h, routine, *args, kernel=kernel):
    
    # instantiate evolving vars
    u = [0, 0, 0, 0]

    # initial conditions
    u[0] = theta0*pi/180
    u[1] = v0*cos(elevation*pi/180)/R_disc(lat)
    u[2] = R_disc(lat)
    u[3] = v0*sin(elevation*pi/180)

    # initialise theta, r arrays
    theta_arr = np.array([u[0]])
    theta_d_arr = np.array([u[1]])
    r_arr = np.array([u[2]])
    r_d_arr = np.array([u[3]])

    # iteration loop
    i = 0
    while True:
        u = routine(t0 + i*h, u, h, kernel, *args)

        # break condition
        if (u[2] < R_disc(lat)): break

        # update arrs
        theta_arr = np.append(theta_arr, u[0])
        theta_d_arr = np.append(theta_d_arr, u[1])
        r_arr = np.append(r_arr, u[2])
        r_d_arr = np.append(r_d_arr, u[3])
        i += 1

    return theta_arr, theta_d_arr, r_arr, r_d_arr, i


