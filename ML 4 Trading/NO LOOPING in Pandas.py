import pandas as pd

daily_returns = df.copy() # copy given DataFrame to match size and column names


# compute daily returns for row 1 onwards
# Panda devides the whole row by another row, dont need to loop!!!
daily_returns[1:] = (df[1:] / df[:-1].values) - 1
# .values is needed so that pandas won't try to match rows based on index
# we want them shifted by one, because returns are compared to previous day

daily_returns.ix[0,:] = 0 # set daily returns for row 0 to 0



# another way to loop with Pandas
daily_returns1 = (df / df.shift(1)) - 1
daily_returns1.ix[0,:] = 0


#... and ploting
def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

# Compute stocks chart
plot_data(df)

# Compute daily returns
daily_returns = compute_daily_returns(df)
plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
