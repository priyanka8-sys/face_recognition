from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 45, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        img_left = Image.open(r"college_images/face detection.jpg")
        img_left = img_left.resize((950, 1000), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(self.root, image=self.photoimg_left).place(x=0, y=55, width=950, height=1000)

        img_right = Image.open(r"college_images/recog.jpg")
        img_right = img_right.resize((950, 1000), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(self.root, image=self.photoimg_right).place(x=950, y=55, width=950, height=1000)

        Button(self.root, text="FACE RECOGNITION", command=self.face_recog,
               cursor="hand2", font=("times new roman", 20, "bold"), bg="green", fg="white").place(x=1265, y=900, width=315, height=60)

    def face_recog(self):
        FACE_SIZE = (200, 200)   # IMPORTANT: use same size during training!

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

            for (x, y, w, h) in features:
                try:
                    face_img = gray[y:y+h, x:x+w]  # crop face
                    if face_img.size == 0:
                        continue

                    # resize to fixed size (must match training)
                    face_resized = cv2.resize(face_img, FACE_SIZE)

                    # Predict
                    id_pred, predict = clf.predict(face_resized)
                    confidence = int(100 * (1 - predict / 300.0))  # same formula you used

                    print(f"[DEBUG] Predicted ID: {id_pred}, raw predict: {predict}, confidence: {confidence}")

                    # Query DB for details
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",            # note: mysql.connector uses 'user' not 'username'
                            password="avinash123@#!",
                            database="face_recognizer"
                        )
                        my_cursor = conn.cursor()
                        # Use the correct column name in your DB; adjust 'student_id' if needed
                        my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE student_id = %s", (str(id_pred),))
                        result = my_cursor.fetchone()
                        conn.close()
                    except Exception as e:
                        print("[DB ERROR]", e)
                        result = None

                    # Tune threshold as needed. For debugging you can set low threshold.
                    if confidence > 60 and result:
                        name, roll, dep = result
                        cv2.putText(img, f"Roll: {roll}", (x, y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 3)
                        cv2.putText(img, f"Name: {name}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 3)
                        cv2.putText(img, f"Dept: {dep}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 3)
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 3)

                except cv2.error as e:
                    print("[OpenCV ERROR]", e)
                except Exception as e:
                    print("[ERROR inside draw_boundary]", e)

            return img

        def recognize(img, clf, face_cascade):
            return draw_boundary(img, face_cascade, 1.1, 10, (255, 0, 0), clf)

        # Load cascade and trained model
        if not os.path.exists("haarcascade_frontalface_default.xml"):
            messagebox.showerror("Error", "Haar cascade file not found: haarcascade_frontalface_default.xml")
            return

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # Check cv2.face availability
        if not hasattr(cv2, "face"):
            messagebox.showerror("Error", "cv2.face not found. Install opencv-contrib-python.")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()

        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Trained model 'classifier.xml' not found. Please train first.")
            return

        try:
            clf.read("classifier.xml")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read classifier.xml: {e}")
            return

        # Start webcam
        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open webcam.")
            return

        while True:
            ret, frame = video_cap.read()
            if not ret:
                print("Failed to grab frame from webcam.")
                break

            img = recognize(frame, clf, face_cascade)
            cv2.imshow("Face Recognition", img)

            # press ESC (27) or ENTER (13) to exit
            key = cv2.waitKey(1) & 0xFF
            if key == 13 or key == 27:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()