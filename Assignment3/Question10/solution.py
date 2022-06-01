'''
This script provides the solution
for Question 10 of Assignment 3
'''

from cProfile import label
import sys
from pathlib import Path
from turtle import color

# Python imports
import numpy as np
import pandas as pd
from scipy.optimize import minimize
import emcee as mc
import corner

# Add the Utils Module
p = Path(__file__).resolve().parents[2]
sys.path.append(str(p))

# Utils module imports
from Utils.plt_creator import plt_creator
from Utils.mc_routines import log_likelihod, log_probability
from Utils.colors import blue, green, red, black, magenta


# Read file
df = pd.read_csv (
    'data.txt',
    sep = '&',
    engine = 'python'
)
df.columns = df.columns.str.replace(' ','')

# Objective Function
def objective(theta, x):
    return theta[0] + theta[1]*x + theta[2]*x*x

# Prior function
def log_prior(theta):
    return (-np.inf if all(np.abs(theta) > 500) else 0)

# Get optimal theta
data = np.transpose(df[["x", "y", "sigma_y"]].to_numpy())
A = lambda theta, sign=1: sign*log_probability(log_likelihod(theta, objective, data), log_prior(theta))
guess = [1.0, 1.0, 10.0]
soln = minimize(A, guess, args=(-1))

# Initialise Markov Chain sampler
nwalkers = 50
sampler = mc.EnsembleSampler(nwalkers, 3, A)

# Create Markov Chains
pos = soln.x + 1e-4*np.random.randn(nwalkers, 3)
sampler.run_mcmc(pos, 4000)

# Get Chains and Plot
samples = sampler.get_chain()
medians = np.median(samples, axis=0)

a_bf = np.average(medians[:,2])
b_bf = np.average(medians[:,1])
c_bf = np.average(medians[:,0])

a_sigma = np.std(medians[:,2])
b_sigma = np.std(medians[:,1])
c_sigma = np.std(medians[:,0])

# Get best fit values and uncertainities
print("Best fit values of a, b, c are:", a_bf, b_bf, c_bf)
print("One sigma uncertainities on values of a, b, c are:", a_sigma, b_sigma, c_sigma)

# Plot the markov chains
plt = plt_creator(
    title="Markov Chain: c", 
    xLabel="steps", 
    yLabel="c",
    xMargin=0.02, 
    yMargin=0.02
)
plt.plot(samples[:, :, 0], color="0.0", alpha=0.1) # c values
plt.savefig("Results/c.png")
plt.close()

plt = plt_creator(
    title="Markov Chain: b", 
    xLabel="steps", 
    yLabel="b",
    xMargin=0.02, 
    yMargin=0.02
)
plt.plot(samples[:, :, 1], color="0.0", alpha=0.1) # b values
plt.savefig("Results/b.png")
plt.close()

plt = plt_creator(
    title="Markov Chain: a", 
    xLabel="steps", 
    yLabel="a",
    xMargin=0.02, 
    yMargin=0.02
)
plt.plot(samples[:, :, 2], color="0.0", alpha=0.1) # a values
plt.savefig("Results/a.png")
plt.close()

# Plot the corner distribution
c_true, b_true, a_true = medians[0]
sample = samples[:, 0, :]

fig = corner.corner(
    sample,
    labels=["c", "b", "a"],
    truths=[c_true, b_true, a_true]
)
plt.savefig("Results/corner.png")
plt.close()

# Data Plot
# Order data points
order = np.argsort(data[0])

plt = plt_creator(
    title="Data Fits", 
    xLabel="x", 
    yLabel="y",
    xMargin=0.02, 
    yMargin=0.02
)

# Plot data points
plt.errorbar(data[0], data[1], yerr=data[2], fmt="o", color=black, label="data")

# Plot 200 random models
for i in range (200):
    j = np.random.randint(1, 4000)
    theta = samples[j, 0, :]
    label = "random fit" if i == 0 else '_nolegend_'
    plt.plot(data[0][order], objective(theta, data[0])[order], color=magenta, alpha=0.1, label=label)

# Plot best fit model
plt.plot(data[0][order], objective([c_bf, b_bf, a_bf], data[0])[order], color=blue, label="best fit")

plt.legend(loc ="lower right")
plt.savefig("Results/datafit.png")





