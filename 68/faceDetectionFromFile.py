import cv2 #12dars

img = cv2.imread('Picture/Peoples.jpg')

print(img.shape)
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(grayImage.shape)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(grayImage, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('Face Detection from image file', img_rgb)

# "q" tugmachasini bosib dastur ishini to'xtatish
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
