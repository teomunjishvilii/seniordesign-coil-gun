#!/usr/bin/python

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

def detect_red(image):
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	lower_red1 = np.array([0, 200, 30])
	upper_red1 = np.array([10, 255, 255])
	lower_red2 = np.array([170, 200, 30])
	upper_red2 = np.array([180, 255, 255])
	
	mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
	mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
	
	mask = cv2.bitwise_or(mask1, mask2)
	res = cv2.bitwise_and(image, image, mask=mask)
		
	kernel = np.ones((5,5), np.uint8)
	res = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	res = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	
	return res
def main():
	i = 0
	while i<1:
		
		image_name = 'captureCEI' + str(i) + '.jpg'
		image = cv2.imread(image_name)
		cv2.imshow('Original', image)
		
		mask = detect_red(image)
		cv2.imshow('Red Detected', mask)
		
		#height, width, channels = mask.shape
		
		#pixel_coordinates = []
		
		#for y in range(height):
			#for x in range(width):
				#pixel_color = image[y, x]
				#if pixel_color[0] > pixel_color[1] and pixel_color[0] > pixel_color[2]:
					#print(pixel_color[0], pixel_color[1], pixel_color[2])
					#print(x,y) 
					#pixel_coordinates.append((x,y))
				#break
						
		pixel_coordinates = np.column_stack(np.where(mask))
		print(pixel_coordinates)
		
		if len(pixel_coordinates) > 0:
			mean_x = int(np.mean(pixel_coordinates[:, 1]))
			mean_y = int(np.mean(pixel_coordinates[:, 0]))
			
			print((mean_x, mean_y))
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		
		i = i+1
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	
if __name__ == "__main__":
	main()
