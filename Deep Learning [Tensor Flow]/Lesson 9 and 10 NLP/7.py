import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import string
import numpy as np
import pandas as pd


# As noted above, we'll utilize the Song Lyrics dataset on Kaggle.
# I should try on my own Eminem lyrics https://www.kaggle.com/thaddeussegura/eminem-lyrics-from-all-albums

from urllib.request import urlopen

data = urlopen('https://storage.googleapis.com/kagglesdsdata/datasets/835677/1426970/eminem_lyrics/ALL_eminem.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20200924%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20200924T201536Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=9e8afd7dba5915b209e33905c68e93f2bfb1d3baac9456e1a0d16d1b74a0b482baa26bb6f348c2f901b46b63555b1a2bcc900c9db7d17321c27fe4578cc5d12463ca6b3e7c8998cf66a05a33b4b324dba3e48341d010f13a423debb8d1c2f52536870a9cc3ddfa72a4ca9bda874e934bcfdd21512e413e068bbd8c0a2a4042df66358d978080d164ead2f9e0edf1eee4bf66cf2f5c0aa63a5b7e9cea80ca6c211a0558aca9e7671235f105074f5f3f74abb882001acec29573c84b8ed9bf044b7233fb270a12fefe01bd40fe64b44cc0b89d54469357719d14404bb3c6033961c25af43c5c5f9c20fc090cf38fe03946058ecb9b67ebdfe4022c564480a2c73c').read().decode('utf-8')
print(data[:11])
print(len(data))

# split
text = data.split()
print(text[:10])

# remove puctuation, make all lowercase
dataset = []
import re
for s in text:
    s = re.sub(r'[^\w\s]','',s).lower()
    dataset.append(s)
print(dataset[:10])
print(len(dataset))

def tokenize_corpus(corpus, num_words=-1):
  # Fit a Tokenizer on the corpus
  if num_words > -1:
    tokenizer = Tokenizer(num_words=num_words)
  else:
    tokenizer = Tokenizer()
  tokenizer.fit_on_texts(corpus)
  return tokenizer

# Tokenize the corpus
tokenizer = tokenize_corpus(dataset)

total_words = len(tokenizer.word_index) + 1

print(tokenizer.word_index)
print(total_words)

token_list = tokenizer.texts_to_sequences(dataset[:10])



# get inputs and outputs
input_data = []
labels = []
for i in range(18):
    tokens = np.array(sum(tokenizer.texts_to_sequences(dataset[i:i+11]), []))
    input_data.append(tokens[:-1])
    labels.append(tokens[-1])


print(input_data)
print(labels)

# One-hot encode the labels
one_hot_labels = tf.keras.utils.to_categorical(labels, num_classes=total_words)
