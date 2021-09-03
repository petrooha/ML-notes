import csv
import numpy

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/enrollments.csv')
daily_engagement = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/daily_engagement.csv')
project_submissions = read_csv('C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/project_submissions.csv')

def remove_udacity_accounts(data):
    non_udacity_data = []
    for row in data:
        if row['is_udacity'] == 'False':
            non_udacity_data.append(row)
    return non_udacity_data
non_udacity_enrollments = remove_udacity_accounts(enrollments)
enrollments = non_udacity_enrollments

#########
######### dictionary of students who hasnt canceled or canceled passed 7 days
# #######       {account_key : join_date}

paid_students = {}
def is_float(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

for line in enrollments:
    if is_float(line['days_to_cancel']):
        if float(line['days_to_cancel']) > 7:
            account_key = line['account_key']
            date = line['join_date']
            if account_key not in paid_students or date > paid_students[account_key]:# to make the enrollment date the most recent 
                paid_students[account_key] = date
    else:#if the days_to_cancel is not a number, then the enrollment wasnt canceled
        account_key = line['account_key']
        date = line['join_date']
        paid_students[account_key] = date
#print len(paid_students)

#######
######## Create a list of rows from the engagement table, including only paid students, with engagements within 1 week of the student's join date:
#########

from datetime import datetime

q=0
paid_engagement_first_week = []
for row in daily_engagement:
    if row['acct'] in paid_students:
        stud = row['acct']
        ed = datetime.strptime(row['utc_date'], "%Y-%m-%d")
        jd = datetime.strptime(paid_students[stud], "%Y-%m-%d")
        if (ed - jd).days < 7 and (ed - jd).days >= 0:
            paid_engagement_first_week.append(row)
#print len(paid_engagement_first_week)


##########
########## Create a Dictionary {paid_student : "list of engagements"}
########## then, compute the average of minutes spent on engagements

from collections import defaultdict

eng_by_acct = defaultdict(list)## creates {x : []}
for eng_record in paid_engagement_first_week:
    account_key = eng_record['acct']# assigns the key (x)
    eng_by_acct[account_key].append(eng_record)# appends to []

#then:
days_by_acct = {}#-> {student : total days}

for account_key, list_of_engagements in eng_by_acct.items():# looping through {x : []}
    total_days = 0
    for record in list_of_engagements:# looping through each []
        if float(record['num_courses_visited']) > 0:
            total_days += 1
        
    days_by_acct[account_key] = total_days

dayz = days_by_acct.values()# to get list of values from dict

import numpy as np

#print 'Mean:', np.mean(dayz) # Solution!
#print 'Standard deviation:', np.std(dayz)
#print 'Minimum:', np.min(dayz)
#print 'Maximum:', np.max(dayz)


#########
#### Students who pass
################

paid_submissions = []
for row in project_submissions:
    if row['account_key'] in paid_students:
        paid_submissions.append(row)
        
splk = ['746169184', '3176718735']
passing = set()
subway_studs = set()
for row in paid_submissions:
    if row['lesson_key'] in splk:
        if row['assigned_rating'] == 'PASSED' or row['assigned_rating'] == 'DISTINCTION':
            passing.add(row['account_key'])
print len(passing)

# Analyze total minutes spent for each group of students (also total dayz and lessons)

passmin = []
nopassmin = []
for key in days_by_acct:
    if key in passing:
        passmin.append(days_by_acct[key])
    else:
        nopassmin.append(days_by_acct[key])
        
#print 'Mean pass:', np.mean(passmin), 'Mean nopass:', np.mean(nopassmin) # Solution!
#print 'STD:', np.std(passmin), 'STD:', np.std(nopassmin)
#print 'Min pass:', np.min(passmin), 'Min nopass:', np.min(nopassmin)
#print 'MAX pass:', np.max(passmin), 'MAX nopass:', np.max(nopassmin)

import matplotlib.pyplot as plt
plt.hist(passmin)
plt.hist(nopassmin)
