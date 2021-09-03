import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(df, title="Stock prices"):
    '''Plot stock prices'''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

# Plot a histogram
daily_returns.hist(bins=20)
plt.show

# Get mean, STD and kurtosis
mean = daily_returns['SPY'].mean()
std = daily_returns['SPY'].std()
kurt = daily_returns.kurtosis # if number is positive - "Fat tails", higher volatility

# Add lines to histogram showing mean and boundries within STD
plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
plt.show()

# Compute and plot both histograms on the same chart
daily_returns['SPY'].hist(bins=20, label="SPY")
daily_returns['XOM'].hist(bins=20, label="XOM")
plt.legend(loc='upper right')
plt.show()


# Scatterplot SPY vs XOM
# show alfa and betta
# last is correlation line
daily_returns.plot(kind='scatter', x='SPY', y='XOM')
betta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')
plt.show()

print "alfa SPY vs XOM ", alfa_XOM
print "beta XOM vs SPY", beta_XOM
print "Correlation of XOM to SPY ", daily_returns.cott(method='pearson')
