import cv2

def load_and_process_image(image_path, target_size=(500, 500)):
    try:
        # Загрузка изображения
        image = cv2.imread(image_path)

        # Проверка, удалось ли загрузить изображение
        if image is None:
            raise FileNotFoundError(f"Изображение по пути '{image_path}' не найдено.")

        # Изменение размера изображения
        resized_image = cv2.resize(image, target_size)

        # Дополнительные операции с изображением (по вашему желанию)
        # Например, можно применить фильтры, конвертировать в ч/б и т.д.

        return resized_image

    except Exception as e:
        print(f"Произошла ошибка при обработке изображения: {e}")
        return None

# Пример использования функции
image_path = 'yorichi.jpg.jpg'
processed_image = load_and_process_image(image_path)

if processed_image is not None:
    cv2.imshow('Обработанное изображение', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
