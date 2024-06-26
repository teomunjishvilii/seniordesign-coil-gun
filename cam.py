import cv2
import time

def capture_image():		
	cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

	if not cap.isOpened():
		print("Error")
		exit()

	ret, frame = cap.read()
	if ret:	
		out = cv2.imwrite('captureCEI0.jpg', frame)
	else:
		print("Failed to capture image!")
		
		
capture_image()
