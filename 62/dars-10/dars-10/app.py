import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Создание синтетического набора данных
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Разделение набора данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Стандартизация входных признаков
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Построение простой нейронной сети
model = Sequential()
model.add(Dense(64, input_dim=20, activation='relu'))  # Можно изменять количество нейронов и функцию активации
model.add(Dense(1, activation='sigmoid'))  # Слой вывода для бинарной классификации

# Компиляция модели
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Обучение модели
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Оценка модели на тестовом наборе
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Точность на тесте: {test_acc}')

# Построение истории обучения
plt.plot(history.history['accuracy'], label='Точность обучения')
plt.plot(history.history['val_accuracy'], label='Точность валидации')
plt.xlabel('Эпоха')
plt.ylabel('Точность')
plt.legend()
plt.show()
