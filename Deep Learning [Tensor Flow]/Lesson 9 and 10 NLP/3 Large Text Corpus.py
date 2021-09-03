# dataset on Kaggle
"""https://www.kaggle.com/marklvl/sentiment-labelled-sentences-data-set"""

# Import Tokenizer and pad_sequences
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Import numpy and pandas
import numpy as np
import pandas as pd


# The combined dataset of reviews has been saved
# in a Google drive belonging to Udacity. You can download it from there.

path = tf.keras.utils.get_file('reviews.csv', 
                               'https://drive.google.com/uc?id=13ySLC_ue6Umt9RJYSeM2t-V0kCv-4C-P')
print (path)

"""
Each row in the csv file is a separate review.

The csv file has 2 columns:

text (the review)
sentiment (0 or 1 indicating a bad or good review)
"""

# Read the csv file
dataset = pd.read_csv(path)

# Review the first few entries in the dataset
dataset.head()

# Get the reviews from the text column
reviews = dataset['text'].tolist()



# Tokenize
#################

tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(reviews)

word_index = tokenizer.word_index
print(len(word_index))
print(word_index)



# Generate Sequences
#####################

sequences = tokenizer.texts_to_sequences(reviews)
padded_sequences = pad_sequences(sequences, padding='post')

# What is the shape of the vector containing the padded sequences?
# The shape shows the number of sequences and the length of each one.
print(padded_sequences.shape)

# What is the first review?
print (reviews[0])

# Show the sequence for the first review
print(padded_sequences[0])


