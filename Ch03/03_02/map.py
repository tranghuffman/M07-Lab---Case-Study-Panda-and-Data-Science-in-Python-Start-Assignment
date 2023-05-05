# %%
import pandas as pd

df = pd.read_csv(
    'track.csv',
    parse_dates=['time'],
    index_col='time',
)
df.columns
# %%
df.index[:5]
# %%
import folium

center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(
    location=center,
    zoom_start=5,
)
m
# %%
