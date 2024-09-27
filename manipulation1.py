import pandas as pd

# Replace 'your_dataset.csv' with your actual dataset file name
df = pd.read_csv('Titanic-Dataset.csv')
print(df)

#adding new row
df1=df.loc[891]=[892,2,3,'Chris Williamson','male',20,1,0,24772,30.0000,'B78','s']
print(df1)
