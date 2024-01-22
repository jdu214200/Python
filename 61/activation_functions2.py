# Import necessary libraries
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras import backend as K


# Custom Heaviside activation function for inference
def heaviside_activation(x):
    return K.cast(x > 0, dtype='float32')


# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Preprocess the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define activation functions to experiment with
activation_functions = ['linear', 'sigmoid', 'relu', 'tanh', 'softmax']


# Function to create a model with a specified activation function
def create_model(activation_function):
    model = Sequential()
    model.add(Dense(64, input_dim=X_train.shape[1]))
    model.add(Activation(activation_function))
    model.add(Dense(32))
    model.add(Activation(activation_function))
    model.add(Dense(3, activation='softmax'))  # Change to 3 classes for Iris dataset
    return model


# Loop through activation functions and train models
for activation_function in activation_functions:
    print(f"\nTraining model with {activation_function} activation function:")

    # Create and compile the model
    model = create_model(activation_function)
    model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=0)

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss with {activation_function} activation function: {loss}")
    print(f"Test Accuracy with {activation_function} activation function: {accuracy}")