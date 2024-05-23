#!/usr/bin/python

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

def main():
	i = 0
	while i<1:
		
		image_name = 'captureLED' + str(i) + '.jpg'
		image = cv2.imread(image_name)
		cv2.imshow('Original', image)
		
		lower_bound = np.array([100, 200, 200])
		upper_bound = np.array([255, 255, 255])
		
		height, width, channels = image.shape
		
		pixel_coordinates = []
		
		for y in range(height):
			for x in range(width):
				pixel_color = image[y, x]
				if all(lower_bound <= pixel_color) and all(pixel_color <= upper_bound):
					if pixel_color[0] > pixel_color[1] and pixel_color[0] > pixel_color[2]: 
						pixel_coordinates.append((x,y))
					
		
		mean_x = int(sum(x for x, y in pixel_coordinates) / len(pixel_coordinates))
		mean_y = int(sum(y for x, y in pixel_coordinates) / len(pixel_coordinates))
		
		print((mean_x, mean_y))
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		
		i = i+1
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	
if __name__ == "__main__":
	main()
