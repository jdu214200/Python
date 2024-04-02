import tensorflow as tf
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Генерация данных для бинарной классификации
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение простого перцептрона
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, activation='sigmoid', input_shape=(X_train.shape[1],))
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Оценка производительности модели
predictions = model.predict(X_test)
y_pred = (predictions > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность перцептрона: {accuracy}")
