#!/usr/bin/python

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

def detect_red(image):
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
	#lower_red = np.array([100, 170, 190])
	#upper_red = np.array([255, 255, 255])
	
	lower_red1 = np.array([0, 200, 30])
	upper_red1 = np.array([10, 255, 255])
	lower_red2 = np.array([170, 200, 30])
	upper_red2 = np.array([180, 255, 255])
	
	mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
	mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
	
	#mask = cv2.inRange(hsv, lower_red, upper_red)
	mask = cv2.bitwise_or(mask1, mask2)
	
	res = cv2.bitwise_and(image, image, mask=mask)
	
	return res

def main():
	i = 0
	while i<1:
		
		image_name = 'captureCEI' + str(i) + '.jpg'

		image_path = image_name
		image = cv2.imread(image_path)
		
		red_detected = detect_red(image)
		

		cv2.imshow('Original', image)
		cv2.imshow('Red Detected', red_detected)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		
		i = i+1
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	
if __name__ == "__main__":
	main()
