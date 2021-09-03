import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import pandas as pd
import tensorflow_datasets as tfds


path = tf.keras.utils.get_file('reviews.csv', 
                               'https://drive.google.com/uc?id=13ySLC_ue6Umt9RJYSeM2t-V0kCv-4C-P')
dataset = pd.read_csv(path)

# Some fake reviews  
fake_reviews = ["I love this phone", 
                "Everything was cold",
                "Everything was hot exactly as I wanted", 
                "Everything was green", 
                "the host seated us immediately",
                "they gave us free chocolate cake", 
                "we couldn't hear each other talk because of the shouting in the kitchen"
              ]


sentences = dataset['text'].tolist()
labels = dataset['sentiment'].tolist()

# Print some example sentences and labels
for x in range(2):
  print(sentences[x])
  print(labels[x])
  print("\n")


vocab_size = 1000
tokenizer = tfds.features.text.SubwordTextEncoder.build_from_corpus(sentences, vocab_size,
                                                               max_subword_length=5)
# How big is the vocab size?
print("Vocab size is ", tokenizer.vocab_size)

# Check that the tokenizer works appropriately
num = 5
print(sentences[num])
encoded = tokenizer.encode(sentences[num])
print(encoded)


# Separately print each subword, decoded
for i in encoded:
    print(tokenizer.decode([i]))


## Replace sentence data with encoded subwords
# same as **text_to_sequences** from previous exercises
for i, sentence in enumerate(sentences):
    sentences[i] = tokenizer.encode(sentence)

# Check the sentences are appropriately replaced
print(sentences[5])



# Final preprocessing (padding, truncating, test split)
max_length = 50
trunc_type = 'post'
padding_type = 'post'

# Pad
sequences_padded = pad_sequences(sentences, maxlen=max_length,
                                 padding=padding_type, truncating=trunc_type)

# Train / test
training_size = int(len(sentences) * 0.8)

train_seq = sequences_padded[0:training_size]
test_seq = sequences_padded[training_size:]
train_labels = np.array(labels[0:training_size])
test_labels = np.array(labels[training_size:])







#####     FUNCTIONS:

# Define a function to take a series of reviews
# and predict whether each one is a positive or negative review

num_epochs = 10

def predict_review(model, new_sentences, maxlen=max_length, show_padded_sequence=True):
    new_sequences = []

    # convert new reviews to sequences
    for i, frvw in enumerate(new_sentences):
        new_sequences.append(tokenizer.encode(frvw))

    # Pad new reviews
    new_padded = pad_sequences(new_sequences, maxlen=max_length,
                               padding=padding_type, truncating=trunc_type)

    classes = model.predict(new_padded)
    # The closer class to 1 the more positive the review

    # we can see padded sequence if desired
    for x in range(len(new_sentences)):
        if (show_padded_sequence):
            print(new_padded[x])
        # print review as text
        print(new_sentences[x])
        # print its predicted class
        print(classes[x])
        print("\n")



# Graph Function
import matplotlib.pyplot as plt


def plot_graphs(history, string):
  plt.plot(history.history[string])
  plt.plot(history.history['val_'+string])
  plt.xlabel("Epochs")
  plt.ylabel(string)
  plt.legend([string, 'val_'+string])
  plt.show()



# Function to train, show graphs, make predictions of different models

def fit_model_now(model, sentences):
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    history = model.fit(train_seq, train_labels, epochs=num_epochs,
                        validation_data=(test_seq, test_labels))
    return history

def plot_results(history):
    plot_graphs(history, "accuracy")
    plot_graphs(history, "loss")

def fit_model_and_show_results(model, sentences):
    history = fit_model_now(model, sentences)
    plot_results(history)
    predict_review(model, sentences)





# Define the model
embedding_dim = 16

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(), 
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile and train the model and then show the predictions for our extra sentences
fit_model_and_show_results(model, fake_reviews)

###########################


# Another one with Bidirectional LSTM
model_bidi_lstm = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim)), 
    tf.keras.layers.Dense(6, activation='relu'), 
    tf.keras.layers.Dense(1, activation='sigmoid')
])

fit_model_and_show_results(model_bidi_lstm, fake_reviews)

##############################


# Another one
model_multiple_bidi_lstm = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim, 
                                                       return_sequences=True)), 
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(embedding_dim)),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

fit_model_and_show_results(model_multiple_bidi_lstm, fake_reviews)


