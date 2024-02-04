import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    # Veb-kameradan kadrni olish
    ret, frame = cap.read()

    # Algoritim ishini yaxshilash uchun tasvirni kulrangga o'tkazish
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Kadrda yuzlarni aniqlash
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Aniqlangan yuzlarni sanab o'tish
    for (x, y, w, h) in faces:
        # Yuz atrofida to'rtburchak chizich.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Aniqlangan yuzlar bilan ramkani ko'rsatish
    cv2.imshow('Face Detection', frame)

    # "q" tugmachasini bosib dastur ishini to'xtatish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Resurslarni bo'shatish va oynalarni yopish
cap.release()
cv2.destroyAllWindows()
