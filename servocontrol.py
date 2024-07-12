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
	
set_angle(100, pwm1)
set_angle(90, pwm2)

def translate_coords_to_angle(x,y):
	verti = 84
	horiz = 113

	
	if(x >= 0 and x <= 11 and y < 8):
		print("2nd here")
		pwm1_angle = verti+(1.2*y)
		pwm2_angle = horiz-(1.4*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	elif(x >= 0 and x <= 11 and y >= 8):
		print("4nd here")
		pwm1_angle = verti+(1.2*y)
		pwm2_angle = horiz-(1.4*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	elif(x >= 0 and x < 12 and y >= 16):
		print("3rd here")
		pwm1_angle = verti+(1.1*y)
		pwm2_angle = horiz-(1.2*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	
	elif(x >= 12 and x < 19 and y < 8):
		pwm1_angle = verti+(1.2*y)
		pwm2_angle = horiz-(1.5*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	elif(x >= 12 and x < 19 and y >= 8):
		pwm1_angle = verti+(1.2*y)
		pwm2_angle = horiz-(1.5*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	elif(x >= 19 and x < 25 and y < 8):
		print("x 19 25 y < 8")
		pwm1_angle = verti+(1.2*y)
		pwm2_angle = horiz-(1.5*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
		
	elif(x >= 19 and x < 29 and y >= 8):
		print("x 19-28 and y >= 8")
		pwm1_angle = verti+(1.1*y)
		pwm2_angle = horiz-(1.6*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
		
	elif(x >= 25 and x < 31 and y < 8):
		print("x 25 31 y < 8")
		pwm1_angle = verti+(1.2*y)
		pwm2_angle = horiz-(1.6*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
		
	elif(x >= 25 and x < 31 and y >= 8):
		pwm1_angle = verti+(1.2*y)
		pwm2_angle = horiz-(1.6*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
		
	elif(x >= 31 and x < 34 and y < 8):
		print("x 31 34 y < 8")
		pwm1_angle = verti+(1.3*y)
		pwm2_angle = horiz-(1.6*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	elif(x >= 31 and x < 34 and y >= 8):
		pwm1_angle = verti+(y*1.2)
		pwm2_angle = horiz-(1.6*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)	
	elif(x >= 34 and x < 44 and y < 8):
		pwm1_angle = verti+(y*1.2)
		pwm2_angle = horiz-(1.6*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	elif(x >= 34 and x < 44 and y >= 8):
		print("34 44 y>8")
		pwm1_angle = verti+(y*1.2)
		pwm2_angle = horiz-(1.6*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	elif(x >= 44):
		print("yes")
		pwm1_angle = verti+(y*1.2)
		pwm2_angle = horiz-(1.6*(x-(x/3)))
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)


def translate_coords_to_angle3(x,y):
	if(x < 24 and y < 7 ):
	  print("Top Left quarter")
	  pwm1_angle = 84+(6*y)
	  pwm2_angle = 113-(0.3*x)
	  set_angle(pwm1_angle, pwm1)
	  time.sleep(1.5)
	  set_angle(pwm2_angle, pwm2)
	  
	elif(x < 24 and y >= 7 and y < 10):
	  print("Top left quarter")
	  pwm1_angle = 87+(0.6*y)
	  pwm2_angle = 106.5-(0.78*x)
	  set_angle(pwm1_angle, pwm1)
	  time.sleep(1.5)
	  set_angle(pwm2_angle, pwm2)
	  
	if(x == 18 and y >= 7):
		pwm1_angle = 87+(0.65*y)
		pwm2_angle = 106.5-(0.65*x)
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
	elif (x <= 17 and y == 7):
		pwm1_angle = 87+(0.6*y)
		pwm2_angle = 106.5-(0.2*x)
		set_angle(pwm1_angle, pwm1)
		time.sleep(1.5)
		set_angle(pwm2_angle, pwm2)
		
	  
	elif(x >= 24 and y >= 10):
	  print("Right bottom quarter")
	  pwm1_angle = 87+(0.9*y)
	  pwm2_angle = 106.5-(0.85*x)
	  set_angle(pwm1_angle, pwm1)
	  time.sleep(1.5)
	  set_angle(pwm2_angle, pwm2)
	elif(x >= 24 and x < 35 and y < 10):
	  print("Top Right quarter")
	  pwm1_angle = 87+(0.72*y)
	  pwm2_angle = 106.5-(0.88*x)
	  set_angle(pwm1_angle, pwm1)
	  time.sleep(1.5)
	  set_angle(pwm2_angle, pwm2)
	  if(x == 26 and y ==7):
		  pwm1_angle = 87+(0.72*y)
		  pwm2_angle = 106.5-(0.75*x)
		  set_angle(pwm1_angle, pwm1)
		  time.sleep(1.5)
		  set_angle(pwm2_angle, pwm2)

	  
	elif(x >= 35 and y < 10):
	  print("Right Top quarter")
	  #if(x == 34):
		  #pwm1_angle = 87+(0.8*y)
		  #pwm2_angle = 106.5-(0.9*x)
		  #set_angle(pwm1_angle, pwm1)
		  #time.sleep(1.5)
		  #set_angle(pwm2_angle, pwm2)
	  pwm1_angle = 87+(0.75*y)
	  pwm2_angle = 106.5-(0.9*x)
	  set_angle(pwm1_angle, pwm1)
	  time.sleep(1.5)
	  set_angle(pwm2_angle, pwm2)
	elif(x >= 12 and x < 24 and y >= 10):
	  print("Bottom Left quarter (Right Half)")
	  if(x == 23):
		  pwm1_angle = 87+(0.8*y)
		  pwm2_angle = 106.5-(0.9*x)
		  set_angle(pwm1_angle, pwm1)
		  time.sleep(1.5)
		  set_angle(pwm2_angle, pwm2)
		
	  pwm1_angle = 87+(0.8*y)
	  pwm2_angle = 106.5-(0.8*x)
	  set_angle(pwm1_angle, pwm1)
	  time.sleep(1.5)
	  set_angle(pwm2_angle, pwm2)
	elif(x < 12 and x < 24 and y >= 10):
	  print("Bottom Left quarter (Left Half)")
	  pwm1_angle = 87+(0.9*y)
	  pwm2_angle = 106.5-(0.2*x)
	  set_angle(pwm1_angle, pwm1)
	  time.sleep(1.5)
	  set_angle(pwm2_angle, pwm2)
	
def translate_coords_to_angle2(x,y):
	if(x == 0 and y == 0):
	  set_angle(87, pwm1)
	  time.sleep(1.5)
	  set_angle(106.5, pwm2)
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
		if(x < 24):
		  print("Left half")
		  pwm1_angle = 9+(1*y)
		  pwm2_angle = 128-(0.85*x)
		  set_angle(pwm1_angle, pwm1)
		  time.sleep(1.5)
		  set_angle(pwm2_angle, pwm2)
		elif(x >= 24):
		  print("Right half")
		  pwm1_angle = 9+(0.88*y)
		  pwm2_angle = 128-(0.96*x)
		  set_angle(pwm1_angle, pwm1)
		  time.sleep(1.5)
		  set_angle(pwm2_angle, pwm2)
#	  pwm1_angle = 9+(1*y)
#	  pwm2_angle = 128-(0.75*x)
#	  set_angle(pwm1_angle, pwm1)
#	  time.sleep(1.5)
#	  set_angle(pwm2_angle, pwm2)
	
	
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
	   
#translate_coords_to_angle(0,0)
#calculate_angle_with_grid(0, 4)
time.sleep(2)
pwm1.stop()
pwm2.stop()
GPIO.cleanup()

