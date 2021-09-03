
## Import the Tokenizer


# Import the Tokenizer
from tensorflow.keras.preprocessing.text import Tokenizer



## Write some sentences
sentences = [
    'My favorite food is ice cream',
    'do you like ice cream too?',
    'My dog likes ice cream!',
    "your favorite flavor of icecream is chocolate",
    "chocolate isn't good for dogs",
    "your dog, your cat, and your parrot prefer broccoli"
]

## Tokenize the words

# Optionally set the max number of words to tokenize.
# The out of vocabulary (OOV) token represents words that are not in the index.
# Call fit_on_text() on the tokenizer to generate unique numbers for each word

tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)



## View the word index
"""
After you tokenize the text, the tokenizer has
a word index that contains key-value pairs for all
the words and their numbers.

The word is the key, and the number is the value.
Notice that the OOV token is the first entry.
"""

# Examine the word index
word_index = tokenizer.word_index
print(word_index)

# Get the number for a given word
print(word_index['favorite'])



# Create sequences for the sentences
"""
After you tokenize the words, the word index contains
a unique number for each word. However, the numbers in
the word index are not ordered. Words in a sentence have
an order. So after tokenizing the words, the next step
is to generate sequences for the sentences.
"""

sequences = tokenizer.texts_to_sequences(sentences)
print (sequences)



# Sequence sentences that contain words that are not in the word index
"""
Let's take a look at what happens if the sentence being sequenced contains words that are not in the word index.

The Out of Vocabluary (OOV) token is the first entry in
the word index. You will see it shows up in the sequences
in place of any word that is not in the word index.
"""

sentences2 = ["I like hot chocolate", "My dogs and my hedgehog like kibble but my squirrel prefers grapes and my chickens like ice cream, preferably vanilla"]

sequences2 = tokenizer.texts_to_sequences(sentences2)
print(sequences2)

