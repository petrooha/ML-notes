    #  I gotta make a dict with field names as keys and list of types of data for each column 
 
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def is_int(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def is_float(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

def audit_file(filename, fields):
    fieldtypes = {}
    
    file1 = open(filename, 'rb')
    reader = csv.DictReader(file1)
    
    next(reader)
    next(reader)
    next(reader)

    for e in fields:
        d=set()
        fieldtypes[e] = d
        for row in reader:
            if row[e] == "NULL":
                d.add(type(None))

            elif row[e] == "":
                d.add(type(None))

            elif str(row[e]).find("{") == 0:
                d.add(type([]))

            elif is_int(row[e]):
                d.add(type(int()))

            elif is_float(row[e]):
                d.add(type(1.1))
            else:
                d.add(type(str()))
               

    return fieldtypes
