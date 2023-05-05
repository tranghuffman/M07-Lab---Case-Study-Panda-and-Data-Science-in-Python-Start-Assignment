# %%
import pandas as pd

df = pd.read_csv('people.csv', parse_dates=['Date of birth'])

# %%
df['Index']
# %%
df.Index
# %%
df[['Index', 'User Id']]

# %%
df['Index'][0]
# %%
df.loc[0]
# %%
df.loc[2:7]
# %%
df[['Index', 'User Id']][2:7]
# %%
df.index
# %%
import numpy as np

df1 = pd.DataFrame(
    np.arange(10).reshape(5, 2),
    columns = ['x', 'y'],
    index = ['a', 'b', 'c', 'd', 'e']
)
df1
# %%
df1.loc['a']
# %%
df1.loc['a':'d']
# %%
df1.iloc[0]
# %%
df.index
# %%
df.index = df['Index']
df.index
# %%
df.loc[0]
# %%
