# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

d = [q["properties"]["type"] for q in data["features"]]
msg = collections.Counter(d)

for x in msg.keys():
    print(f'{x:15}: ',msg[x])



total = defaultdict(int)
for types in data["features"]:
    total[types["properties"]["type"]] += 1

for x,y in total.items():
    print(f'{x:15}: {y}')