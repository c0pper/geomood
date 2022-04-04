import folium
import pandas as pd
import pickle
df = pd.read_csv("geomood.csv")

m = folium.Map(location=[40.8312592, 14.244409])

for e in df.iterrows():
    lat = e[1]["lat"]
    lon = e[1]["lon"]
    adr = e[1]["adr"]
    name = str(e[1]["name"])
    date = e[1]["mood_date"]
    mood = e[1]["mood"].capitalize()
    popup = folium.Popup(f"<b><p>{name}</p></b>\n<i><p>{adr}</p></i>\n<p>{date}</p>\n<p>{mood}</p></i>", max_width=300,
                         min_width=300)
    tooltip = f"<b><p>{name}</p></b>\n<p>{mood}</p>"
    if mood == "Rad":
        folium.Marker(
            [lat, lon], popup=popup, tooltip=tooltip, icon=folium.Icon(color="orange")
        ).add_to(m)
    elif mood == "Good":
        folium.Marker(
            [lat, lon], popup=popup, tooltip=tooltip, icon=folium.Icon(color="green")
        ).add_to(m)
    elif mood == "Meh":
        folium.Marker(
            [lat, lon], popup=popup, tooltip=tooltip, icon=folium.Icon(color="purple")
        ).add_to(m)
    elif mood == "Bad":
        folium.Marker(
            [lat, lon], popup=popup, tooltip=tooltip, icon=folium.Icon(color="blue")
        ).add_to(m)
    else:
        folium.Marker(
            [lat, lon], popup=popup, tooltip=tooltip, icon=folium.Icon(color="gray")
        ).add_to(m)

pickle.dump(m, open('map.pkl', 'wb'))
