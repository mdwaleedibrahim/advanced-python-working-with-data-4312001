# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []
with open('../../5magquakes.csv', 'r') as f:
    data = f.readlines()

# TODO: open the CSV file for reading


pprint.pp(data)
