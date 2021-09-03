# Import Tokenizer and pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


sentences = [
    'My favorite food is ice cream',
    'do you like ice cream too?',
    'My dog likes ice cream!',
    "your favorite flavor of icecream is chocolate",
    "chocolate isn't good for dogs",
    "your dog, your cat, and your parrot prefer broccoli"
]
print("\nSentances: ", sentences)


tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")

# Tokenize the words
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print("\nWord Indexes: ", word_index)

# Turn sentences into sequences
sequences = tokenizer.texts_to_sequences(sentences)
print ("\nSequences: ", sequences)



##### PADDING


# For all the options when padding and truncating sequences, see
"""
https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/pad_sequences
"""


# Make the sequences all the same length
padded = pad_sequences(sequences)

print("\nPadded Sequences:")
print(padded)


# Specify a max length for the padded sequences
padded = pad_sequences(sequences, maxlen=15)
print("\nPadded 'maxlen=15'\n", padded)

# Put the padding at the end of the sequences
padded = pad_sequences(sequences, maxlen=15, padding="post")
print("\nPadded 'maxlen=15' and 'padding=post'\n", padded)

# Limit the length of the sequences, you will see some sequences get truncated
padded = pad_sequences(sequences, maxlen=3)
print("\nPadded 'maxlen=3'\n", padded)



# What happens if some of the sentences contain words that are not in the word index?


# Try turning sentences that contain words that 
# aren't in the word index into sequences.
# Add your own sentences to the test_data
test_data = [
    "my best friend's favorite ice cream flavor is strawberry",
    "my dog's best friend is a manatee"
]
print ("\nTest Sentances: ", test_data)

# Remind ourselves which number corresponds to the
# out of vocabulary token in the word index
print("<OOV> has the number", word_index['<OOV>'], "in the word index.")

# Convert the test sentences to sequences
test_seq = tokenizer.texts_to_sequences(test_data)
print("\nTest Sequence = ", test_seq)

# Pad the new sequences
padded = pad_sequences(test_seq, maxlen=10)
print("\nPadded Test Sequence: ")

# Notice that "1" appears in the sequence wherever there's a word 
# that's not in the word index
print(padded)
