import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statistics

# Question 23
# hexbin plot
df = pd.DataFrame(np.random.randn(1000, 2), columns = ['a', 'b'])
df['b'] = df['b'] + np.arange(1000)
df.plot.hexbin(x = 'a', y = 'b', gridsize = 25)
plt.show()

# stacked bar plot
df2 = pd.DataFrame(np.random.rand(10, 4), columns = ['a', 'b', 'c', 'd'])
df2.plot.bar(stacked = True)
plt.show()

# pie plot
series = pd.Series(3 * np.random.rand(4), index = ['a', 'b', 'c', 'd'], name = 'series')
series.plot.pie(figsize = (6,6))
plt.show()

# area plot 
df = pd.DataFrame(np.random.rand(10, 4), columns = ['a', 'b', 'c', 'd'])
df.plot.area()
plt.show()

# scatter plot
df = pd.DataFrame(np.random.rand(50, 4), columns = ['a', 'b', 'c', 'd'])
df.plot.scatter(x = 'a', y = 'b')
plt.show()

# box plot
df = pd.DataFrame(np.random.rand(10, 5), columns = ['A', 'B', 'C', 'D', 'E'])
df.plot.box()
plt.show()

# plot with data from 3 columns
df = pd.DataFrame(3 * np.random.rand(4, 3), index = ['a', 'b', 'c', 'd'], columns = ['x', 'y', 'z'])
df.plot.pie(subplots = True, figsize = (8, 4))
plt.show()

# customized box plot: must change the whiskers and caps 
df = pd.DataFrame(np.random.rand(10, 5), columns = ['A', 'B', 'C', 'D', 'E'])
color = {'boxes': 'DarkRed', 'whiskers': 'DarkOrange', 'medians': 'DarkGreen', 'caps': 'Green'}
df.plot.box(color = color, sym = 'r+')
plt.show()


# Question 24

data = [32, 13, 19, 37, 27, 22, 20, 87, 42, 14, 26, 28, 35, 31, 10]
plt.boxplot(data, vert = 0)
plt.show()
print('Mean: ' + str(statistics.mean(data)))
print('Median: ' + str(statistics.median(data)))
print('Cut points for 8 quantiles: ' + str(statistics.quantiles(data, n = 8)))
q1, q3 = np.percentile(data, [25 , 75])
q1 = int(q1)
q3 = int(q3)
print('Quartile 1: ' + str(q1))
print('Quartile 3: ' + str(q3))
iqr = q3 - q1
print('IQR: ' + str(iqr))
print('Lower Bound for Outliers: ' + str(q1 - (1.5 * iqr)))
print('Upper Bound for Outliers: ' + str(q3 + (1.5 * iqr)))