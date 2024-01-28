# Tavsirni shaklan o'zgartirish dasturi

from skimage.io import imread, imshow
from matplotlib import pyplot as plt

from skimage.transform import  resize, rescale, rotate
from numpy import fliplr, flipud

# rasmni fayli manzilini file o'zgaruvchisiga olish
file = "images/Kolibri.jpg"

# rasm faylini o'qish
imageOriginal = imread(file)
imageResized = resize(imageOriginal, (300, 300)) # O'lchamlari o'zgartirilgan tasvir
imageRescaled = rescale(imageOriginal, 0.5, channel_axis=2) # Mashtablashtirilgan tasvir
imageRotated = rotate(imageOriginal, angle=30) # 30 gradusga burilgan tasvir
imageRotated2 = rotate(imageOriginal, angle=45, resize=True) # 45 gradusga burilgan tasvir
imageFlipud = flipud(imageOriginal)
imageFliplr = fliplr(imageOriginal)

height, width, _ = imageOriginal.shape
imageCropped = imageOriginal[240:(height-170),10:(width-10)]

# figura (rasm oynasi)ni yaratish
fig = plt.figure(figsize=(15,7))

# Figura 2x4 o'chamda
# Figurani 1-pozitsiyasiga subplot (qism oyna) qo'shish
fig.add_subplot(2, 4, 1)

# Original tasvirni ko'rsatish
plt.imshow(imageOriginal)
plt.axis('on')
plt.title("Original tasvir")

# Figuraning 2-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 4, 2)

# O'lcham o'zgartirilgan (300x300)
plt.imshow(imageResized)
plt.axis('on')
plt.title("Resize(300x300)")

# Figuraning 3-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 4, 3)

# Mashtablashtirilgan tasvir
plt.imshow(imageRescaled)
plt.axis('on')
plt.title("Rescale (0.5)")

# Figuraning 4-pozitsiga subplot qo'shish
fig.add_subplot(2, 4, 4)

# 30 gradusga burilgan tasvir
plt.imshow(imageRotated)
plt.axis('off')
plt.title("30 gradusga burish")

# Figuraning 5-pazitsiyasiga subplot qo'shish
fig.add_subplot(2, 4, 5)

# O'lchamlarini o'zgartirib, 45 gradusga burilgan tasvir
plt.imshow(imageRotated2)
plt.axis('off')
plt.title("45 gradusga burish")

# Figuraning 6-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 4, 6)

# tasvirni teskari qilish (yuqoridan-pastga)
plt.imshow(imageFlipud)
plt.axis('off')
plt.title("Flipud")

# Figuraning 7-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 4, 7)

# tasvirni teskari qilish (chapdan-o'ngga)
plt.imshow(imageFliplr)
plt.axis('off')
plt.title("Fliplr")

# Figuraning 8-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 4, 8)

# tasvirni kesish
plt.imshow(imageCropped)
plt.axis('off')
plt.title("Cropped")

plt.show()