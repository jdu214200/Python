# Импорт библиотек
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, mean_squared_error

# Загрузка набора данных Iris
iris = load_iris()
X = iris.data
y = iris.target

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Инициализация и обучение модели линейной регрессии
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Инициализация и обучение модели дерева решений
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)

# Инициализация и обучение модели SVM
svm_model = SVC()
svm_model.fit(X_train, y_train)

# Предсказание на тестовом наборе
linear_predictions = linear_model.predict(X_test)
tree_predictions = tree_model.predict(X_test)
svm_predictions = svm_model.predict(X_test)

# Оценка качества моделей
linear_accuracy = mean_squared_error(y_test, linear_predictions)
tree_accuracy = accuracy_score(y_test, tree_predictions)
svm_accuracy = accuracy_score(y_test, svm_predictions)

# Вывод результатов
print(f"Точность модели линейной регрессии: {linear_accuracy}")
print(f"Точность модели дерева решений: {tree_accuracy}")
print(f"Точность модели SVM: {svm_accuracy}")
