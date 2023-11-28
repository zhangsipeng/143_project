import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def remove_after_character(value, character=','):
    index = value.find(character)
    if index != -1:
        return value[:index]
    else:
        return value


dfFert = pd.read_csv('new_fert_data.csv')
dfGDP = pd.read_csv('GDP_data.csv')

x = dfGDP['Country'].tolist()
x = list(set(x))

y = dfFert['Country'].tolist()
#print(y)
#print(x)

fertlist = []
for i in y:
    i = i.split(',', 1)[0]
    fertlist.append(i)

#print(fertlist)
finalized_list = []
for i in fertlist:
    if i not in x:
        finalized_list.append(i)


dfFert = dfFert[~dfFert['Country'].isin(finalized_list)]
dfFert['Country'] = dfFert['Country'].apply(remove_after_character)
dfFert = dfFert.drop(columns=dfFert.columns[0:1])
dfFert = dfFert.sort_values(by='Country')

years = list(dfFert.columns[1:])

print(dfGDP)
print(dfFert)
count = 0
k = None
l = None



for index in range(len(dfFert['Country'])):
    value1 = dfFert['Country'].iloc[index]
    for i in range(len(dfGDP['Country'])):
        value2 = dfGDP['Country'].iloc[i]
        if value1 == value2:
            for j in range(1,28):

                k = float((dfFert.iloc[index, j]))
                l =float((dfGDP.iloc[i, j]))
                plt.subplot(9,3,j)
                plt.plot(k, l, color='blue', marker='o')

plt.show()

