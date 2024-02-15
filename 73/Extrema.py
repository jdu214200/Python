import matplotlib.pyplot as plt #17dars
from skimage.measure import label
from skimage import data
from skimage import color
from skimage.morphology import extrema
from skimage import exposure

# Загрузка цветного изображения глубокого поля Хаббла из встроенных данных skimage
color_image = data.hubble_deep_field()

# Для иллюстрации работы алгоритма, обрезаем изображение
x_0 = 70
y_0 = 354
width = 100
height = 100
img = color.rgb2gray(color_image)[y_0:(y_0 + height), x_0:(x_0 + width)]

# Масштабирование яркости изображения для визуализации
img = exposure.rescale_intensity(img)

# Обнаружение всех локальных максимумов на изображении галактики
local_maxima = extrema.local_maxima(img)
label_maxima = label(local_maxima)
overlay = color.label2rgb(label_maxima, img, alpha=0.7, bg_label=0, bg_color=None, colors=[(1, 0, 0)])

# Определение локальных максимумов с уровнем яркости h
h = 0.05
h_maxima = extrema.h_maxima(img, h)
label_h_maxima = label(h_maxima)
overlay_h = color.label2rgb(label_h_maxima, img, alpha=0.7, bg_label=0, bg_color=None, colors=[(1, 0, 0)])

# Создание новой фигуры с тремя подграфиками
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Отображение оригинального изображения в первом подграфике
ax[0].imshow(img, cmap='gray')
ax[0].set_title('Оригинальное изображение')
ax[0].axis('off')

# Отображение локальных максимумов во втором подграфике
ax[1].imshow(overlay)
ax[1].set_title('Локальные максимумы')
ax[1].axis('off')

# Отображение локальных максимумов с уровнем яркости h в третьем подграфике
ax[2].imshow(overlay_h)
ax[2].set_title(f'h максимумы для h = {h:.2f}')
ax[2].axis('off')

# Отображение созданной фигуры
plt.show()
