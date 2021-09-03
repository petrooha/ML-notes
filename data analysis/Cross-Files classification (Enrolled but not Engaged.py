from datetime import datetime as dt
import csv

engagement_filename = 'C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/daily_engagement.csv'
enrollment_filename = 'C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/enrollments.csv'

with open(engagement_filename, 'rb') as f:
    reader = csv.DictReader(f)
    engagement = list(reader)

with open(enrollment_filename, 'rb') as e:
    reader = csv.DictReader(e)
    enrollment = list(reader)

for line in engagement:
    line['account_key'] = line['acct']
    del line['acct']
## standart operations untill here ===============================
    
# next, set of unique students enrolled 
d = set()
for row in enrollment:
    d.add(row['account_key'])

# unique students engaged
q = set()
for row in engagement:
    q.add(row['account_key'])

# unique students enrolled but not engaged
not_in = set()
for row in d:
    if row not in q:
        not_in.add(row)
print "Were enrolled but not engaged ", len(not_in)


# Enrollment data for enrolled but not engaged
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)
for row in enrollment:
    row['days_to_cancel'] = parse_maybe_int(row['days_to_cancel'])
    
for line in enrollment:
    if line['account_key'] in not_in:
        if line['days_to_cancel'] != 0:
            print line



