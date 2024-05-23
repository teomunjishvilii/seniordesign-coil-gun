#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setwarnings(False)

servo_pin = 13
pwm = GPIO.PWM(servo_pin, 50)  # PWM frequency is 50Hz
pwm.start(2.5)  # Initialization
GPIO.output(servo_pin, True)

def set_angle(angle):
	duty = float(angle) / 18.0 + 2.5
	pwm.ChangeDutyCycle(duty)

try:
    while True:
      for angle in range(0, 180, 20):
	      set_angle(angle)
	      time.sleep(1)
	      
      for angle in range(180, 0, -20):
	      set_angle(angle)
	      time.sleep(1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()











































































































































