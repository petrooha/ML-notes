import logging
import sys
import string

from util import logfile

logging.basicConfig(filename=logfile, format='%(message)s',
                   level=logging.INFO, filemode='w')


def word_count():
    # For this exercise, write a program that serially counts the number of occurrences
    # of each word in the book Alice in Wonderland.
    #
    # The text of Alice in Wonderland will be fed into your program line-by-line.
    # Your program needs to take each line and do the following:
    # 1) Tokenize the line into string tokens by whitespace
    #    Example: "Hello, World!" should be converted into "Hello," and "World!"
    #    (This part has been done for you.)
    #
    # 2) Remove all punctuation
    #    Example: "Hello," and "World!" should be converted into "Hello" and "World"
    #
    # 3) Make all letters lowercase
    #    Example: "Hello" and "World" should be converted to "hello" and "world"


    word_counts = {}

    for line in sys.stdin:
        data = line.strip().split(" ")

    for i in data:
        key = i.translate(string.maketrans("",""),string.punctuation).lower()
        # remove punctuation and make all words lowercase
        if key in word_counts.keys():
            word_counts[key] +=1
        else:
            word_counts[key] = 1 #adds that word to dictionary and assigns value 1

            
