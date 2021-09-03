from datetime import datetime as dt
import csv

enrollment_filename = 'C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/enrollments.csv'

with open(enrollment_filename, 'rb') as e:
    reader = csv.DictReader(e)
    enrollments = list(reader)

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

for row in enrollments:
    row['days_to_cancel'] = parse_maybe_int(row['days_to_cancel'])
    row['is_cancel'] = row['is_canceled'] == 'True'


#=======================================
# Creating new dictionary here
paid_students = {}
for enrollment in enrollments:
    if (enrollment['days_to_cancel'] == None or
            enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']# creates key
        enrollment_date = enrollment['join_date']# creates value
        if account_key not in paid_students:
            paid_students[account_key] = enrollment_date#assigns value to a key
print len(paid_students)
