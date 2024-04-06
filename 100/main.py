import cv2
import os

# Путь к изображению
image_path = 'путь_к_изображению.jpg'

# Проверка существования файла
if not os.path.isfile(image_path):
    print(f"Изображение по пути '{image_path}' не найдено.")
else:
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Ваш остальной код...
