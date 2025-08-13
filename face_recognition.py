from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import cv2
import os
import csv

class Face_Recognition:
    """
    A Tkinter-based application for real-time face recognition.
    It uses OpenCV for face detection and recognition, and connects to a MySQL
    database to retrieve student information and mark attendance in a CSV file.
    """
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Face Recognition System")

        # Main title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 45, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # Image for the left side of the window
        try:
            # Using a placeholder image for demonstration since the original path is local
            img_left = Image.open(r"college_images/face detection.jpg")
            img_left = img_left.resize((950, 1000), Image.Resampling.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            Label(self.root, image=self.photoimg_left).place(x=0, y=55, width=950, height=1000)
        except FileNotFoundError:
            messagebox.showerror("Error", "Missing 'college_images/face detection.jpg'")

        # Image for the right side of the window
        try:
            img_right = Image.open(r"college_images/recog.jpg")
            img_right = img_right.resize((950, 1000), Image.Resampling.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)
            Label(self.root, image=self.photoimg_right).place(x=950, y=55, width=950, height=1000)
        except FileNotFoundError:
            messagebox.showerror("Error", "Missing 'college_images/recog.jpg'")

        # Button to start the face recognition process
        Button(self.root, text="FACE RECOGNITION", command=self.face_recog,
               cursor="hand2", font=("times new roman", 20, "bold"), bg="green", fg="white").place(x=1265, y=900, width=315, height=60)

    def mark_attendance(self, student_id, roll, name, department):
        """
        Marks attendance in an attendance.csv file, avoiding duplicate entries for the day.
        """
        try:
            with open("attendance.csv", "a+", newline="") as f:
                # Check if the file is empty and write the header
                if f.tell() == 0:
                    f.writelines("student_id,roll,name,department,time,date,status\n")

                f.seek(0)
                myDataList = f.readlines()
                entry_found = False
                now = datetime.now()
                date_str = now.strftime("%Y-%m-%d")

                for line in myDataList:
                    entry = line.strip().split(",")
                    if entry[0] == str(student_id) and len(entry) > 5 and entry[5] == date_str:
                        entry_found = True
                        break

                if not entry_found:
                    d1 = now.strftime("%Y-%m-%d")
                    dtString = now.strftime("%H:%M:%S")
                    f.writelines(f"{student_id},{roll},{name},{department},{dtString},{d1},Present\n")

        except Exception as e:
            messagebox.showerror("Attendance Error", f"Failed to mark attendance: {e}")
            print(f"[ERROR] Failed to write to attendance.csv: {e}")

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf, db_cursor):
        """
        Detects faces in a frame, predicts the identity, and draws a boundary box.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

        for (x, y, w, h) in features:
            try:
                face_img = gray[y:y+h, x:x+w]
                if face_img.size == 0:
                    continue

                face_resized = cv2.resize(face_img, (200, 200))

                # Predict the face
                id_pred, predict = clf.predict(face_resized)
                confidence = int(100 * (1 - predict / 300.0))

                # Check if the confidence is high enough for a positive match
                if confidence > 60:
                    # Database query using the single, open cursor
                    db_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE student_id = %s", (str(id_pred),))
                    result = db_cursor.fetchone()

                    if result:
                        name, roll, dep = result
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                        cv2.putText(img, f"ID: {id_pred}", (x, y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll: {roll}", (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)
                        cv2.putText(img, f"Dept: {dep}", (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)
                        self.mark_attendance(str(id_pred), str(roll), str(name), str(dep))
                    else:
                        # If ID is predicted but no match in DB
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 3)

            except cv2.error as e:
                print(f"[OpenCV ERROR] {e}")
            except Exception as e:
                print(f"[ERROR inside draw_boundary loop] {e}")

        return img

    def face_recog(self):
        """
        Initializes the recognition model and starts the webcam stream.
        """
        # Load the Haar Cascade classifier for face detection
        if not os.path.exists("haarcascade_frontalface_default.xml"):
            messagebox.showerror("Error", "Missing: haarcascade_frontalface_default.xml")
            return
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # Check if the cv2.face module is available
        if not hasattr(cv2, "face"):
            messagebox.showerror("Error", "cv2.face not found. Please install opencv-contrib-python.")
            return

        # Load the trained LBPHFaceRecognizer model
        clf = cv2.face.LBPHFaceRecognizer_create()
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Missing: classifier.xml. Please train the model first.")
            return

        try:
            clf.read("classifier.xml")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read classifier.xml: {e}")
            return

        # Open the webcam with a loop to try different camera indexes
        video_cap = None
        for i in range(5):  # Try camera indexes 0 to 4
            video_cap = cv2.VideoCapture(i)
            if video_cap.isOpened():
                break
        
        if video_cap is None or not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open any webcam. Please check your camera connection and permissions.")
            return

        # Establish a single database connection before the main loop
        db_conn = None
        db_cursor = None
        try:
            db_conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="avinash123@#!",
                database="face_recognizer"
            )
            db_cursor = db_conn.cursor()

            while True:
                ret, frame = video_cap.read()
                if not ret:
                    print("Failed to grab frame from webcam.")
                    break

                img = self.draw_boundary(frame, face_cascade, 1.1, 10, (255, 0, 0), clf, db_cursor)
                cv2.imshow("Face Recognition", img)

                key = cv2.waitKey(1) 
                if key == 13 or key == 27:  # Enter or Esc key to quit
                    break

        except mysql.connector.Error as e:
            messagebox.showerror("DB Error", f"Failed to connect to database: {e}")
            print(f"[DB ERROR] {e}")
        finally:
            # Ensure the camera and database connections are always closed
            if video_cap:
                video_cap.release()
            cv2.destroyAllWindows()
            if db_cursor:
                db_cursor.close()
            if db_conn and db_conn.is_connected():
                db_conn.close()
                print("MySQL connection closed.")


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()



