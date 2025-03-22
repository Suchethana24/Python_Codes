import pandas as pd
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
series = pd.Series(data)
print(series)
# print(type(series))
series = pd.Series(data, index=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
print(series)
