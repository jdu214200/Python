import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.arange(1, 6)
y_line = np.array([10, 15, 7, 12, 20])
y_scatter = np.array([5, 8, 10, 2, 6])
y_bar = np.array([8, 12, 15, 7, 10])

# Line Chart
plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1)
plt.plot(x, y_line, marker='o', linestyle='-', color='b')
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()