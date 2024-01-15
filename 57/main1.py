import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.arange(1, 6)
y_line = np.array([10, 15, 7, 12, 20])
y_scatter = np.array([5, 8, 10, 2, 6])
y_bar = np.array([8, 12, 15, 7, 10])



# Scatter Plot
plt.subplot(1, 3, 2)
plt.scatter(x, y_scatter, color='g', marker='s')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')



plt.tight_layout()
plt.show()