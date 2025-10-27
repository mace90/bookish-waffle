import pandas as pd
import requests
from io import StringIO

import plotly.graph_objects as go


url_airport = "https://raw.githubusercontent.com/jpatokal/openflights/refs/heads/master/data/airports.dat"
url_routes = "https://raw.githubusercontent.com/jpatokal/openflights/refs/heads/master/data/routes.dat"
response_airport = requests.get(url_airport).text
routes = requests.get(url_routes).text

columns = [
    "Airport ID", "Name", "City", "Country", "IATA", "ICAO",
    "Latitude", "Longitude", "Altitude", "Timezone", "DST",
    "Tz database timezone", "Type", "Source"
]
columns2 = [
    "Airline", "Airline ID", "Source airport", "Source airport ID", "Destination airport", "Destination airport ID",
    "Codeshare", "Stops", "Equipment"
]

csv_like = StringIO(response_airport)
df = pd.read_csv(csv_like,header=None, names=columns)
print(df.head())
csv_like_2 = StringIO(routes)
df2 = pd.read_csv(csv_like_2,header=None, names=columns2)
print(df2.head())





import plotly.graph_objects as go

#Filter Flughäfen nach Land
df_selected = df[df["Country"].isin(["Germany"])]
#df_selected = df[df["Country"].isin(["Germany", "France"])]


df2["Source airport ID"] = df2["Source airport ID"].astype(str)
df2["Destination airport ID"] = df2["Destination airport ID"].astype(str)
df_selected["Airport ID"] = df_selected["Airport ID"].astype(str)

routes_selected = df2[
    df2["Source airport ID"].isin(df_selected["Airport ID"]) &
    df2["Destination airport ID"].isin(df_selected["Airport ID"])]

routes_coords = routes_selected.merge(df_selected, left_on="Source airport ID", right_on="Airport ID")
routes_coords = routes_coords.merge(df_selected, left_on="Destination airport ID", right_on="Airport ID", suffixes=("_source", "_dest"))


fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lon = df_selected["Longitude"],
    lat = df_selected["Latitude"],
    text = df_selected["Name"],
    mode = "markers",
    marker = dict(size=4, color="blue"),
    name = "Airports"
))

for _, row in routes_coords.iterrows():
    fig.add_trace(go.Scattergeo(
        lon = [row["Longitude_source"], row["Longitude_dest"]],
        lat = [row["Latitude_source"], row["Latitude_dest"]],
        mode = "lines",
        line = dict(width=1, color="red"),
        opacity = 0.5,
        showlegend=False
    ))

fig.update_layout(
    title_text = "Flugrouten innerhalb Deutschlands (OpenFlights)",
    geo = dict(
        scope="europe",
        projection_type="mercator",
        showland=True,
        landcolor="rgb(243, 243, 243)",
        countrycolor="rgb(204, 204, 204)",
        center=dict(lat=51.1657, lon=10.4515),
        lataxis=dict(range=[47, 56]),
        lonaxis=dict(range=[5, 16])
    ),
    height=700
)

fig.show()

