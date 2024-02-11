import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

# Загрузка данных
digits = datasets.load_digits()
images = digits.images
labels = digits.target

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Создание модели машинного обучения (например, сверточная нейронная сеть)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(8, 8, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели
model.fit(X_train.reshape(-1, 8, 8, 1), y_train, epochs=5, validation_data=(X_test.reshape(-1, 8, 8, 1), y_test))

# Оценка модели на тестовых данных
test_loss, test_acc = model.evaluate(X_test.reshape(-1, 8, 8, 1), y_test)
print(f"Точность на тестовых данных: {test_acc}")
