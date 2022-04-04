import os
import json
import pandas as pd
import numpy as np

path = "SemanticLocationHistory"
file_paths = []

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        file_paths.append(os.path.join(root, name))

place_visits = []


def get_visits_from_files_in_folders(file_path):
    f = open(file_path, encoding="utf-8")
    data = json.load(f)
    for i in data["timelineObjects"]:
        try:
            lat = i["placeVisit"]["location"]["latitudeE7"]
            lon = i["placeVisit"]["location"]["longitudeE7"]
            adr = i["placeVisit"]["location"]["address"]
            name = i["placeVisit"]["location"]["name"]
            start_time = i["placeVisit"]["duration"]["startTimestamp"]
            end_time = i["placeVisit"]["duration"]["endTimestamp"]
            print(adr)
            place_visits.append((lat, lon, adr.replace('\n', " "),
                                 name.replace('\n', " "), start_time, end_time))
        except KeyError:
            pass


for p in file_paths:
    get_visits_from_files_in_folders(p)

df = pd.DataFrame(place_visits, columns=["lat", "lon", "adr", "name", "start_t", "end_t"])
df["mood_date"] = df["start_t"].str[:10]
mood_df = pd.read_csv("mood.csv")[["full_date", "mood"]]
mood_df = mood_df.iloc[::-1]



def testf(x):
    col = mood_df.loc[mood_df['full_date'] == x]
    mood = col["mood"].values[0]
    return mood

df["lat"] = df["lat"].apply(lambda x: x/10000000)
df["lon"] = df["lon"].apply(lambda x: x/10000000)
df["mood"] = df["mood_date"].apply(testf)

df.to_csv("geomood.csv", index=False)
