import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv')

# Count the number of passengers in each class
passenger_class_counts = df['Pclass'].value_counts()

# Create the bar chart
plt.bar(passenger_class_counts.index, passenger_class_counts.values, color='skyblue')
plt.title('Number of Passengers per Class')
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.xticks([1, 2, 3])  # Set the x-ticks to correspond to classes
plt.show()


