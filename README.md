# ✋ Hand Gesture Controlled Brightness - Python Project

This project uses **hand gestures detected via webcam** to control the **brightness of your laptop screen** in real-time. It integrates **Computer Vision (OpenCV & MediaPipe)** with **System Control (Screen_Brightness_Control)**, offering an innovative hands-free approach to screen brightness adjustment.

---

## 🚀 Features
- Detects **hand using webcam**.
- Tracks **distance between thumb and index finger** to adjust brightness.
- **Real-time updates** - move your fingers closer or farther to change brightness.
- Works on **Windows laptops**.

---

## 🛠️ Technologies Used
- Python
- OpenCV (for webcam feed and hand tracking)
- MediaPipe (for hand landmarks detection)
- Screen_Brightness_Control (for modifying laptop brightness)

---

## ⚙️ How It Works

1. The webcam captures your hand movements.
2. **MediaPipe** detects key points (landmarks) on your hand.
3. The distance between **thumb and index finger** is calculated.
4. This distance is mapped to a brightness scale (0% - 100%).
5. The **screen_brightness_control** library applies the brightness to your laptop.

---

## 📸 Example Demo

- Place your hand in front of the camera.
- Move your **thumb and index finger** closer to reduce brightness.
- Move them farther apart to increase brightness.

---

## 🎯 Key Learning Areas

- Computer Vision (Hand Tracking using **MediaPipe**)
- OpenCV for webcam feed
- System-level control via Python
- Mapping **distance to brightness level** using simple math

---

## 📊 Applications

- **Touchless laptop control**
- Accessibility enhancement for **physically challenged users**
- Future extension - gesture control for volume, screen lock, etc.

---
