import numpy as np

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

# Change False to True for each block of code to see what it does

# Accessing elements
if False:
    print ridership[1, 3]
    print ridership[1:3, 3:5]
    print ridership[1, :]
    
# Vectorized operations on rows or columns
if False:
    print ridership[0, :] + ridership[1, :]
    print ridership[:, 0] + ridership[:, 1]
    
# Vectorized operations on entire arrays
if False:
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print a + b

def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    '''
    i = ridership[0,:].argmax()
    
    overall_mean = ridership.mean()
    mean_for_max = ridership[:,i].mean()
    
    return (overall_mean, mean_for_max)

# NumPy axis argument
if False:
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print a.sum()
    print a.sum(axis=0)
    print a.sum(axis=1)


#       ******************************************      #
#########                                       ##########
######### Dataframes ||||||||||||||||||||||     ##########
    ####                                        #########


import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)

# Change False to True for each block of code to see what it does

# DataFrame creation
if False:
    # You can create a DataFrame out of a dictionary mapping column names to values
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print df_1

    # You can also use a list of lists or a 2D NumPy array
    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    print df_2
   

# Accessing elements
if False:
    print ridership_df.iloc[0]
    print ridership_df.loc['05-05-11']
    print ridership_df['R003']
    print ridership_df.iloc[1, 3]
    
# Accessing multiple rows
if False:
    print ridership_df.iloc[1:4]
    
# Accessing multiple columns
if False:
    print ridership_df[['R003', 'R005']]
    
# Pandas axis
if False:
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print df.sum()
    print df.sum(axis=1)# or axis = 'colomns' or 'index'
    print df.values.sum()


##############
######### This is the same as "mean_riders_for_max_station()" exercise, 
######    but this time the input is a Pandas DataFrame rather than a 2D NumPy array.
###############
if False:
    i = ridership_df.loc['05-01-11'].idxmax()# or .iloc[0]
        
    overall_m = ridership_df.values.mean()
    m_for_max = ridership_df[i].mean()

    print overall_m, m_for_max

######||||||||||||||||||||||||||||||#############################
###########################||||||||||||||||||||||||||||||||||||||######################


#####$$     Calculating CORRELATION     where x & y are arrays:
##########  built-in as "np.corrcoef(x,y)"

def correlation(x, y):

    mx = x.mean()
    my = y.mean()
    sx = x.std(ddof=0)
    sy = y.std(ddof=0)
    a = 0
    for i in range(len(x)):
        a = a + ((x[i] - mx)/ sx) * ((y[i] - my)/ sy)

    return a / len(x)


###########################                      ########################
#                           VECTORIZED FUNCTIONS
###########################                      ########################

# Adding DataFrames with the column names
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]})
    print df1 + df2
    
# Adding DataFrames with overlapping column names 
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df2 = pd.DataFrame({'d': [10, 20, 30], 'c': [40, 50, 60], 'b': [70, 80, 90]})
    print df1 + df2

# Adding DataFrames with overlapping row indexes
if False:
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]},
                       index=['row1', 'row2', 'row3'])
    df2 = pd.DataFrame({'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 90]},
                       index=['row4', 'row3', 'row2'])
    print df1 + df2

# --- Quiz ---
# Cumulative entries and exits for one station for a few hours.
entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
    })
# one-step function:

#print entries_and_exits.diff()

# OR with .SHIFT(x) which shifts an array x rows down:

#print 'Solution: ', entries_and_exits - entries_and_exits.shift(1)
#--------------------------------------------------------------------


########
########
########         DataFrame APPLYMAP()


if False:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })
    
    def add_one(x):
        return x + 1
        
    print df.applymap(add_one)

#-----      Switch number to grading letter
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
def convert_g(grade):
    if grade > 89:
        g = 'A'
    elif grade > 79:
        g = 'B'
    elif grade > 69:
        g = 'C'
    elif grade > 59:
        g = 'D'
    else:
        g = 'F'
    return g
def convert_grades(grades):# always need 2 functions
    return grades.applymap(convert_g)
########################-------------------------------------




#               DataFrame APPLY()  &  QCUT()


if False:
    def convert_grades_curve(exam_grades):
        # Pandas has a bult-in function that will perform this calculation
        # This will give the bottom 0% to 10% of students the grade 'F',
        # 10% to 20% the grade 'D', and so on. You can read more about
        # the qcut() function here:
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
        return pd.qcut(exam_grades,
                       [0, 0.1, 0.2, 0.5, 0.8, 1],
                       labels=['F', 'D', 'C', 'B', 'A'])
        
    # qcut() operates on a list, array, or Series. This is the
    # result of running the function on a single column of the
    # DataFrame.
    print convert_grades_curve(grades_df['exam1'])
    
    # qcut() does not work on DataFrames, but we can use apply()
    # to call the function on each column separately
    print grades_df.apply(convert_grades_curve)

###
#####  Standardize a column:
###
def standardize_column(column):
    return (column - column.mean()) / column.std(ddof=0)# will produce column of values
def standardize(df):
    return df.apply(standardize_column)# each column of df will be standardized
#------------------------


########                            ##########
####                SORT                ######
########                            ##########

def second_largest_in_column(column):
    sorted_column = column.sort_values(ascending=False)
    return sorted_column.iloc[1]
#-------------------------------------


#       ****************************************        \\\\\\\\\\\\
#       ****************************************        >>>>>>>>>>>>



#####################
##################### Adding a Series to a DataFrame
#####################


if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' 
    print df + s
    
# Adding a Series to a one-row DataFrame 
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10], 1: [20], 2: [30], 3: [40]})
    
    print df
    print '' 
    print df + s

# Adding a Series to a one-column DataFrame
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({0: [10, 20, 30, 40]})
    
    print df
    print '' 
    print df + s
    

    
# Adding when DataFrame column names match Series index
if False:
    s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    print df
    print '' 
    print df + s
    
# Adding when DataFrame column names don't match Series index
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        'a': [10, 20, 30, 40],
        'b': [50, 60, 70, 80],
        'c': [90, 100, 110, 120],
        'd': [130, 140, 150, 160]
    })
    
    print df
    print '' 
    print df + s
########||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Adding using +
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' 
    print df + s
    
# Adding with axis='index'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' 
    print df.add(s, axis='index')
    # The functions sub(), mul(), and div() work similarly to add()
    
# Adding with axis='columns'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })


    print df
    print '' 
    print df.add(s, axis='columns')
    # The functions sub(), mul(), and div() work similarly to add()

#######          /\ 
####            //\\
##             //  \\
##            //_  _\\
##               ||
    #            ||
    # Some other functions


#
####
#######
##########
    #########   STNDARDIZE without APPLY()
##########
#######
####
df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })

def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    
    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''

    print df
    a = []
    
    b = []
    
    for e in range(len(df.columns)):
        a.append(df[e].mean())
        b.append(df[e].std(ddof=0))

    df = df.sub(a, axis='columns')
    df = df.div(b, axis='columns')
    print a
    print b
    print df

#____/////----  OR SIMPLY  -->

    df = (df - df.mean()) / df.std()
    
def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().
    
    This one is more challenging than standardizing each column!
    '''
    print df
    a = []
    
    b = []
    
    for e in range(len(df)):
        a.append(df.iloc[e].mean())
        b.append(df.iloc[e].std(ddof=0))

    df = df.sub(a, axis='index')
    df = df.div(b, axis='index')
    print a
    print b
    print df

#______/////----- OR  :--> 
    
    df = df.sub(df.mean(axis='columns'), axis = 'index')
    df = df.div(df.std(axis = 'columns'), axis = 'index')
    ##!!!!!   axises here = opposite of what default is         !!!!!!!!

###----------------------------------------------------------------------###
###======================================================================###



###                                                     ###
#######                                             #######
############                                    ###########
    ###########         GROUPBY()           #############
############                                    ###########
#######                                             #######
###                                                     ###
    
import matplotlib.pyplot as plt

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does

# Examine DataFrame
if False:
    print example_df
    
# Examine groups
if False:
    grouped_data = example_df.groupby('even')
    # The groups attribute is a dictionary mapping keys to lists of row indexes
    print grouped_data.groups
    
# Group by multiple columns
if False:
    grouped_data = example_df.groupby(['even', 'above_three'])
    print grouped_data.groups
    
# Get sum of each group
if False:
    grouped_data = example_df.groupby('even')
    print grouped_data.sum()
    
# Limit columns in result
if False:
    grouped_data = example_df.groupby('even')
    
    # You can take one or more columns from the result DataFrame
    print grouped_data.sum()['value']
    
    print '\n' # Blank line to separate results
    
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
    print grouped_data['value'].sum()


# groupby() without as_index
if True:
    first_even = example_df.groupby('even').first()
    print first_even
    # print first_even['even'] # Causes an error. 'even' is no longer a column in the DataFrame
    
# groupby() with as_index=False
if False:
    first_even = example_df.groupby('even', as_index=False).first()
    print first_even
    print first_even['even'] # Now 'even' is still a column in the DataFrame


############|||||||||||||||||||||||||||||||||||||||\\\\\\\\\
    ##########||||||||||||||||||||||||||||||||||||      >>>>>>>>>>>>>>
    ##########||||||||||||||||||||||||||||||||||||//////////
    

filename = 'nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

'''Write code here to group the subway data by a variable of your choice, then
either print out the mean ridership within each group or create a plot.

I group by day of the week and by weather conditions
'''
if False:
    grouped_sub = subway_df.groupby(['conds']).mean()['ENTRIESn_hourly']
    print grouped_sub
    grouped_sub.plot()

    grouped_day = subway_df.groupby(['day_week'])
    print grouped_day.mean()['ENTRIESn_hourly']
    grouped_day.mean()['ENTRIESn_hourly'].plot()
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||




########
    #######
    ##########      GROUPBY() with APPLY()      !!!!!!!!!!!!!!!!!!!!!!!!!
    #######             
########                    Dataframe sorts on its own

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Standardize each group
if False:
    def standardize2(xs):
        return (xs - xs.mean()) / xs.std()
    grouped_data = example_df.groupby('even')
    print grouped_data['value'].apply(standardize2)
    
# Find second largest value in each group
if False:
    def second_largest(xs):
        sorted_xs = sorted(xs, reverse=False)
        return sorted_xs[1]# .iloc produces error
    grouped_data = example_df.groupby('even')
    print grouped_data['value'].apply(second_largest)


########      !!!!!                 !!!!!           !!!!


# DataFrame with cumulative entries and exits for multiple stations
ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

'''
    Fill in this function to take a DataFrame with cumulative entries
    and exits and return a DataFrame with hourly entries and exits.
    The hourly entries and exits should be calculated separately for
    each station (the 'UNIT' column).
    
    Hint: Take a look at the `get_hourly_entries_and_exits()` function
    you wrote in a previous quiz, DataFrame Vectorized Operations. If
    you copy it here and rename it, you can use it and the `.apply()`
    function to help solve this problem.
    '''
def get_hourly_entries_and_exits(entries_and_exits):
    return entries_and_exits - entries_and_exits.shift(1)# not (2), and no sorting needed either

if False:
    print ridership_df
    print ridership_df.groupby(['UNIT'])['ENTRIESn','EXITSn'].apply(get_hourly_entries_and_exits)

##|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
##||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||





                        #######
###########             MERGE()
                        #######




subway_df = pd.DataFrame({
    'UNIT': ['R003', 'R003', 'R003', 'R003', 'R003', 'R004', 'R004', 'R004',
             'R004', 'R004'],
    'DATEn': ['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
              '05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'ENTRIESn': [ 4388333,  4388348,  4389885,  4391507,  4393043, 14656120,
                 14656174, 14660126, 14664247, 14668301],
    'EXITSn': [ 2911002,  2911036,  2912127,  2913223,  2914284, 14451774,
               14451851, 14454734, 14457780, 14460818],
    'latitude': [ 40.689945,  40.689945,  40.689945,  40.689945,  40.689945,
                  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ,  40.69132 ],
    'longitude': [-73.872564, -73.872564, -73.872564, -73.872564, -73.872564,
                  -73.867135, -73.867135, -73.867135, -73.867135, -73.867135]
})

weather_df = pd.DataFrame({
    'DATEn': ['05-01-11', '05-01-11', '05-02-11', '05-02-11', '05-03-11',
              '05-03-11', '05-04-11', '05-04-11', '05-05-11', '05-05-11'],
    'hour': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'latitude': [ 40.689945,  40.69132 ,  40.689945,  40.69132 ,  40.689945,
                  40.69132 ,  40.689945,  40.69132 ,  40.689945,  40.69132 ],
    'longitude': [-73.872564, -73.867135, -73.872564, -73.867135, -73.872564,
                  -73.867135, -73.872564, -73.867135, -73.872564, -73.867135],
    'pressurei': [ 30.24,  30.24,  30.32,  30.32,  30.14,  30.14,  29.98,  29.98,
                   30.01,  30.01],
    'fog': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'rain': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tempi': [ 52. ,  52. ,  48.9,  48.9,  54. ,  54. ,  57.2,  57.2,  48.9,  48.9],
    'wspdi': [  8.1,   8.1,   6.9,   6.9,   3.5,   3.5,  15. ,  15. ,  15. ,  15. ]
})

def combine_dfs(subway_df, weather_df):
    '''
    Fill in this function to take 2 DataFrames, one with subway data and one with weather data,
    and return a single dataframe with one row for each date, hour, and location. Only include
    times and locations that have both subway data and weather data available.
    '''
    
    return subway_df.merge(weather_df, on=['DATEn', 'hour', 'latitude','longitude'], how='inner')
# how can also = outter, left or right
# if column names are different for both tables, left_on = [DATEn, HOURSn'], right_on = [date, hour]


# Plots: https://classroom.udacity.com/courses/ud170/lessons/5428018709/concepts/54422618100923
