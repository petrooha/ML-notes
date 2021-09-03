from datetime import datetime as dt
import csv

enrollments_filename = 'C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/enrollments.csv'

with open(enrollments_filename, 'rb') as f:
    reader = csv.DictReader(f)
    enrollments = list(reader)

print "Total Enrollments ", len(enrollments)
d = set()
for row in enrollments:
    d.add(row['account_key'])# 'add' makes sure the value is not already in the list
print "Unique Students Enrolled ", len(d)

# OR with Pandas:

import pandas as pd

engagements = pd.read_csv('daily_engagement.csv')
print len(engagements['acct'].unique())

## OR make a universal function
def unique_set(filename):
    print len(filename)
    uni_set = set()
    for row in filename:
        uni_set.add(row['account_key'])# 'account_key' or any feature by which the data should be classified as unique
    return uni_set
