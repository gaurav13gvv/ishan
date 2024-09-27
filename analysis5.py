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

#modify single value
df.loc[2, 'pclass'] = 2
print(df)

#display first(n)rows
print(df.head(4))
print(df)

#display last(n)rows
print(df.tail(2))
print(df)

# Display non-adjacent columns 'Name', 'Age', and 'Fare'
non_adjacent_columns = df[['Name', 'Age', 'Fare']]
print(non_adjacent_columns)

# Display non-adjacent rows 1, 3, and 5 (Python uses 0-based indexing)
non_adjacent_rows = df.iloc[[0, 2, 4]]  # This will display rows with index 0, 2, and 4
print(non_adjacent_rows)

#display shape, size, info
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

#modify single value
df.loc[2, 'pclass'] = 2
print(df)

#display first(n)rows
print(df.head(4))
print(df)

#display last(n)rows
print(df.tail(2))
print(df)

# Display non-adjacent columns 'Name', 'Age', and 'Fare'
non_adjacent_columns = df[['Name', 'Age', 'Fare']]
print(non_adjacent_columns)

# Display non-adjacent rows 1, 3, and 5 (Python uses 0-based indexing)
non_adjacent_rows = df.iloc[[0, 2, 4]]  # This will display rows with index 0, 2, and 4
print(non_adjacent_rows)

#display shape,size,info
print(df.shape)  # Shape of the DataFrame
print(df.size)   # Total elements in DataFrame
print(df.info()) # Information about DataFrame




