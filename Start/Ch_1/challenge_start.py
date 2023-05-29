# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1: How many quakes are there in total?
print(f'Total no. of earthquakes is: {len(data["features"])}')

# 2: How many quakes were felt by at least 100 people?
def quakes100(q):
    return q["properties"]["felt"] is not None and q["properties"]["felt"] >= 100

quake100count = list(filter(quakes100, data["features"]))
print(f'Total quakes felt by atleast 100 people: {len(quake100count)}')


# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def max_felt(q):
    if q["properties"]["felt"] is not None:
        return q["properties"]["felt"]
    else:
        return 0

maxfelt = max(data["features"], key=max_felt)
print(f'Place whose quake was felt by the most people: {maxfelt["properties"]["title"]}, felt by {maxfelt["properties"]["felt"]} people')


# 4: Print the top 10 most significant events, with the significance value of each   
def max_sig(q):
    if q["properties"]["sig"] is not None:
        return float(q["properties"]["sig"])
    else:
        return 0

data["features"].sort(key=max_sig, reverse=True)

for i in range(10):
    print(f'Event: {data["features"][i]["properties"]["title"]}, Significance: {data["features"][i]["properties"]["sig"]}')