# Face Recognition System

A Python-based **Face Recognition System** for detecting, recognizing, and managing attendance using facial data.  
This project uses **OpenCV** and **Haar Cascade Classifiers** for face detection, along with training and recognition scripts.

---

## 📌 Features
- Detect and recognize faces in real-time via webcam.
- Train a face recognition model from stored images.
- Maintain student details and attendance records.
- Modular scripts for training, recognition, and management.
- Uses Haar Cascade for detection and LBPH (Local Binary Pattern Histogram) for recognition.

---

## 📂 Project Structure




face_recognition/
├── college_images/ # Dataset of student images
├── data/ # Training data folder
├── attendence.py # Attendance logging
├── classifier.xml # Trained face recognition model
├── developer.py # Developer/testing utilities
├── face_recognition.py # Face detection & recognition
├── haarcascade_frontalface_default.xml # Haar Cascade XML file
├── help.py # Helper functions
├── main.py # Main application entry point
├── student.py # Student data management
├── train.py # Model training script
└── README.md # Project documentation




---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/priyanka8-sys/face_recognition.git
cd face_recognition
