# work
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset.csv')
print(df.head())
cuisine_counts = df['Cuisines'].value_counts()
top_cuisines = cuisine_counts.head(3)
total_restaurants = len(df)
percentages = (top_cuisines / total_restaurants) * 100
import numpy as np

# Define the colors for the bars
colors = ['red', 'blue', 'green']

# Plot the bar chart with colors
plt.bar(top_cuisines.index, top_cuisines.values, color=colors)

# Add labels and title
plt.xlabel('cuisine')
plt.ylabel('count')
plt.title('top three cusines')

#show the chart
plt.show()
plt.pie(top_cuisines.values, labels=top_cuisines.index, autopct='%1.1f%%')
plt.title('top three cuisines')
plt.show()
