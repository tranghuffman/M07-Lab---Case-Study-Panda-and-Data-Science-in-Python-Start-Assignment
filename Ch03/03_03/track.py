# %%
import pandas as pd

df = pd.read_csv(
    'track.csv',
    parse_dates=['time'],
    index_col='time',
)
# %%
import folium

center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(
    location=center,
    zoom_start=5,
)

loc = tuple(df.iloc[2][['latitude', 'longitude']])
marker = folium.Marker(loc)
marker.add_to(m)
m
# %%
m = folium.Map(
    location=center,
    zoom_start=5,
)
marker = folium.CircleMarker(
    loc,
    color= 'red')
marker.add_to(m)
m

# %%
m = folium.Map(
    location=center,
    zoom_start=5,
)
marker = folium.CircleMarker(
    loc,
    color= 'red',
    popup= 'Hi there',
)
marker.add_to(m)
m
# %%
m = folium.Map(
    location=center,
    zoom_start=5,
)

def add_marker(row):
    loc = tuple(row[['latitude', 'longitude']])
    marker = folium.CircleMarker(
        loc,
        color= 'red',
        popup= row.name.strftime('%H:%M'),
    )
    marker.add_to(m)

add_marker(df.iloc[2])
m
     
# %%
m = folium.Map(
    location=center,
    zoom_start=5,
)
df.apply(add_marker, axis=1)
m
# %%
m = folium.Map(
    location=center,
    zoom_start=5,
)
min_df = df.resample('min').mean()
min_df.apply(add_marker, axis=1)
m
# %%
