# using list
import pandas as pd
data = [1, 2, 3, 4, 5]
data_1 = pd.DataFrame(data)
print(data_1)
print("=======================")

# using dictionary
dataset = {"Name":["suchi", "akhi", "pooji", "rohi", "hruthi"], "Age":[20, 21, 20, 22, 21]}
print(pd.DataFrame(dataset))
print("=======================")

# using series
series = pd.Series([6, 12, 13],index=["a","b","c"])
df = pd.DataFrame(series)
print(df)
print("=====================")

# using numpy
import  numpy as np
import  pandas as pd
numpy_array = np.array([[50000, 30000, 20000, 10000],["suchi","akhi","rohi","pooji"]])
df = pd.DataFrame({"name":numpy_array[1], "salary":numpy_array[0]})
print(df)