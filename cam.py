import cv2
import time

cap = cv2.VideoCapture(0)

#if not cap.isOpened():
#	print("Error")
#	exit()
i = 0
while i<1:
	ret, frame = cap.read()
	out = cv2.imwrite('captureCEI' + str(i) + '.jpg', frame)
	cv2.imshow('Original', out)
	i = i+1
		
#cap.release()
#cv2.destroyAllWindows()
