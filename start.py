#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from cam import capture_image
from capturecoords import main
from servocontrol import translate_coords_to_angle, set_angle
from shoot import pin_on, pin_off
import time;

servo_1_pin = 13
servo_2_pin = 12
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_1_pin, GPIO.OUT)
GPIO.setup(servo_2_pin, GPIO.OUT)
# Set up the GPIO pin as an output 
GPIO.setup(led_pin, GPIO.OUT)


GPIO.output(servo_1_pin, True)
GPIO.output(servo_2_pin, True) 
GPIO.setwarnings(False)
pwm1 = GPIO.PWM(servo_1_pin, 50)  # PWM frequency is 50Hz
pwm2 = GPIO.PWM(servo_2_pin, 50)  # PWM frequency is 50Hz 
pwm1.start(2.5)  # Initialization
pwm2.start(2.5)  # Initialization

set_angle(100, pwm1)
set_angle(90, pwm2) 

capture_image()
coords = main()
if(coords is not None):
	[x, y] = coords
	translate_coords_to_angle(x, y)
	time.sleep(4)
	pwm1.stop()
	pwm2.stop()
	pin_on(led_pin)
	time.sleep(3)
	pin_off(led_pin)


pwm1.stop()
pwm2.stop()
pin_off(17)
GPIO.cleanup()
