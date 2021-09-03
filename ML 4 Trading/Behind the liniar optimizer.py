import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo

def error(line, data): # error function for minimizer to minimize
    """Compute error between given line model and observed data.

    Parameters
    ---------
    line: tuple/list/array (C0, C1) where C0 is the slope and C1 is Y-intercept
    data: 2D array where each row is a point (x, y)

    Returns error as a single value."""

    # Metric: Sum of squares Y-axis diffirences between
    # each point of data and corresponding point on the line
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1]))**2)
    return err

# Define original line
l_orig = np.float32([4,2])
print "Original line: CO = {}, C1 = {}".format(l_orig[0], l_orig[1])
Xorig = np.linspace(0, 10, 21) # 21 equaly spaced points btw 0 and 10
Yorig = l_orig[0]*Xorig + l_orig[1]
plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")

# Generate noisy data points
noise_sigma = 5.0
noise = np.random.normal(0, noise_sigma, Yorig.shape)
data = np.asarray([Xorig, Yorig + noise]).T
plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")


# Try to fit line to this data
def fit_line(data, error_func):
    """Fit a line to given data, using a supplied error function.

    Parameters
    ---------
    data: 2D array where each row is a point (X0, Y)
    error_func: function that computes the error between a line and observed data
    returns line that minimizes the error function."""
    # Generate initial guess for line model
    l = np.float32([0, np.mean(data[:, 1])]) # slope = 0, intercept = mean(y values)

    # Plot initial guess (optional)
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0]*x_ends + l[1], 'm--', linewidth=2.0, label="Initial guess")

    # Call optimizer to minimize error function
    result = spo.minimize(error_func, l, args=(data), method='SLSQP')
    return result.x


l_fit = fit_line(data, error)
print "Fitted line: CO = {}, C1 = {}".format(l_fit[0], l_fit[1])
plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth =2, label="Fitted line")
plt.show()

