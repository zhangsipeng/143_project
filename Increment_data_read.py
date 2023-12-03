import pandas as pd

df=pd.read_csv('./indicators.csv')

# df=df.drop(columns=df.columns[4:])
col_country=df.loc[:,'Country']
col_country=col_country.drop_duplicates()
list_country=col_country.values.tolist()

col_years=df.loc[:,'Year']
col_years=col_years.drop_duplicates()
list_years=col_years.values.tolist()
list_years=list_years[0:-1]
list_years.append('Country Name')


data=[]
group=df.groupby('Country')
for item in list_country:
    col=group.get_group(item)
    col_GDP=col.loc[:,'GDP Per Capita']
    lst=col_GDP.values.tolist()
    
    increment_list=[]
    for i in range(len(lst)-1):
        increment_list.append((lst[i+1]-lst[i])/lst[i])

    col_fertile=col.loc[:,'Fertility rate, total (births per woman)']
    lst=col_fertile.values.tolist()
    fertile_incre_list=[]
    for i in range(len(lst)-1):
        fertile_incre_list.append((lst[i+1]-lst[i])/lst[i])

    ratio=[]
    for i in range(len(increment_list)):
        ratio.append(fertile_incre_list[i]/increment_list[i])
    ratio.append(item)
    data.append(ratio)


new_assembled_df=pd.DataFrame(data,index=list_country,columns=list_years)

new_assembled_df.to_csv("Fertile_ratio.csv")
print(new_assembled_df)