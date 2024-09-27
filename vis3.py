import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv')

# Create a histogram to show the distribution of passenger ages
plt.hist(df['Age'].dropna(), bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Passenger Ages')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.show()
