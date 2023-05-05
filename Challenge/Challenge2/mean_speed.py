# %%
import pandas as pd

df = pd.read_parquet('taxi.parquet')

# %%
mask = df['Latest tpep_pickup'] > df['Earliest tpep_pickup']
df = df[mask]
# %%
times = df['Latest tpep_pickup'] - df['Earliest tpep_pickup']
times_hour = times / pd.Timedelta(1, 'hour')
speed = df['trip_distance'] / times_hour
# %%
