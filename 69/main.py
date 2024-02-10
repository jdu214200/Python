import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import  to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# CNN modelini qurish
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Modelni kompilyatsiyalash
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Modelni o'qitish
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

#Modelning aniqligini baholash
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test ma'lumotlari asosidagi aniqlik: {test_acc}")

# Test ma'lumotlarni bashoratlash
predictions = model.predict(test_images)

# Bir nechta bashoratlarni vizuallashtirish
num_samples = 5
for i in range(num_samples):
    plt.figure(figsize=(2, 2))
    plt.imshow(test_images[i].reshape(28, 28), cmap='gray')
    plt.title(f"Bashorat natijasi: {np.argmax(predictions[i])}, Real: {np.argmax(test_labels[i])}")
    plt.show()