import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
iris_data = iris.data
iris_target = iris.target
iris_feature_names = iris.feature_names
import pandas as pd
iris_df = pd.DataFrame(data=iris_data, columns=iris_feature_names)
iris_df['Species'] = iris.target_names[iris_target]

sn.pairplot(iris_df, hue='Species', markers=["o", "s", "D"])
plt.suptitle('Abbos abbos abbos', y=1.02)
plt.show()

plt.figure(fiqsize=(12, 8))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    sn.boxplot(x='Species', y=iris_feature_names[i], data=iris_df)
    plt.title(f'Abbooooooooooos: {iris_feature_names[i]}')
plt.tight_layout
plt.show()
