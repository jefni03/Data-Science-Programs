from pandas import Series, DataFrame
import pandas as pd
import json
import numpy as np
import sqlite3

# Task 1
df = pd.read_csv('scores.csv')
grade = pd.DataFrame(df)

grade['Total Grade'] = np.round((((grade['Test 1'] / 100) * .20) + ((grade['Test 2'] / 100) * .20) + ((grade['Test 3'] / 100) * .20) + ((grade['Project'] / 100) * .40)) * 100, decimals=2)

x = []
for i in grade['Total Grade']:
    if i > 90:
        i = 'A'
    elif 80 < i or i > 90:
        i = 'B'
    else:
        i = 'C'
    x.append(i)


grade['Letter Grade'] = x

CSVgrade = grade.to_csv('grades.csv', index = False)

# Task 2
list = []
with open('names.txt', 'r') as file:
    for space in file:
        new = space.split()
        list.append(new)

var = [item for element in list for item in element]

gpa = np.round(np.random.uniform(low = 2.0, high = 4.0, size= len(var)), 2)


major = np.random.choice(['CS', 'BIO', 'CHEM', 'MATH'], len(var))
column = {'StudentNAMES': var, 'GPA': gpa, 'Major': major}
sf = pd.DataFrame(data = column)

csvv = sf.to_csv('profile.csv', index = False)
jsonv = sf.to_json(orient ='split', index=False)

temp = json.loads(jsonv)

with open('profile.json', 'w') as f:
    new = json.dump(temp, f, indent = 2)

# Task 3
con = sqlite3.connect('database.db')
cursor = con.cursor()

# a
gradesdb = cursor.execute("CREATE TABLE grades(Name text, Test_1 int, Test_2 int, Test_3 int, Project int, Total_Grade int, Letter_Grade text)")

cursor.execute("CREATE TABLE profile(studentNAMES text, GPA int, Major text)")

with open('grades.csv', 'r') as f:
    for i in f:
        cursor.execute("INSERT INTO grades  VALUES (?,?,?,?,?,?,?)", i.split(','))
        con.commit()

with open('profile.csv', 'r') as l:
    for i in l:
        cursor.execute("INSERT INTO profile  VALUES (?,?,?)", i.split(','))
        con.commit()

#b
cursor.execute("SELECT * FROM grades WHERE Name=?", ('Mateo',))
result = cursor.fetchall()
for row in result:
    print(row)

#c 
cursor.execute('''UPDATE profile SET Major = 'CS' WHERE StudentNAMES='Mateo';''')
result = cursor.fetchall()
for row in result:
    print(row)

# d
cursorS = con.execute("SELECT , StudentNAMES, GPA, Major from profile") 
print('Students with more than 3.5:')
for row in cursorS:
    print ("Name = ", row[0] > 3.5)

# e
cursorS = con.execute('INSERT INTO profile  (StudentNAMES, GPA, Major) VALUES (3.2, 'Mateo', 'CS')')
