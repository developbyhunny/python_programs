import pandas as pd

movies_data = pd.read_csv("C:\\users\\hunny\\desktop\\movies_data.csv")

c = 0
for i in range(len(movies_data.Name)):
    if movies_data.Rating[i] > 4:
        print(movies_data.Name[i])
        c = c + 1

print(c)

print(movies_data[movies_data['Rating'] > 4])

movies_data['Name']
print(movies_data[movies_data['year'] > 1950 and movies_data['year'] < 1960])

c = 0
for i in range(len(movies_data.Name)):
    if movies_data.year[i] > 1950 and movies_data.year[i] < 1960:
        print(movies_data.Name[i])
        c += 1

print(c)

for n in range(1950, 1961):
    print(movies_data[movies_data['year'] == n])
    c += 1

print(movies_data[movies_data['Duration'] > 7200 ])


c = 0
for i in range(len(movies_data.Name)):
    if movies_data.Rating[i] > 3 and movies_data.Rating[i] < 4:
        print(movies_data.Name[i])
        c += 1

print(c)

print(movies_data.year.sort())

df = pd.DataFrame(movies_data)
df.sort('Name','year')
df
data = list(movies_data.year)

print(movies_data.year)

sorted = movies_data.sort_values(["year"], ascending=False)
sorted

import string

for i in range(len(movies_data.Name)):
    if movies_data.Duration[i] is None:
        pass
    else:
        print(movies_data[i])
        







movies_data
pd.head(movies_data)

df = pd.DataFrame(movies_data)

