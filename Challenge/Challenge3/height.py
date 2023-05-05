# %%
import pandas as pd

df = pd.read_csv(
    'track.csv',
    parse_dates=['time'],
    index_col='time',
)
df = df.resample('min').mean()
# %%
import folium

m = folium.Map(
    location=[df['latitude'].mean(), df['longitude'].mean()],
    zoom_start=5,
)

def add_marker(row):
    loc = tuple(row[['latitude', 'longitude']])
    marker = folium.CircleMarker(
        loc,
        radius= 5,
        color= 'blue' if row['tp'] < 100 else 'red',
        popup= row.name.strftime('%H:%M'),
    )
    marker.add_to(m)

df.apply(add_marker, axis=1)
m

# %%
