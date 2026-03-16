import pandas as pd
import os 

data= {'Name': ['Vishal','Bob','King'],
      'Age': [25,30,35],
      'City': ['New york','LA','chicago']
      }
df=pd.DataFrame(data)

##adding new row to df for v2
new_row_loc = {'Name':'GF1','Age' : 20, 'City':'City1'}
df.loc[len(df.index)]=new_row_loc

data_dir='data'
os.makedirs(data_dir, exist_ok=True)

file_path= os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path, index=False)
print(f"csv file save to {file_path}")