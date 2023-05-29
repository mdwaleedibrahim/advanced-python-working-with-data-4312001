# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value


# TODO: The max() function finds the maximum value


# TODO: define a custom "key" function to extract a data field
print(f"Maximum field is : {max(strings, key=len)}")

# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(data['metadata']['title'])
print(f"No. of records: ", len(data['features']))

# Min. earthquake magnitude
print(data['features'][2])
min([float(x['properties']['mag']) for x in data['features'] if x['properties']['mag'] != None])

# Max earthquake magnitude