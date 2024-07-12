import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that you are using to control the TC4420 driver
pin = 17

# Set up the GPIO pin as an output 
GPIO.setup(pin, GPIO.OUT)

# Function to turn the MOFET on
def pin_on(pin):
    GPIO.output(pin, GPIO.HIGH)

# Function to turn the MOSFET off
def pin_off(pin):
    GPIO.output(pin, GPIO.LOW)
