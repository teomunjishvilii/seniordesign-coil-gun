#!/usr/bin/python
import RPi.GPIO as GPIO
import time

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


def set_angle(angle, pwm):
	duty = float(angle) / 18.0 + 2.5
	pwm.ChangeDutyCycle(duty)
	
def calculate_angle_with_coords(x, y):
	x_angle = (x/108)*(x)
	duty1 = float(x_angle) / 18.0 + 2.5
	pwm2.ChangeDutyCycle(duty1)
	time.sleep(2)
	
	y_angle = y/7.6
	duty2 = float(y_angle) / 18.0 + 2.5
	pwm1.ChangeDutyCycle(duty2)

try:
    while True: #(262, 185)
      set_angle(24, pwm1)
      set_angle(110, pwm2)
      #time.sleep(2)
      #calculate_angle_with_coords(262, 185)
    
      #for angle in range(0, 60, 10):
	      #set_angle(angle, pwm1)
	      #time.sleep(1)
	      
      #for angle in range(0, 60, 10):	
	      #set_angle(angle, pwm2)
	      #time.sleep(1)
except KeyboardInterrupt:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

