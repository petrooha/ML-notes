import numpy as np

countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076,  51.40000153,  50.5       ,  75.69999695,
    58.40000153,  40.09999847,  61.5       ,  57.09999847,
    60.90000153,  66.59999847,  60.40000153,  68.09999847,
    66.90000153,  53.40000153,  48.59999847,  56.79999924,
    71.59999847,  58.40000153,  70.40000153,  41.20000076])

if True:
    print countries.dtype
    print employment.dtype
    print np.array([0, 1, 2, 3]).dtype
    print np.array([1.0, 1.5, 2.0, 2.5]).dtype
    print np.array([True, False, True]).dtype
    print np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype

# Looping
if False:
    for country in countries:
        print 'Examining country {}'.format(country)

    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        print 'Country {} has employment {}'.format(country,
                country_employment)
        
def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    
    i = 0
    for r in range(len(employment)):
        if employment[r] > i:
            i = employment[r]
            rs = r
    max_country = countries[rs]
    max_value = employment[rs]

    return (max_country, max_value)
    '''
    # OR simply:
    i = employment.argmax()
    return (countries[i], employment[i])

######
######
######

    '''
    Fill in this function to return a standardized version of the given values,
    which will be in a NumPy array. Each value should be translated into the
    number of standard deviations that value is away from the mean of the data.
    '''
    
def standardize_data(values):
    s = values.std()# np.std(values) also works
    m = values.mean()
    r = (values - m) / s
    return r


# Change False to True for each block of code to see what it does

# Arithmetic operations between 2 NumPy arrays
if False:
    a = np.array([1, 2, 3, 4])
    b = np.array([1, 2, 1, 2])
    
    print a + b
    print a - b
    print a * b
    print a / b
    print a ** b
    
# Arithmetic operations between a NumPy array and a single number
if False:
    a = np.array([1, 2, 3, 4])
    b = 2
    
    print a + b
    print a - b
    print a * b
    print a / b
    print a ** b
    
# Logical operations with NumPy arrays
if False:
    a = np.array([True, True, False, False])
    b = np.array([True, False, True, False])
    
    print a & b
    print a | b
    print ~a
    
    print a & True
    print a & False
    
    print a | True
    print a | False
    
# Comparison operations between 2 NumPy Arrays
if False:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 4, 3, 2, 1])
    
    print a > b
    print a >= b
    print a < b
    print a <= b
    print a == b
    print a != b
    
# Comparison operations between a NumPy array and a single number
if False:
    a = np.array([1, 2, 3, 4])
    b = 2
    
    print a > b
    print a >= b
    print a < b
    print a <= b
    print a == b
    print a != b

#####
#####  Using index arrays
#####
    
if False:
    a = np.array([1, 2, 3, 4])
    b = np.array([True, True, False, False])
    
    print a[b]
    print a[np.array([True, False, True, False])]
    
# Creating the index array using vectorized operations
if False:
    a = np.array([1, 2, 3, 2, 1])
    b = (a >= 2)
    
    print a[b]
    print a[a >= 2]
    
# Creating the index array using vectorized operations on another array
if False:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 2, 1])
    
    print b == 2
    print a[b == 2]


#####
##### Modifying slice of an array modifies an array
#####



###        + vs. +=

    
if False:
    a = np.array([1,2,3,4])
    b = a
    a += np.array([1,1,1,1])
    print b
if False:
    a = np.array([1,2,3,4])
    b = a
    a = a + np.array([1,1,1,1])
    print b
