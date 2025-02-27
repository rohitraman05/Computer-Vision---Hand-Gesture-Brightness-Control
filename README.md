# Computer-Vision---Hand-Gesture-Brightness-Control

# Hand Gesture Brightness Control 🖐💡  

A **Computer Vision** project that controls **laptop screen brightness** using **hand gestures**.  
Uses **OpenCV, Mediapipe, and Screen Brightness Control**.  

## 🔹 Features  
✔ Adjust brightness using thumb-index distance  
✔ Real-time hand tracking  
✔ Runs in the background  

## 🔹 Prerequisites  
Install dependencies using:  
```bash
pip install opencv-python mediapipe screen-brightness-control

##🔹 1. Code Explanation
Your script uses OpenCV, Mediapipe, and screen-brightness-control to adjust screen brightness with hand gestures.

📌 Key Components
1️⃣ Import Required Modules
python
Copy
Edit
import cv2
import mediapipe as mp
import screen_brightness_control as sbc
import numpy as np
cv2 → Captures webcam feed
mediapipe → Detects hand landmarks
screen_brightness_control → Adjusts laptop brightness
numpy → Computes distance between fingers

