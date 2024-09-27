import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')

# Create a line chart showing the relationship between Age and Fare
plt.plot(df['Age'], df['Fare'], linestyle='-', marker='o', color='green')
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.grid(True)
plt.show()
