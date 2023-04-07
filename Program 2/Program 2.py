import matplotlib.pyplot as plt
import pandas as pd

# bar chart showing the density of the planets
planets_df = pd.read_csv("planets.csv")
plt.title('Density of Planets')
plt.ylabel('Density')
plt.xlabel('Planets')
plt.bar(planets_df['Name'], planets_df['Density'])
plt.show()

# pie chart showing the percentage of planets with negative rotation values vs. positive rotation values
pos = planets_df['Rotation'].gt(0)
neg = planets_df['Rotation'].lt(0)
rotation = [pos.sum(), neg.sum()]
data = [pos.sum(), neg.sum()]
label = ['Positive Rotation', 'Negative Rotation']
plt.pie(data, labels=label, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()

# line chart with x-axis as planets and y-axis as the gravity
plt.title('Gravity of Planets')
plt.ylabel('Gravity')
plt.xlabel('Planets')
plt.plot(planets_df['Name'], planets_df['Grav'])
plt.show()

# bar chart showing distance of planets 
plt.title('Distance of Planets')
plt.ylabel('Distance')
plt.xlabel('Planets')
plt.bar(planets_df['Name'], planets_df['Distance'])
plt.show()

# read in the file into two lists
x = []
y = []
for line in open('5000_points.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(int(lines[0]))
    y.append(int(lines[1]))

# scatter graph to show all points
plt.figure(figsize=(12,5))
plt.scatter(x, y, color='green')
plt.title("x vs y")
plt.xlabel("X values for points")
plt.ylabel("Y values for points")
plt.xlim(min(x), max(x))
plt.ylim(min(y), max(y))
plt.show()

# scatter graph that shows points in even position with red color and points in odd position with green color
evenx = []
eveny = []
oddx = []
oddy = []

i = 0
for i in range(len(x)):
    if(i % 2 == 0):
        oddx.append(x[i])
    else:
        evenx.append(x[i])
    if(i % 2 == 0):
        oddy.append(y[i])
    else:
        eveny.append(y[i])
plt.scatter(evenx, eveny, color='red')
plt.scatter(oddx, oddy, color='green')
plt.show()


# bar chart comparing the number of points in these three groups (x < y, x == y, and x > y, where x and y are coordinates of a point.)
count_equal = 0
x_greater_than_y = 0
x_less_than_y = 0
for i in range(len(x)):
    if(x[i] > y[i]):
        x_greater_than_y +=1 
    if(x[i] < y[i]):
        x_less_than_y += 1
    if(x[i] == y[i]):
        count_equal += 1
names = ['X > y', 'X < Y', 'X = Y']
final_count = [x_greater_than_y, x_less_than_y, count_equal]
plt.title('Count for Comparison of Coordinates')
plt.ylabel('Count')
plt.xlabel('Comparisons')
plt.bar(names, final_count)
plt.show()

# pie chart to show the three group comparisons
plt.pie(final_count, labels=names, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()