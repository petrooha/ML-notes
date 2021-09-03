# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        header = f.readline().split(",") #read the 1st line and use "," as delimiter, giving list of values that we can use as keys
        counter = 0
        for line in f:
            if counter == 10:
                break
            fields = line.split(",") # giving values for each line after header (within the loop)
            entry = {}

            for i, value in enumerate(fields): #gives index for each value and the value for each item in the fields list (line in the loop)
                entry[header[i].strip()] = value.strip() #then we assign them with values' indexes from header, stripping both off of extra whitespace

            data.append(entry)
            counter+=1
        return data

#### OR a shorter way, dealing with quotes, commas, etc (excluding counter ==10):
import csv
def parse_csv(datafile):
    data = []
    n=0
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)# reads csv into dictionary assuming 1st row to be the header
        for line in r:
            data.append(line)
    return data

