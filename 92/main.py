# Импорт библиотек
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Загрузка данных из файла CSV
# Предположим, что у вас есть файл "your_data.csv" с признаками и метками
data = pd.read_csv('your_data.csv')

# Выделение признаков (X) и меток (y)
X = data.drop('target_column', axis=1)  # Замените 'target_column' на вашу целевую переменную
y = data['target_column']

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Инициализация и обучение модели случайного леса
model = RandomForestClassifier(random_state=42)
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
