from matplotlib.pyplot import ylabel


# Function for returning a plt instance

import matplotlib.pyplot as plt

def plt_creator(title="", xLabel="", yLabel="", xMargin=0, yMargin=0):
    
    plt.figure()
    plt.margins(xMargin)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    return plt