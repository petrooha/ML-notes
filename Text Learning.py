from nltk.stem.snowball import SnowballStemmer
import string

stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")
print stemmer.stem("responsivity")
print stemmer.stem("unresponsive")

#splitting text in words
ff = open("test_email.txt", "r")
all_text = ff.read()
print all_text
content = all_text.split()
print content


if len(content) > 1:
    ### remove punctuation
    text_string = list()
    for i in content:
        text_string.append(i.translate(string.maketrans("", ""), string.punctuation))
print text_string


#strip words to the roots
stemmer = SnowballStemmer("english")
string = list()
for l in text_string:
    string.append(stemmer.stem(l))
print string


#join list of words into one string
s = " "
s = s.join(string)
print s


#removing stopwords
from collections import Counter
from nltk.corpus import stopwords
sw = stopwords.words("english")
sw_dict = Counter(sw)
s = ' '.join([word for word in s.split() if word not in sw_dict])
#making sure they're all removed
if s.find(" there ") > -1 or s.find(" here ") > -1:
    print "STOPWORD"

#TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(word_data)
print X.shape
