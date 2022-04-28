'''
This script provides a solver routine for
the BVP for Question 1 of Assignment 2.
'''

# Python imports
from math import cos, sin, sqrt
import numpy as np

# constants
D = 3
m = 450
g = 9.8

# define the equation
def kernel(u, t):
    x_der = u[1]
    vx_der = -(D/m)*u[1]*sqrt(u[1]*u[1] + u[3]*u[3])
    y_der = u[3]
    vy_der = -g -(D/m)*u[3]*sqrt(u[1]*u[1] + u[3]*u[3])        
    return np.array([x_der, vx_der, y_der, vy_der])

# Integration routine
def integrator(u, t0, xf, h, routine, *args, kernel=kernel):

    # initialise theta, r arrays
    x_arr = np.array([u[0]])
    y_arr = np.array([u[2]])

    # iteration loop
    i = 0
    while True:
        u = routine(t0 + i*h, u, h, kernel, *args)

        # break condition
        if (u[0] > xf): break

        # update arrs
        x_arr = np.append(x_arr, u[0])
        y_arr = np.append(y_arr, u[2])
        i += 1

    return y_arr[-1]

# Secant method for root finding
def secant(v1, v2, x1, x2, xf):
    return v1 + (xf - x1)*(v1 - v2)/(x1 - x2)

# Main Solver for BVP
def solver(v0, theta1, theta2, xf, yf, h, tol, routine):
    
    # run on initial guesses
    u1 = [0, v0*cos(theta1), 0, v0*sin(theta1)]
    yf1 = integrator(u1, 0, xf, h, routine)

    u2 = [0, v0*cos(theta2), 0, v0*sin(theta2)]
    yf2 = integrator(u2, 0, xf, h, routine)

    # luck check
    if (abs(yf1 - yf) < tol):
        return theta1

    # iteration loop
    i=0
    while (i < 100):
        if (abs(yf2 - yf) < tol):  # exit condition
            return theta2
        else:
            # root finder   
            thetam = secant(theta1, theta2, yf1, yf2, yf)
            theta1 = theta2
            theta2 = thetam
            yf1 = yf2

            # run with updated theta
            u2 = [0, v0*cos(theta2), 0, v0*sin(theta2)]
            yf2 = integrator(u2, 0, xf, h, routine)

            # increase iterator
            i += 1


    



