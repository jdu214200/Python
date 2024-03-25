# Импорт библиотек
import numpy as np
import pandas as pd

# Создание данных с использованием NumPy
np.random.seed(42)
данные = np.random.randint(0, 100, size=(5, 3))  # Массив 5x3 случайных чисел от 0 до 100

# Создание DataFrame с использованием Pandas
df = pd.DataFrame(данные, columns=['Колонна_1', 'Колонна_2', 'Колонна_3'])

# Вывод DataFrame
print("Исходные данные:")
print(df)

# Примеры операций с DataFrame
среднее_значение = df.mean()
максимальное_значение = df.max()

print("\nСредние значения по колоннам:")
print(среднее_значение)

print("\nМаксимальные значения по колоннам:")
print(максимальное_значение)
