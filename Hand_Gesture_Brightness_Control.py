import cv2
import mediapipe as mp
import screen_brightness_control as sbc
import numpy as np

# Initialize Mediapipe Hands module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Extract landmarks
            landmarks = hand_landmarks.landmark

            # Get coordinates of thumb and index finger
            h, w, _ = frame.shape
            x1, y1 = int(landmarks[4].x * w), int(landmarks[4].y * h)   # Thumb tip
            x2, y2 = int(landmarks[8].x * w), int(landmarks[8].y * h)   # Index finger tip

            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Calculate distance
            distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Map distance to brightness (10 to 100%)
            brightness = np.interp(distance, [20, 200], [10, 100])

            # Apply brightness
            sbc.set_brightness(int(brightness))

            # Display brightness level
            cv2.putText(frame, f'Brightness: {int(brightness)}%', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (0, 255, 0), 2, cv2.LINE_AA)

            # Draw a line between thumb and index finger
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    # Show webcam feed
    cv2.imshow("Hand Gesture Brightness Control", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
