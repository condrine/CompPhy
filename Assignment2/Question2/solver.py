'''
This script provides the solution 
for Question 2 of Assignment 2
'''

# Python imports
from scipy.sparse import coo_matrix, linalg
import numpy as np
from scipy.linalg import eigh_tridiagonal as eigtr

# Potential term for Shrodinger Eqn.
def V(x, k, lmbda):
    return 0.5*k*x**2 + (1/24)*lmbda*x**4

# Solver routine 
def solver(xi, xf, N, isPeriodic, Nvalues, *args):
    h = (xf - xi)/N
    X = np.linspace(xi, xf, N, endpoint=False)

    # calculate diagonal (i,i) elements
    diag = 2/(h*h) + 2*V(X, *args)
    diag_row = np.arange(0, N)
    diag_col = diag_row.copy()

    # calculate subdiagonal (i, i+1) elements
    subdiag_1 = np.full(N-1, -1/(h*h))
    subdiag_1_row = np.arange(0, N-1)
    subdiag_1_col = subdiag_1_row.copy() + 1

    # calculate subdiagonal (i+1, i) elements
    subdiag_2 = subdiag_1.copy()
    subdiag_2_row = np.arange(1, N)
    subdiag_2_col = subdiag_2_row.copy() - 1

    # concatenate all the arrays to form the sparse matrix
    row = np.concatenate((diag_row, subdiag_1_row, subdiag_2_row))
    col = np.concatenate((diag_col, subdiag_1_col, subdiag_2_col))
    val = np.concatenate((diag, subdiag_1, subdiag_2))

    # add off diagonal elements if needed
    if (isPeriodic):
        row = np.append(row, [0, N-1])
        col = np.append(col, [N-1, 0])
        val = np.append(val, [-1/(h*h), -1/(h*h)])

    # calculate eigenvalues
    eigs = linalg.eigsh(
        coo_matrix((val, (row, col)), shape=(N, N)).toarray(),  # sparse matrix
        which='SA', 
        k=Nvalues, 
        return_eigenvectors=False
    )
    
    return eigs/2



