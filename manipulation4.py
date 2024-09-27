import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv')
print(df)

# adding new column
df["city"]="london"
print(df)

#delete column
df=df.drop(['city'],axis=1)
print(df)

#delete row
df=df.drop([4],axis=0)
print(df)
