#!/usr/bin/python

import os
import pickle
import re
import sys
import string
from nltk.stem.snowball import SnowballStemmer
sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText
from collections import Counter
from nltk.corpus import stopwords
sw = stopwords.words("english")
sw_dict = Counter(sw)

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter < 201:
            path = os.path.join('..', '..', path[:-1])
            #print path
            email = open(path, "r")
            text = email.read()
            text = text[text.find("X-FileName")+9:]
            
            content = text.split()
            if len(content) > 1:
                st = list()
                for i in content:
                    st.append(i.translate(string.maketrans("", ""), string.punctuation))
            stemmer = SnowballStemmer("english")
            text = list()
            for l in st:
                text.append(stemmer.stem(l))
            s = " "
            s = s.join(text)
            if s.find('xfrom sara shackleton') > 0 or s.find('xfrom shackleton sara') > 0:
                from_data.append(0)
            else:
                from_data.append(1)
            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            s = s.replace("sara", "")
            s = s.replace("shackleton", "")
            s = s.replace("chris", "")
            s = s.replace("germani", "")
            s = ' '.join([word for word in s.split() if word not in sw_dict])
            ### append the text to word_data
            if s.find(" there ") > -1 or s.find(" here ") > -1:
                print "theres one!", s
                break
            word_data.append(s)
            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris


            email.close()

print "emails processed"


from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )


### in Part 4, do TfIdf vectorization here

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(word_data)

print X.shape



from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


clf = DecisionTreeClassifier(min_samples_split = 40)

clf.fit(X, from_data)
pred = clf.predict(X)


print max(clf.feature_importances_)
