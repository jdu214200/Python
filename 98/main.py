import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Загрузка данных (исправленный код с использованием встроенного датасета Iris)
iris = load_iris()
X, y = iris.data, iris.target

# Кодирование меток классов
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Добавление временного шага к данным
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Создание и обучение рекуррентной нейронной сети
model = tf.keras.models.Sequential([
    tf.keras.layers.SimpleRNN(32, activation='relu', input_shape=(X_train.shape[1], 1)),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Оценка производительности модели
predictions = model.predict(X_test)
y_pred = tf.argmax(predictions, axis=1).numpy()
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность рекуррентной нейронной сети: {accuracy}")
