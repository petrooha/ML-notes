import sys

def mapper():
    for line in sys.stdin: #cycle through lines of data

        #tokenize the line of data
        data = line.strip.split(" ")

        for i in data:
            #clean the data
            cleaned_data = i.translate(string.maketrans("",""), string.punctuation).lower()
            #emit a key-value pair
            print "{0}\t{1}".format(cleaned_data, 1)


def reducer():

    word_count = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t") #recall keys separated by a tab

        if len(data) != 2:
            continue #if we have a strange row with not just a key and a value

        this_key, count = data
        if old_key and old_key != this_key: #if we're not on the same key anymore
            print"{0\t{1}".format(old_key, word_count)
            word_count = 0

        old_key = this_key
        word_count +=float(count)
    if old_key != None: #word count for the last key value
        print "{0\t{1}".format(old_key, word_count)
