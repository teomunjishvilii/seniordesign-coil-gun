#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from cam import capture_image
from capturecoords import main
from servocontrol import translate_coords_to_angle, set_angle
import time;

servo_1_pin = 13
servo_2_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_1_pin, GPIO.OUT)
GPIO.setup(servo_2_pin, GPIO.OUT)
GPIO.output(servo_1_pin, True)
GPIO.output(servo_2_pin, True) 
GPIO.setwarnings(False)
pwm1 = GPIO.PWM(servo_1_pin, 50)  # PWM frequency is 50Hz
pwm2 = GPIO.PWM(servo_2_pin, 50)  # PWM frequency is 50Hz
pwm1.start(2.5)  # Initialization
pwm2.start(2.5)  # Initialization

set_angle(24, pwm1)
set_angle(110, pwm2)

capture_image()
[x, y] = main()
translate_coords_to_angle(x, y)

time.sleep(2)
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
