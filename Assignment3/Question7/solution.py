'''
This script provides the solution
for Question 7 of Assignment 3
'''

# Python imports
import numpy as np
from scipy.stats import chi2


# Get Chi-2 value
def getChi2(Sample, Exp):
    return np.sum((Sample - Exp)**2/Exp)

# Get Chi-2 Probability
def getProb(V, k):
    return 1 - chi2.cdf(V, k)

# Chi-2 test labels
def heuristics(Prob):
    if (Prob < 1 or Prob > 99):
        return "Not Sufficiently Random"
    elif (Prob < 5 or Prob > 95):
        return "Suspect"
    elif (Prob < 10 or Prob > 90):
        return "Almost Suspect"
    else:
        return "Suspect"

# Random Samples
Samp1 = np.asarray([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13])
Samp2 = np.asarray([3, 7, 11, 15 ,19, 24, 21, 17, 13, 9, 5])

# Probability distribution
Prob = np.asarray([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])/36

# Sample 1
p = getProb(getChi2(Samp1, Prob*np.sum(Samp1)), len(Samp1)-1)*100
print("Chi-2 probability for Sample 1 is %f"%p)
print("Sample 1 is:", heuristics(p))

# Sample 2
p = getProb(getChi2(Samp2, Prob*np.sum(Samp2)), len(Samp2)-1)*100
print("Chi-2 probability for Sample 2 is %f"%p)
print("Sample 2 is:", heuristics(p))




