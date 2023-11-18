import pandas as pd

def fertility_data_read(x):

    assert isinstance(x, pd.DataFrame)
    #asserting argument is a dataframe
    x = x.drop(columns=x.columns[2:32])
    x = x.drop(columns=x.columns[28:])
    #the first drop statement drops years 1960 to 1989, second drop statment takes out 2015 to 2022
    return x
    
#if __name__ == '__main__':

 #   df = pd.read_csv('fert_data.csv')
  #  print(fertility_data_read(df))
        
