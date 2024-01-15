import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.arange(1, 6)
y_line = np.array([10, 15, 7, 12, 20])
y_scatter = np.array([5, 8, 10, 2, 6])
y_bar = np.array([8, 12, 15, 7, 10])

# Bar Chart
plt.subplot(1, 3, 3)
plt.bar(x, y_bar, color='r', alpha=0.7)
plt.title('Bar Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()