import pandas as pd

df=pd.read_csv('./indicators.csv')
df=df.drop(columns=df.columns[3:])
col_country=df.loc[:,'Country']
col_country=col_country.drop_duplicates()
list_country=col_country.values.tolist()

col_years=df.loc[:,'Year']
col_years=col_years.drop_duplicates()
list_years=col_years.values.tolist()


data=[]
group=df.groupby('Country')
for item in list_country:
    col=group.get_group(item)
    col_GDP=col.loc[:,'GDP']
    data.append(col_GDP.values.tolist())


new_assembled_df=pd.DataFrame(data,index=col_country,columns=col_years)

new_assembled_df.to_csv("GDP_data.csv")
# print(new_assembled_df)

