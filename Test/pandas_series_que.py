import pandas as pd
import numpy as np

# Creating a Series from a list
data = [60, 20, 10, 40, 50]
series = pd.Series(data)

# print(series)
# print(series[2])
# print(series[3:])
# print(series[series>=20])
op = series.apply(lambda x : x*2)
print(op)

# data = [1, np.nan, 3, np.nan, 5]
# series = pd.Series(data)

# print(series.isnull())
# print("----------------")
# clean_series = series.dropna()
# print(clean_series)


# import pandas as pd

# data1 = [1, 2, 3, 4, 5]
# data2 = [10, 20, 30, 40, 50]
# series1 = pd.Series(data1)
# series2 = pd.Series(data2)

# # Adding two Series
# sum_series = series1 + series2
# print(sum_series)

# # Finding the mean
# mean_value = series1.mean()
# print(mean_value)


