# %%
import pandas as pd

csv_file = 'time.csv'
df = pd.read_csv(csv_file)
df.dtypes
# %%
df = pd.read_csv(csv_file, parse_dates=['12-Hour'])
df.dtypes
# %%
