import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[25.58,-92.09], zoom_start=8, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, lg, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,lg], popup=str(el), icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Test.html")
