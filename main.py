import cv2
import sys

WINDOW_NAME = 'Video Feed'

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video.")
    sys.exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        
    cv2.imshow('Video Feed', frame)
    
    # Use bitwise AND to handle cross-platform key codes (e.g., for Windows/Linux compatibility)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()