import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

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

#print(dfGDP)
#print(dfFert)

k = None
l = None

all_fert_vals = []
all_GDP_vals = []

for index in range(len(dfFert['Country'])):
    value1 = dfFert['Country'].iloc[index]
    for i in range(len(dfGDP['Country'])):
        value2 = dfGDP['Country'].iloc[i]
        if value1 == value2:
            for j in range(1,28):

                k = float((dfFert.iloc[index, j]))
                l =float((dfGDP.iloc[i, j]))
                all_fert_vals.append(k)
                all_GDP_vals.append(l)
                plt.figure(1, figsize=(12,8))
         
                plt.subplot(9,3,j)
                plt.title(f"{1989 + j}") 
                plt.plot(k, l, color='blue', marker='o')
                plt.subplots_adjust(hspace=0.95, wspace=0.5)
                plt.suptitle('Scatterplots of Fertility vs GDP per Capita from 1990-2016')

plt.figure(2)
afvnp = np.array(all_fert_vals)
agvnp = np.array(all_GDP_vals)
plt.scatter(afvnp, agvnp, color='blue', label = 'Fertility Rate against GDP/Capita', marker='o')
afvnp[np.isnan(afvnp)] = 0
agvnp[np.isnan(agvnp)] = 0

            
mask = (afvnp != 0) & (agvnp != 0)
filtered_array1 = afvnp[mask]
filtered_array2 = agvnp[mask]

def exp_func(x, a, b):
    return a * np.exp(b * x)

params, covariance = curve_fit(exp_func, filtered_array1, filtered_array2)
a, b = params

x_fit = np.linspace(min(filtered_array1), max(filtered_array1), 100)
y_fit = exp_func(x_fit, a, b)




plt.plot(x_fit, y_fit, 'r-', label = "Exponential Regression: 62430*-0.714^x", linewidth=2)
plt.legend()
plt.xlabel("Fertility Rate")
plt.ylabel("GDP per Capita")
plt.title('Exponential Regression For All Data Points from 1990-2016')
    
plt.show()



