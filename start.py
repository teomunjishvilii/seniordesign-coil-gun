from cam import capture_image
from capturecoords import main
from servocontrol import translate_coords_to_angle

capture_image()
[x, y] = main()
translate_coords_to_angle(x, y)
