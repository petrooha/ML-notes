import csv

enrollments_filename = 'C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

enrollments = []
f = open(enrollments_filename, 'rb')
reader = unicodecsv.DictReader(f)
for row in reader:
    enrollments.append(row)
f.close()

# OR:

with open(enrollments_filename, 'rb') as f:
    reader = csv.DictReader(f)
    enrollments = list(reader)

# OR with Pandas:
import pandas as pd
engagements = pd.read_csv('daily_engagement.csv')

# OR EVEN BETTER:

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/enrollments.csv')
daily_engagement = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/daily_engagement.csv')
project_submissions = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/project_submissions.csv')


# It takes few seconds to import Pandas, but it saves LOTS of time on the back end

import pandas as pd
daily_engagements = pd.read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/daily_engagement.csv')
##### read_csv is built in in pandas
print len(daily_engagements['acct'].unique())
# unique() is like set()
