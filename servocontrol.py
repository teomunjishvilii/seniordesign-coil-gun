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
	
set_angle(24, pwm1)
set_angle(110, pwm2)

def translate_coords_to_angle(x,y):
	if(x == 0 and y == 0):
	  set_angle(10, pwm1)
	  time.sleep(1.5)
	  set_angle(128, pwm2)
	elif(x == 9 and y == 0):
	  set_angle(7, pwm1)
	  time.sleep(1.5)
	  set_angle(89, pwm2)
	elif(x == 10 and y == 0):
	  set_angle(7, pwm1)
	  time.sleep(1.5)
	  set_angle(85, pwm2)
	elif(x == 11 and y == 0):
	  set_angle(7, pwm1)
	  time.sleep(1.5)
	  set_angle(81, pwm2)
	else:
	  pwm1_angle = 9+(4*y)
	  pwm2_angle = 128-(4*x)
	  set_angle(pwm1_angle, pwm1)
	  time.sleep(1.5)
	  set_angle(pwm2_angle, pwm2)
	
	
def calculate_angle_with_grid(x, y):
	if(x == 0 and y == 0):
	  set_angle(10, pwm1)
	  time.sleep(1.5)
	  set_angle(127, pwm2)
	elif(x == 1 and y == 0):
	  set_angle(10, pwm1)
	  time.sleep(1.5)
	  set_angle(123, pwm2)
	elif(x == 2 and y == 0):
	  set_angle(9, pwm1)
	  time.sleep(1.5)
	  set_angle(119, pwm2)
	elif(x == 3 and y == 0):
	  set_angle(9, pwm1)
	  time.sleep(1.5)
	  set_angle(115, pwm2)
	elif(x == 4 and y == 0):
	  set_angle(9, pwm1)
	  time.sleep(1.5)
	  set_angle(111, pwm2)
	elif(x == 5 and y == 0):
	  set_angle(9, pwm1)
	  time.sleep(1.5)
	  set_angle(107, pwm2)
	elif(x == 6 and y == 0):
	  set_angle(9, pwm1)
	  time.sleep(1.5)
	  set_angle(103, pwm2)
	elif(x == 7 and y == 0):
	  set_angle(9, pwm1)
	  time.sleep(1.5)
	  set_angle(99, pwm2)
	elif(x == 8 and y == 0):
	  set_angle(9, pwm1)
	  time.sleep(1.5)
	  set_angle(94, pwm2)
	elif(x == 9 and y == 0):
	  set_angle(7, pwm1)
	  time.sleep(1.5)
	  set_angle(89, pwm2)
	elif(x == 10 and y == 0):
	  set_angle(7, pwm1)
	  time.sleep(1.5)
	  set_angle(85, pwm2)
	elif(x == 11 and y == 0):
	  set_angle(7, pwm1)
	  time.sleep(1.5)
	  set_angle(81, pwm2)
	  
      
	  
	elif(x == 0 and y == 1):
	  set_angle(14, pwm1)
	  time.sleep(1.5)
	  set_angle(128, pwm2)
	  
	elif(x == 0 and y == 2):
	  set_angle(18, pwm1)
	  time.sleep(1.5)
	  set_angle(128, pwm2)
	  time.sleep(1.5)
	  
	elif(x == 0 and y == 3):
	  set_angle(22, pwm1)
	  time.sleep(1.5)
	  set_angle(128, pwm2)
	  time.sleep(1.5)
	  
	elif(x == 0 and y == 4):
	  set_angle(26, pwm1)
	  time.sleep(1.5)
	  set_angle(128, pwm2)
	  time.sleep(1.5)
	   
translate_coords_to_angle(3,0)
#calculate_angle_with_grid(0, 4)
time.sleep(2)
pwm1.stop()
pwm2.stop()
GPIO.cleanup()

