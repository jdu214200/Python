import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

# Iris ma'lumotlarini ko'chirib olish
iris = load_iris()
x = iris.data
y = iris.target

# Tanlanmani o'quv va test to'plamlarga ajratish
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Ma'lumotlarni normallashtirish
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Bir qatlamli addiy neyron to'rini yaratish
model = Sequential()
model.add(Dense(units=10, input_dim=4, activation='relu'))  # Kiruvchi belgilari 4 ta
model.add(Dense(units=3, activation='softmax'))  # Irisda 3 ta sinf
model.compile(loss='sparse_categorical_crossentropy', optimizer=SGD(learning_rate=0.1), metrics=['accuracy'])

# Neyron to'ri tuzilmasi chiqish qiymati
print("Yangi neyron qo'shilishidan oldin:")
model.summary()

# Qatlamga yana bir yangi neyron qo'shish
model.add(Dense(units=1))

# Neyron to'ri tuzilmasi chiqish qiymati
print("\nYangi neyron qo'shilgandan keyin:")
model.summary()
