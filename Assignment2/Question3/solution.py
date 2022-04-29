'''
This script provides the solution
for Question 3 of Assignment 2
'''

from math import sqrt
import sys
import os

# Python imports
import numpy as np
from scipy.linalg import eigh

# Add the Utils Module
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path.replace("Assignment2/Question3", ""))

# Utils module imports
from Utils.colors import blue, red
from Utils.plt_creator import plt_creator

# First Method to get Mean and Variance (double loop, low round off)
def get_mean_var1(Ct_arr):

    # Calculate Average
    Ct_avg = sum([Ct for Ct in Ct_arr])
    Ct_avg = Ct_avg/len(Ct_arr)

    # Calculate Var
    Ct_var = sum([(Ct - Ct_avg)**2 for Ct in Ct_arr])
    Ct_var = Ct_var/len(Ct_arr)

    return Ct_avg, Ct_var

# Second Method to get Mean and Variance (single loop, large round off)
def get_mean_var2(Ct_arr):

    Ct_sum = 0
    Ct_sqr_sum = 0
    for Ct in Ct_arr:
        Ct_sum += Ct
        Ct_sqr_sum += Ct*Ct

    Ct_avg = Ct_sum/len(Ct_arr)
    Ct_var = Ct_sqr_sum/len(Ct_arr) - Ct_avg**2

    return Ct_avg, Ct_var

# Third Method to get Mean and Variance (single loop, low round off)
def get_mean_var3(Ct_arr):
    M = 0
    S = 0
    Ct_sum = 0
    for i in range(len(Ct_arr)):
        S = S + (Ct_arr[i] - M)*(Ct_arr[i] - (M + (Ct_arr[i] - M)/(i+1)))
        M = M + (Ct_arr[i] - M)/(i+1)
        Ct_sum += Ct_arr[i]
    
    Ct_avg = Ct_sum/len(Ct_arr)
    Ct_var = S/(len(Ct_arr))

    return Ct_avg, Ct_var
    
# Get Covariance for (t1, t2)
def get_cov(Ct1_arr, Ct2_arr):

    # calculate average
    Ct1_avg = sum([Ct for Ct in Ct1_arr])/len(Ct1_arr)
    Ct2_avg = sum([Ct for Ct in Ct2_arr])/len(Ct2_arr)

    # calculate covariance
    cov = sum([(Ct1_arr[i] - Ct1_avg)*(Ct2_arr[i] - Ct2_avg) for i in range(len(Ct2_arr))])/len(Ct2_arr)
    return cov

# initialise data dictionary
data_dict = {}

# read file and store data
file = "corr.dat"
with open(file) as f:
    line = f.readline()
    while line:
        t, Ct = line.split()
        # create a new entry for a new t
        if int(t) not in data_dict:
            data_dict[int(t)] = []
        # add values of Ct to dict
        data_dict[int(t)].append(float(Ct))
        line = f.readline()

# Part A
Ct_avg_arr = []
Ct_err_arr = []
t_arr = []
for t in data_dict:
    Ct_arr = data_dict[t]
    Ct_avg, Ct_var = get_mean_var3(Ct_arr)
    Ct_err = sqrt(Ct_var/(len(Ct_arr) - 1))

    Ct_avg_arr.append(Ct_avg)
    Ct_err_arr.append(Ct_err)
    t_arr.append(t)

plt = plt_creator(
    title=r'$\overline{C_m}$ vs t', 
    xLabel="t", 
    yLabel=r'$\overline{C_m}(t)$',
    xMargin=0.02, 
    yMargin=0.02
)
plt.errorbar(t_arr, Ct_avg_arr, yerr=Ct_err, ecolor='red')
plt.savefig("Results/Cbarvst.png")   

# Part B
mat = [[get_cov(data_dict[t1], data_dict[t2]) for t2 in range(33,63)] for t1 in range(33,63)]
eigs = eigh(mat, eigvals_only=True)
print("Eigenvalues of the required covariance matrix are: ", eigs)