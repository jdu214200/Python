# Импорт библиотек
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Загрузка набора данных Iris
iris = load_iris()
X = iris.data
y = iris.target

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Инициализация и обучение модели классификации (например, k-ближайших соседей)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Предсказание на тестовом наборе
predictions = model.predict(X_test)

# Оценка качества модели
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

# Вывод результатов
print(f"Точность модели: {accuracy}")
print("\nОтчет по классификации:")
print(report)
