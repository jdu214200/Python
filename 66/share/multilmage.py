# Tavsirga bir nechta usullar yordamida ishlov berish va
# ularni yagona oynada chiqarish dasturi

from skimage.io import imread, imshow
from matplotlib import pyplot as plt

file = "images/Kolibri.jpg"

# figura (rasm oynasi)ni yaratish
fig = plt.figure(figsize=(10, 7))

# rasmni o'zgrtirish

imageOriginal = imread(file)
imageGray = imread(file, as_gray=True)

# Figura 2x3 o'lchamda
# Figuraning 1-pozitsiyasiga subplot (qism oyna) qo'shish
fig.add_subplot(2, 3, 1)

# Original tasvirni ko'rsatish
plt.imshow(imageOriginal)
plt.axis('off')
plt.title("Original tasvir")

# Figuraning 2-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 3, 2)

# Kulrang tasvirni ko'rstish
plt.imshow(imageGray, cmap="gray")
plt.axis('off')
plt.title("Kulrang tasvir")

# Figuraning 3-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 3, 3)

# tasvirni ko'rsatish
plt.imshow(imageGray, cmap="plasma")
plt.axis('off')
plt.title("plasma")

# Figuraning 4-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 3, 4)

# tasvirni korsatish
plt.imshow(imageGray, cmap='Accent')
plt.axis('off')
plt.title("Accent")

# Figuraning 5-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 3, 5)

# tasvirni ko'rsatish
plt.imshow(imageGray, cmap='copper')
plt.axis('off')
plt.title("copper")

# Figuraning 5-pozitsiyasiga subplot qo'shish
fig.add_subplot(2, 3, 5)

# tasvirni ko'rsatish
plt.imshow(imageGray, cmap='jet')
plt.axis('off')
plt.title("jet")

plt.show()