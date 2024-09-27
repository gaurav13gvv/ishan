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

#modify values of a row
df.loc[5]=[5,2,1,"james cameron","male",24,0,1,688970,7.500,"C190","c"]
print(df)

#modify values of a column
df["parch"]=0
print(df)

