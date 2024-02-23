import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import requests

# Загрузка изображений из интернета
url_img1 = "https://www.tama.ac.jp/guide/teacher/img/shinnishi_makoto.jpg"
url_img2 = "https://researchmap.jp/newest/avatar.jpg"
url_img3 = "https://www.tama.ac.jp/guide/teacher/img/suganuma_mutsumi.jpg"
url_img4 = "https://crmsj.org/wp/wp-content/uploads/2023/08/37e3808047553cedb34daa9b1d7ab2a3-1024x390.jpeg"

response_img1 = requests.get(url_img1)
response_img2 = requests.get(url_img2)
response_img3 = requests.get(url_img3)
response_img4 = requests.get(url_img4)

with open("img1.jpg", "wb") as img_file:
    img_file.write(response_img1.content)

with open("img2.jpg", "wb") as img_file:
    img_file.write(response_img2.content)

with open("img3.jpg", "wb") as img_file:
    img_file.write(response_img3.content)

with open("img4.jpg", "wb") as img_file:
    img_file.write(response_img4.content)

# Верификация сходства лиц между img1 и img2
result = DeepFace.verify('img1.jpg', 'img2.jpg')
print("Сходство лиц между img1 и img2:", result)

# Верификация сходства лиц между img1 и img3
result = DeepFace.verify('img1.jpg', 'img3.jpg')
print("Сходство лиц между img1 и img3:", result)

# Анализ особенностей лица на img1
DeepFace.analyze('img1.jpg', actions=["age", "gender", "emotion", "race"])

# Верификация сходства лиц между img2 и img4
result = DeepFace.verify('img2.jpg', 'img4.jpg')
print("Сходство лиц между img2 и img4:", result)

# Отображение изображения с прямоугольником вокруг обнаруженного лица на img4
resp = DeepFace.verify('img2.jpg', 'img4.jpg')
orig = cv2.imread("img4.jpg")
x, y, w, h = resp["facial_areas"]['img4']["x"], resp["facial_areas"]['img4']["y"], resp["facial_areas"]['img4']["w"], resp["facial_areas"]['img4']["h"]

img = cv2.rectangle(orig, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4, shift=0)

# Отображение окончательного изображения
show_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(show_img)
plt.show()



