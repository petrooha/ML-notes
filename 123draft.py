from nltk.corpus import stopwords
sw = stopwords.words("english")
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")
print stemmer.stem("responsivity")
print stemmer.stem("unresponsive")
