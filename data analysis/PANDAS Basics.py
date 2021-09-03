import pandas as pd

# to read csv:
# a = pd.read_csv('filemane')

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7,  75. ,  83.4,  57.6,  74.6,  75.4,  72.3,  81.5,  80.2,
                          70.3,  72.1,  76.4,  68.1,  75.2,  69.8,  79.4,  70.8,  62.7,
                          67.3,  70.6]

gdp_values = [ 1681.61390973,   2155.48523109,  21495.80508273,    562.98768478,
              13495.1274663 ,   9388.68852258,   1424.19056199,  24765.54890176,
              27036.48733192,   1945.63754911,  21721.61840978,  13373.21993972,
                483.97086804,   9783.98417323,   2253.46411147,  25034.66692293,
               3680.91642923,    366.04496652,   1175.92638695,   1132.21387981]

###
#### Life expectancy and gdp data in 2007 for 20 countries
###

life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

print pd.Series(gdp_values, index=countries)#creates a dictionary from 2 lists
# pd.idxmax returns the index value of where the max value occures
# pd.describe() shows std mean min max and such

def variable_correlation(variable1, variable2):
    i=0
    m1 = variable1.mean()
    m2 = variable2.mean()
    for e in range (0, len(gdp_values)):
        if (variable1[e] > m1 and variable2[e] > m2) or (variable1[e] < m1 and variable2[e] <m2):
            i +=1
    return (i, len(gdp) - i)
print variable_correlation(life_expectancy, gdp)
# print life_expectancy.loc['Angola']

employment_values = [
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076,
]

####     Fill in this function to return the name of the country
####    with the highest employment in the given employment
####    data, and the employment in that country.

employment = pd.Series(employment_values, index=countries)

def max_employment(employment):
    '''    
    Try using the Pandas idxmax() function. Documention can
    be found here:
    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.idxmax.html
    '''
    max_country = employment.idxmax()
    max_value = employment.max()
### OR:
    #max_country = employment.argmax()
    #max_value = employment.loc[max_country]
    
    return (max_country, max_value)
#-------- THATS IT !!!!!-------#

#######
###########||||||||||||||||||||||||||||| .dropna() .add()
#######

# Addition when indexes are the same
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print s1 + s2

# Indexes have same elements in a different order
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['b', 'd', 'a', 'c'])
    print s1 + s2

# Indexes overlap, but do not have exactly the same elements
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    print s1 + s2

# Indexes do not overlap
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
    print s1 + s2

######
#### To fix the problem with NaN, run function .dropna() or .add()
######
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
sum_result = s1 + s2
print sum_result.dropna()

######### OR use .add() with fill_value = 0, keeping unmatched index unchanged
sr = s1.add(s2, fill_value = 0)
print sr

######|||||||||||||||||||||||||||||||||||||


######
######      .APPLY()
######

if False:
    s = pd.Series([1, 2, 3, 4, 5])
    def add_one(x):
        return x + 1
    print s.apply(add_one)

# Switch firstvand last names in the series through .apply()

names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])

def reverse_name(name):
    a = name.split(" ")
    b = a[0]
    c = a[1]
    return c + ", " + b
    
def reverse_names(names):
    return names.apply(reverse_name)
