import pandas as pd

engagements = pd.read_csv('daily_engagement.csv')
print len(engagements['acct'].unique())
