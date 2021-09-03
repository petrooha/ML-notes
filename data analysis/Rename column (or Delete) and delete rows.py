from datetime import datetime as dt
import csv

engagement_filename = 'C:/Users/Mishka Mars/Desktop/Petya/Udacity/data analysis/daily_engagement.csv'

with open(engagement_filename, 'rb') as f:
    reader = csv.DictReader(f)
    engagement = list(reader)


# Rename column 'acct' to 'account_key'
for line in engagement:
    line['account_key'] = line['acct']
    del line['acct']
 
# To delete:
# https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary






# to delete rows:
"""
this stuff will run error because need to read the files here and fix column name

#1 creating a set of test accounts [is_udacity:True]
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])

#2 making a function to return updated dictionaries
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

#3 updating all tables 
non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagements = remove_udacity_accounts(engagementss)
non_udacity_submitions = remove_udacity_accounts(submitions)
"""
