from skimage import io, color, exposure, transform
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Функция для отображения изображений
def show_img(*args, cmap=None):
    fig, axes = plt.subplots(1, len(args), figsize=(12, 4))
    for i, img in enumerate(args):
        axes[i].imshow(img, cmap=cmap)
        axes[i].axis('off')
    plt.show()

# Загрузка изображения из сети
image = io.imread('https://img.freepik.com/free-photo/a-colorful-hummingbird-with-a-colorful-background_1340-38746.jpg')

# Применение различных вариантов обработки цвета

# Преобразование изображения в оттенки серого
gray_image = color.rgb2gray(image)

# Изменение яркости и контраста
brightened_image = exposure.adjust_gamma(image, gamma=1.5)
contrast_enhanced_image = exposure.rescale_intensity(image, in_range=(0, 100), out_range=(0, 255))

# Инверсия цветов
inverted_image = 255 - image

# Отображение исходного и обработанных изображений
show_img(image, gray_image, brightened_image, contrast_enhanced_image, inverted_image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение поворота изображения на различные углы и направления

# Поворот на 30 градусов
rotated_30_deg = transform.rotate(gray_image, angle=30)

# Поворот на -45 градусов (в обратную сторону)
rotated_minus_45_deg = transform.rotate(gray_image, angle=-45)

# Поворот на 90 градусов
rotated_90_deg = transform.rotate(gray_image, angle=90)

# Отображение исходного и повернутых изображений
show_img(gray_image, rotated_30_deg, rotated_minus_45_deg, rotated_90_deg, cmap='gray')