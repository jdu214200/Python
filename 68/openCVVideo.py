import cv2

myCapture = cv2.VideoCapture('Video/90s Anime edit -`♥´-.mp4')

if not myCapture.isOpened():
    print("Ошибка при открытии видеофайла!")

while myCapture.isOpened():
    ret, frame = myCapture.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

myCapture.release()
cv2.destroyAllWindows()