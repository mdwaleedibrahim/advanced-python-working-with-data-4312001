# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime as dt

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent

def getSig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig

significantData = sorted(data["features"], key=getSig, reverse=True)
significantData = significantData[:40]
significantData.sort(key=lambda x: x["properties"]["time"], reverse=True)

# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
Header = ["Magnitude" , "Place", "FeltReports", "Date", "GoogleMaplink"]

rows = []
for event in significantData:
    Magnitude = event["properties"]["mag"]
    Place = event["properties"]["place"]
    FeltReports = 0 if event["properties"]["felt"] is None else event["properties"]["felt"]
    Date = dt.date.fromtimestamp(int(event["properties"]["time"]) / 1000)
    latlong = event["geometry"]["coordinates"]
    GoogleMaplink= f"https://maps.google.com/?q={latlong[1]},{latlong[0]}"
    rows.append([Magnitude, Place, FeltReports, str(Date), GoogleMaplink])
 
# Date should be in the format of YYYY-MM-DD

with open('40sig.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(Header)
    writer.writerows(rows)

