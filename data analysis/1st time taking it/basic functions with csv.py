import csv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/enrollments.csv')
daily_engagement = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/daily_engagement.csv')
project_submissions = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/project_submissions.csv')
    
### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

enrollment_num_rows = len(enrollments)
d = set()
for row in enrollments:
    d.add(row['account_key']) # row[0] produces an error, because 'row' or 'line' doesn't mean anything by themselves and can be 'a' or 'x' or any other variable
enrollment_num_unique_students = len(d)

engagement_num_rows = len(daily_engagement)
e = set()
for row in daily_engagement:
    e.add(row['acct'])
engagement_num_unique_students = len(e)

submission_num_rows = len(project_submissions)
f = set()
for row in project_submissions:
    f.add(row['account_key'])
submission_num_unique_students = len(f)

"""
print enrollment_num_rows
print enrollment_num_unique_students

print engagement_num_rows
print engagement_num_unique_students

print submission_num_rows

print submission_num_unique_students"""

# to recognize the pattern between engagement and enrollment; 
# the pattern can be seen or recognized through other functions, such as looping each colomn
"""
a= set()
for i in d:
    if i not in e:
        a.add(i)
print a

for row in enrollments:
    if row['account_key'] in a:
        print row
"""
# the pattern is that days_to_cancel == 0 or '' becides 2 accounts which had is_udacity : True
# there was total 6 accounts with is-udacity : True, which turned out to be test accounts and need to be removed:
def remove_udacity_accounts(data):
    non_udacity_data = []
    for row in data:
        if row['is_udacity'] == 'False':
            non_udacity_data.append(row)
    return non_udacity_data
non_udacity_enrollments = remove_udacity_accounts(enrollments)
print len(non_udacity_enrollments) # just to check
