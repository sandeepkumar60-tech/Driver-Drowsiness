import cv2
import numpy as np
import dlib
from imutils import face_utils

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"D:\Driver-Drowsiness-Project\Driver-Drowsiness-Project\shape_predictor_68_face_landmarks.dat")

sleep, drowsy, active = 0, 0, 0
status = ""
color = (0, 0, 0)

def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    return ratio

print("Driver Drowsiness Detection started...")
print("Press ESC to stop.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 0)

    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_ratio = blinked(
            landmarks[36], landmarks[37], landmarks[38],
            landmarks[41], landmarks[40], landmarks[39]
        )
        right_ratio = blinked(
            landmarks[42], landmarks[43], landmarks[44],
            landmarks[47], landmarks[46], landmarks[45]
        )

        blink_ratio = (left_ratio + right_ratio) / 2.0

        # Print ratio in terminal for calibration
        print(f"Blink ratio: {blink_ratio:.3f}", end="\r")

        if blink_ratio < 0.27:        # relaxed for easier trigger
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 3:
                status = "SLEEPING !!!"
                color = (0, 0, 255)
        elif 0.27 <= blink_ratio < 0.32:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 3:
                status = "Drowsy !"
                color = (0, 165, 255)
        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 3:
                status = "Active :)"
                color = (0, 255, 0)

        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, status, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv2.putText(frame, f"Ratio: {blink_ratio:.2f}", (x1, y2 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    cv2.imshow("Driver Drowsiness Detection", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("\nProgram exited successfully.")
