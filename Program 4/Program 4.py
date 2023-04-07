from statistics import correlation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

scores_df=pd.read_csv('scores.csv')
planets_df=pd.read_csv('planets.csv')


print('The max test score for Test 1: ' + str(scores_df['Test 1'].max()))
print('The max test score for Test 2: ' + str(scores_df['Test 2'].max()))
print('The max test score for Test 3: ' + str(scores_df['Test 3'].max()))
print('The max test score for Project: ' + str(scores_df['Project'].max()))
print('The min test score for Test 1: ' + str(scores_df['Test 1'].min()))
print('The min test score for Test 2: ' + str(scores_df['Test 2'].min()))
print('The min test score for Test 3: ' + str(scores_df['Test 3'].min()))
print('The min test score for Project: ' + str(scores_df['Project'].min()))
print('The range for Test 1: ' + str(scores_df['Test 1'].max() - scores_df['Test 1'].min() ))
print('The range for Test 2: ' + str(scores_df['Test 2'].max() - scores_df['Test 2'].min() ))
print('The range for Test 3: ' + str(scores_df['Test 3'].max() - scores_df['Test 3'].min() ))
print('The range for Project: ' + str(scores_df['Project'].max() - scores_df['Project'].min() ))
print('The mean for Test 1: ' + str(scores_df['Test 1'].mean()))
print('The mean for Test 2: ' + str(scores_df['Test 2'].mean()))
print('The mean for Test 3: ' + str(scores_df['Test 3'].mean()))
print('The mean for Project: ' + str(scores_df['Project'].mean()))
print('The variance for Test 1: ' + str(scores_df['Test 1'].var()))
print('The variance for Test 2: ' + str(scores_df['Test 2'].var()))
print('The variance for Test 3: ' + str(scores_df['Test 3'].var()))
print('The variance for Project: ' + str(scores_df['Project'].var()))
print('The standard deviation for Test 1: ' + str(scores_df['Test 1'].std()))
print('The standard deviation for Test 2: ' + str(scores_df['Test 2'].std()))
print('The standard deviation for Test 3: ' + str(scores_df['Test 3'].std()))
print('The standard deviation for Project: ' + str(scores_df['Project'].std()))

plt.boxplot(scores_df['Test 1'])
plt.show()

plt.boxplot(scores_df['Test 2'])
plt.show()

plt.boxplot(scores_df['Test 3'])
plt.show()

print('The corelation between Mass and Diameter: ' + str(correlation(planets_df['Mass'], planets_df['Diam'])))
print('The corelation between Distance and Temperature: ' + str(correlation(planets_df['Distance'], planets_df['Temp'])))
print('The corelation between Day and Period: ' + str(correlation(planets_df['Day'], planets_df['Period'])))
