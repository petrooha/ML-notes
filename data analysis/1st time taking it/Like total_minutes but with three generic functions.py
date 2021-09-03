####        1
###### to group the records by acct_key
####

from collections import defaultdict

def group_data(data, key_name):# key_name - key to group by
    grouped_data = defaultdict(list)## creates {x : []}
    for data_point in data:
        key = data_point[key_name]# assigns the key (x)
        grouped_data[key].append(data_point)# appends to []
    return grouped_data
#engagement_by_acct = group_data(paid_engagement_first_week, 'acct')

####        2
###### to sum up all the entries for acct_key
####

def sum_grouped_items(grouped_data, field_name):
    summed_data = {}#-> {field_name : total of all values}

    for key, data_points in grouped_data.items():# looping through {x : []}
        total = 0
        for data_point in data_points:# looping through each []
            total += float(data_point[field_name])
        summed_data[key] = total
    return summed_data

#total_minutes_by_acct = sum_grouped_items(engagement_by_account, 'total_minutes_visited')

#####       3
####### STATS
#####

import numpy as np

def describe_data(data):
    print 'Mean:', np.mean(total_minutes) # Solution!
    print 'Standard deviation:', np.std(total_minutes)
    print 'Minimum:', np.min(total_minutes)
    print 'Maximum:', np.max(total_minutes)
#total_minutes = total_minutes_by_acct.values()
#describe_data(total_minutes)
