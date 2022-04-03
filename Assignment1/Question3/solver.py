'''
This script provides a solver routine for
the BVP for Question 3 of Assignment 1.
'''

# Python imports
import numpy as np

# Derivative kernel
def kernel(u, r, E, l):
    alpha = 0.471
    sigma = 0.2025
    m = 1.27/2
    u_der = u[1]    # dtheta/dt
    u_dder = 2*m*(-alpha/r + sigma*r + l*(l+1)/(2*m*r*r) - E)*u[0]    # dv/dt
    return np.array([u_der, u_dder])

# Integration routine
def integrator(u, routine, N, r0, rf, nNodes, *args, kernel=kernel):
    h = (rf-r0)/N   # step size

    # initialise theta, v arrays
    u_arr = np.array([u[0]])

    # node counter
    nodes = 0

    # iteration loop
    for i in range(0, N):
        u = routine(r0 + i*h, u, h, kernel, *args)
        u_arr = np.append(u_arr, u[0])

        if (np.sign(u_arr[i+1]) != np.sign(u_arr[i]) and u_arr[i] != 0):
            nodes += 1
            if (nodes > nNodes):
                return [nodes], False

    if (nodes < nNodes):
        return [nodes], False

    return u, True

# Secant method for root finding
def secant(v1, v2, x1, x2, xf):
    return v1 + (xf - x1)*(v1 - v2)/(x1 - x2)

# Main Solver for Schrodinger eqn
def solver(u0, r0, rf, l, E1, E2, N, tol, routine, nNodes):

    u1, flag = integrator(u0, routine, N, r0, rf, nNodes, E1, l)
    while (flag == False):  # handle bad initial guesses
        mult = pow(2, nNodes - u1[0]) if nNodes > u1[0] else pow(1.5, nNodes - u1[0])
        E1 = E1*mult
        u1, flag = integrator(u0, routine, N, r0, rf, nNodes, E1, l)

    u2, flag = integrator(u0, routine, N, r0, rf, nNodes, E2, l)
    while (flag == False):  # handle bad initial guesses
        mult = pow(2, nNodes - u2[0]) if nNodes > u2[0] else pow(1.5, nNodes - u2[0])
        E2 = E2*mult
        u2, flag = integrator(u0, routine, N, r0, rf, nNodes, E2, l)

    # luck check
    if (abs(u1[0] - 0) < tol):
        print(E1)

    # iteration loop
    i=0
    while (i < 100):
        if (abs(u2[0] - 0) < tol):  # exit condition
            return E2
        else:
            # root finder   
            Em = secant(E1, E2, u1[0], u2[0], 0)
            E1 = E2
            E2 = Em
            u1[0] = u2[0]

            # run with updated Energy
            u2, flag = integrator(u0, routine, N, r0, rf, nNodes, E2, l)
            while (flag == False):  # handle bad guess
                mult = pow(2, nNodes - u2[0]) if nNodes > u2[0] else pow(1.5, nNodes - u2[0])
                E2 = E2*mult
                u2, flag = integrator(u0, routine, N, r0, rf, nNodes, E2, l)
            
            # increase iterator
            i += 1
