import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv')

# Calculate the number of survivors and non-survivors
survival_counts = df['Survived'].value_counts()

# Create the pie chart
plt.pie(survival_counts, labels=['Did Not Survive', 'Survived'], autopct='%1.1f%%', colors=['lightcoral', 'lightgreen'], startangle=90)
plt.title('Survival Rate')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
