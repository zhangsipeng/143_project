import pandas as pd
import matplotlib.pyplot as plt


file_path = 'fd.xlsx'
df = pd.read_excel(file_path)


countries = df.iloc[:, 0].unique()  
years = df.iloc[:, 1].unique()      


plt.figure(figsize=(10, 6))

for country in countries:
    country_data = df[df.iloc[:, 0] == country]  
    fertility_data = country_data.iloc[:, 2]      
    plt.plot(years, fertility_data, label=country)

plt.title('Fertility Trend')
plt.xlabel('Year')
plt.ylabel('Fertility Rate')
plt.legend()
plt.grid(True)
plt.show()
