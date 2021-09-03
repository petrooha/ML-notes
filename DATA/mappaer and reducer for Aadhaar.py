import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) != 12 or data[0] == 'Registrar':
            continue
        print "{0}\t{1}".format(data[3], data[8])

def reducer():
    count = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue
        this_key, n = data
        if old_key and old_key != this_key: #if we're not on the same key anymore
            print"{0}\t{1}".format(old_key, count)
            count = 0

        old_key = this_key
        count +=float(n)
    if old_key != None: #word count for the last key value
        print "{0}\t{1}".format(old_key, count)
