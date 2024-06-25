
#!/usr/bin/python

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

def detect_red(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 200, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 200, 70])
    upper_red2 = np.array([180, 255, 255])
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    mask = cv2.bitwise_or(mask1, mask2)
    res = cv2.bitwise_and(image, image, mask=mask)
        
    kernel = np.ones((5,5), np.uint8)
    res = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    res = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    return res

def grid_image(image, grid_size_x, grid_size_y, num_grids_x, num_grids_y):
    height, width = image.shape
    grids = {}
    
    for y in range(num_grids_y):
        for x in range(num_grids_x):
            start_x = x * grid_size_x
            start_y = y * grid_size_y
            end_x = start_x + grid_size_x
            end_y = start_y + grid_size_y
            
            grid_pixels = image[start_y:end_y, start_x:end_x]
            grids[(x, y)] = grid_pixels
            
    return grids

def draw_grid(image, grid_size_x, grid_size_y, num_grids_x, num_grids_y):
    for x in range(1, num_grids_x):
        start_x = x * grid_size_x
        cv2.line(image, (start_x, 0), (start_x, image.shape[0]), (0, 255, 0), 2)
    for y in range(1, num_grids_y):
        start_y = y * grid_size_y
        cv2.line(image, (0, start_y), (image.shape[1], start_y), (0, 255, 0), 2)
    return image

def main():
    i = 0
    grid_x = 12
    grid_y = 9
    while i < 1:
        image_name = 'captureCEI' + str(i) + '.jpg'
        image = cv2.imread(image_name)
        
        mask = detect_red(image)
        
        height, width, _ = image.shape
        grid_size_x = width // grid_x
        grid_size_y = height // grid_y
        
        grids = grid_image(mask, grid_size_x, grid_size_y, grid_x, grid_y)
        
        max_pixel_count = 0
        max_grid_key = None
        max_grid_coordinates = None
        
        for key, grid in grids.items():
            pixel_coordinates = np.column_stack(np.where(grid))
            pixel_count = len(pixel_coordinates)
            
            if pixel_count > max_pixel_count:
                max_pixel_count = pixel_count
                max_grid_key = key
                max_grid_coordinates = pixel_coordinates
                
        if max_grid_coordinates is not None:
            mean_x = int(np.mean(max_grid_coordinates[:, 1])) + max_grid_key[0] * grid_size_x
            mean_y = int(np.mean(max_grid_coordinates[:, 0])) + max_grid_key[1] * grid_size_y
            print(f"Grid {max_grid_key}: means = ({mean_x}, {mean_y})")
        
        image_with_grid = draw_grid(image.copy(), grid_size_x, grid_size_y, grid_x, grid_y)
        cv2.imshow('Original with Grid', image_with_grid)
        cv2.imshow('Red Detected', mask)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        i += 1
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


