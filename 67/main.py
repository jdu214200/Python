import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1: Install Required Libraries
# (Already mentioned in the previous response)

# Task 2: Generate Time-Dependent Data and Save to CSV
timestamps = pd.date_range('2024-01-01', '2024-01-10', freq='D')
values = np.random.rand(len(timestamps))
df = pd.DataFrame({'Timestamp': timestamps, 'Value': values})
df.to_csv('time_dependent_data.csv', index=False)

# Task 3: Display Data in Visual Diagrams
# Line Plot
plt.figure(figsize=(10, 5))
plt.plot(df['Timestamp'], df['Value'], label='Time-Dependent Data', marker='o')
plt.title('Time-Dependent Data - Line Plot')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(df['Timestamp'], df['Value'], color='red', label='Scatter Plot')
plt.title('Time-Dependent Data - Scatter Plot')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.show()

# Task 4: Display Results in Various Ways
# Histogram
plt.figure(figsize=(10, 5))
plt.hist(df['Value'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Basic Statistics
mean_value = df['Value'].mean()
median_value = df['Value'].median()
std_dev_value = df['Value'].std()

# Display basic statistics
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev_value)

# Additional Visualization: Box Plot
plt.figure(figsize=(8, 5))
plt.boxplot(df['Value'], vert=False)
plt.title('Box Plot of Values')
plt.xlabel('Value')
plt.show()