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
total_minutes_by_acct = {}#-> {student : total minutes on all assignments}

for account_key, list_of_engagements in eng_by_acct.items():# looping through {x : []}
    total_minutes = 0
    for record in list_of_engagements:# looping through each []
        total_minutes += float(record['total_minutes_visited'])
    total_minutes_by_acct[account_key] = total_minutes

total_minutes = total_minutes_by_acct.values()# to get list of values from dict

import numpy as np

#print 'Mean:', np.mean(total_minutes) # Solution!
#print 'Standard deviation:', np.std(total_minutes)
#print 'Minimum:', np.min(total_minutes)
#print 'Maximum:', np.max(total_minutes)

##### ANALISYS OF THE FIRST RUN AND FIXING THE PROBLEM:
"""
########
#######   As looking at results, STD and MAX are too large => smth is wrong
######   Finding the problematic student:

a = np.max(total_minutes)
for key, value in total_minutes_by_acct.items():
    if value == a:
        print key
        
problematic_student = key
# pulling records on the student
for engagement_record in paid_engagement_first_week:
    if engagement_record['acct'] == problematic_student:
        print engagement_record
        
### by looking at the data, we can assess that the problem is in the earlier function:
### if a student enrolls, then cancels, then enrolls again, his engagement_date - join_date will be negative
### and therefore < 7.   So that line in the code has to be adjusted -> added "and (ed - jd).days >= 0"
"""

#####
##### Split project_submissions into 2 lists:
##### paid students who passed the subway project and those who didnt
#####

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
for key in total_minutes_by_acct:
    if key in passing:
        passmin.append(total_minutes_by_acct[key])
    else:
        nopassmin.append(total_minutes_by_acct[key])
        
#print 'Mean pass:', np.mean(passmin), 'Mean nopass:', np.mean(nopassmin) # Solution!
#print 'STD:', np.std(passmin), 'STD:', np.std(nopassmin)
#print 'Min pass:', np.min(passmin), 'Min nopass:', np.min(nopassmin)
#print 'MAX pass:', np.max(passmin), 'MAX nopass:', np.max(nopassmin)
        
import matplotlib.pyplot as plt
plt.hist(passmin)
plt.hist(nopassmin)
## !!   type "plt.show()" in the shell for the histogramm
