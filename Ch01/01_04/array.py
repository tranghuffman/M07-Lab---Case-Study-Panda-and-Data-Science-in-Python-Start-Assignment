# %%
import numpy as np

# %%
arr = np.array([1, 2, 3])
arr
# %%
len(arr)
# %%
arr[1]
# %%
type(arr[1])
# %%
arr.dtype
# %%
arr32 = np.array([1, 2, 3], dtype = np.int32)
arr32.dtype
# %%
arr * arr
# %%
v1 = np.random.rand(1_000_000)
v2 = np.random.rand(1_000_000)
%time v1 * v2
# %%
arr @ arr
# %%
