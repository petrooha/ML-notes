from datetime import datetime as dt
import csv

enrollments_filename = 'C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/enrollments.csv'

with open(enrollments_filename, 'rb') as f:
    reader = csv.DictReader(f)
    enrollments = list(reader)

# Returns a date type or None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')


# Returns an integer or None
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

print enrollments[0]

for row in enrollments:
    row['cancel_date'] = parse_date(row['cancel_date'])
    row['days_to_cancel'] = parse_maybe_int(row['days_to_cancel'])
    row['is_cancel'] = row['is_canceled'] == 'True'
    row['is_udacity'] = row['is_udacity'] == 'True'
    row['join_date'] = parse_date(row['join_date'])

print enrollments[0]

d = set()
for row in enrollments:
    d.add(row['account_key'])# 'add' makes sure the value is not already in the list
print len(d)
