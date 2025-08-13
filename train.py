from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

# A consistent size is crucial for both training and recognition.
FACE_SIZE = (200, 200)

class Train:
    """
    A Tkinter-based application to train a face recognition model using
    images from the 'data' directory.
    """
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1200+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # Handle image file paths more robustly
        try:
            img_top = Image.open(r"college_images/face_recog.jpg")
            img_top = img_top.resize((1900, 415), Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            Label(self.root, image=self.photoimg_top).place(x=0, y=55, width=1900, height=415)
        except FileNotFoundError:
            messagebox.showerror("Error", "Missing 'college_images/face_recog.jpg'")

        Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
               font=("times new roman", 40, "bold"), bg="red", fg="white").place(x=0, y=470, width=1900, height=80)

        try:
            img_bottom = Image.open(r"college_images/peoples.jpg")
            img_bottom = img_bottom.resize((1900, 415), Image.Resampling.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            Label(self.root, image=self.photoimg_bottom).place(x=0, y=550, width=1900, height=415)
        except FileNotFoundError:
            messagebox.showerror("Error", "Missing 'college_images/peoples.jpg'")

    def face_cropped(self, img):
        """
        Crop a face from an image and resize it to a fixed size.
        This function is crucial for creating consistent training data.
        """
        # Load the Haar Cascade classifier
        try:
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                # Crop the face from the grayscale image
                face_crop = gray[y:y+h, x:x+w]
                # Resize the cropped face to the consistent size
                face_resized = cv2.resize(face_crop, FACE_SIZE)
                return face_resized
        except cv2.error as e:
            print(f"[OpenCV ERROR in face_cropped]: {e}")
            messagebox.showerror("OpenCV Error", "An error occurred during face detection.")
        return None

    def train_classifier(self):
        """
        Collects all face images from the 'data' directory, extracts the IDs from
        the filenames, and trains the LBPHFaceRecognizer model.
        """
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory '{data_dir}' not found.")
            return

        if not os.path.exists("haarcascade_frontalface_default.xml"):
            messagebox.showerror("Error", "Missing: haarcascade_frontalface_default.xml")
            return

        faces = []
        ids = []

        print("Starting training process...")
        for file_name in os.listdir(data_dir):
            file_path = os.path.join(data_dir, file_name)
            if file_name.lower().endswith(('.jpg', '.png', '.jpeg')):
                try:
                    img = cv2.imread(file_path)
                    face_img = self.face_cropped(img)
                    
                    if face_img is not None:
                        # Extract ID from filename, e.g., 'user.1.1.jpg' -> ID is 1
                        id_str = file_name.split('.')[1]
                        
                        try:
                            id = int(id_str)
                            faces.append(face_img)
                            ids.append(id)
                            print(f"Added face from {file_name} with ID {id}")
                            cv2.imshow("Training...", face_img)
                            cv2.waitKey(1)
                        except (ValueError, IndexError):
                            print(f"Skipping {file_name}, invalid name format. Expected format: user.ID.index.jpg")

                except Exception as e:
                    print(f"Error processing {file_name}: {e}")

        cv2.destroyAllWindows()

        if not faces:
            messagebox.showerror("Error", "No valid face images found for training. Check 'data' directory and filenames.")
            return

        ids = np.array(ids)

        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            messagebox.showinfo("Result", "Training datasets completed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {e}")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()