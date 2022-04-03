'''
This script provides a solver routine for
the IVP for Question 2 of Assignment 1.
'''

# Python imports
from math import cos, sin, pi
import numpy as np

# define constants
g = 127094.18 # km/h^2
R = 6371 #km

# Derivative kernel
def kernel(u, t):
    phi_der = u[1]      # dphi/dt
    theta_der = u[3]    # dtheta/dt
    r_der = u[5]        # dr/dt
    phi_dder = -2*u[5]*u[3]/u[4] - 2*u[3]*u[1]*cos(u[2])/sin(u[2])                      # d^2phi/dt^2
    theta_dder = sin(u[2])*cos(u[2])*u[1]*u[1] - 2*u[5]*u[3]/u[4]                       # d^2theta/dt^2
    r_dder =  -g*R*R/(u[4]*u[4]) + u[4]*u[3]*u[3] + u[4]*sin(u[2])*sin(u[2])*u[1]*u[1]  # d^2r/dt^2
    return np.array([phi_der, phi_dder, theta_der, theta_dder, r_der, r_dder])

# return radius of disc of the meridional plane
def R_disc(lat):
    return R*cos(lat*pi/180)

# Solver routine
def solver(phi0, lat, v0, omega, elevation, t0, h, routine, *args, kernel=kernel):
    
    # instantiate evolving vars
    u = [0, 0, 0, 0, 0, 0]

    # initial conditions
    u[0] = phi0*pi/180
    u[1] = v0*cos(elevation*pi/180)/R_disc(lat) + omega
    u[2] = pi/2 - lat*pi/180
    u[3] = 0
    u[4] = R
    u[5] = v0*sin(elevation*pi/180)

    # initialise theta, r arrays
    phi_arr = np.array([u[0]])
    phi_d_arr = np.array([u[1]])
    theta_arr = np.array([u[2]])
    theta_d_arr = np.array([u[3]])
    r_arr = np.array([u[4]])
    r_d_arr = np.array([u[5]])

    # iteration loop
    i = 0
    while True:
        u = routine(t0 + i*h, u, h, kernel, *args)

        # break condition
        if (u[4] < R): break

        # update arrs
        phi_arr = np.append(phi_arr, u[0])
        phi_d_arr = np.append(phi_d_arr, u[1])
        theta_arr = np.append(theta_arr, u[2])
        theta_d_arr = np.append(theta_d_arr, u[3])
        r_arr = np.append(r_arr, u[4])
        r_d_arr = np.append(r_d_arr, u[5])
        i += 1

    return [phi_arr[-1], phi_d_arr[-1], theta_arr[-1], theta_d_arr[-1], r_arr[-1], r_d_arr[-1]], i


