import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv')
print(df)

#adding new column
df["city"]="london"
print(df)

