import cv2
import os
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Dataset directory
DATASET_DIR = 'dataset/'
attendance_file = 'attendance.csv'
model_file = 'knn_model.pkl'

# Ensure dataset and attendance file exist
os.makedirs(DATASET_DIR, exist_ok=True)
if not os.path.exists(attendance_file):
    pd.DataFrame(columns=['Name', 'Time']).to_csv(attendance_file, index=False)

# Function to capture a student's face and save it
def capture_face(student_name):
    cap = cv2.VideoCapture(0)
    print(f"Capturing face for {student_name}. Press 'q' to capture and save.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml").detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y + h, x:x + w]
            folder = os.path.join(DATASET_DIR, student_name)
            os.makedirs(folder, exist_ok=True)
            cv2.imwrite(os.path.join(folder, f"{student_name}.jpg"), face)
            print(f"Image saved for {student_name}.")
            cap.release()
            cv2.destroyAllWindows()
            return

        cv2.imshow('Capture Face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to train the KNN model
def train_model():
    encodings = []
    labels = []

    for student in os.listdir(DATASET_DIR):
        student_folder = os.path.join(DATASET_DIR, student)
        for img_name in os.listdir(student_folder):
            img_path = os.path.join(student_folder, img_name)
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face = cv2.resize(gray, (100, 100)).flatten()
            encodings.append(face)
            labels.append(student)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(encodings, labels)

    with open(model_file, 'wb') as f:
        pickle.dump(knn, f)
    print("Model trained and saved!")

# Function to mark attendance
def mark_attendance(name):
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    
    # Ensure file is initialized properly
    try:
        df = pd.read_csv(attendance_file)
    except (pd.errors.EmptyDataError, FileNotFoundError):
        df = pd.DataFrame(columns=['Name', 'Time'])

    if name not in df['Name'].values:
        new_entry = pd.DataFrame({'Name': [name], 'Time': [timestamp]})
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(attendance_file, index=False)
        print(f'Attendance marked for {name}.')
    else:
        print(f'{name} already marked.')

# Real-time face recognition and attendance
def recognize_faces():
    with open(model_file, 'rb') as f:
        knn = pickle.load(f)

    cap = cv2.VideoCapture(0)
    print("Recognizing faces. Press 'q' to quit.")

    marked = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml").detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = cv2.resize(gray[y:y + h, x:x + w], (100, 100)).flatten().reshape(1, -1)
            name = knn.predict(face)[0]
            if name not in marked:
                mark_attendance(name)
                marked.add(name)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main menu
def main():
    while True:
        print("\nMenu:")
        print("1. Add new student")
        print("2. Train model")
        print("3. Recognize and mark attendance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter the student's name: ").strip()
            capture_face(student_name)
        elif choice == '2':
            train_model()
        elif choice == '3':
            recognize_faces()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
