import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates = pd.date_range(start_date, end_date)
    df1=pd.DataFrame(index=dates)
    print df1
    
    #index_col is parameter to be an index column
    #use_cols to narrow down to select columns
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['NaN'])

    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})#<<<<<<<<<<<<<<<< add this line and 1 more
    
    #all the rows from df1 + rows of SPY that are present in df1
    df1 = df1.join(dfSPY, how='inner')
    # without how='inner', one more command would be needed to drop NaN values:
    df1 = df1.dropna()
    print df1

    
    # do the same thing as for SPY but for more symbols:
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp=pd.read_csv("data/{}.csv".format(symbol), index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['NaN'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})#<<<<<<<<<<<< and this one to avoid the error of overlapping
        df=df1.join(df_temp, how='left')
        if symbol == 'SPY':
            df=df.dropna(subset=['SPY'])#if SPY has NaN all will have NaN
    print df
###########             SLICING DATA
    
    print df.ix['2010-01-22':'2010-01-24',['GOOG','GLD']]# rows and columns
    print df[['GOOG','GLD']]# few columns
    print df['2010-01-22':'2010-01-24']# few rows

###########

    df1 = df1/df1[0]# so that all price points are % of the first price
    """
the same thing would be done if not in pandas as:
    for dat in df1.index:
        for s in symbols:
            df1[date, s] = df1[date, s]/df1[0, s]
"""

######                  PLOTTING        ######

import matplotlib.pyplot as plt
def plot_data(df, title="Stock prices"):
    '''Plot stock prices'''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
if __name__ == "__main__":
    test_run()
