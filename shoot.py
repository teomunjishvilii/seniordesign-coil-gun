import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that you are using to control the TC4420 driver
mosfet_driver_pin = 17

# Set up the GPIO pin as an output
GPIO.setup(mosfet_driver_pin, GPIO.OUT)

# Function to turn the MOSFET on
def mosfet_on():
    GPIO.output(mosfet_driver_pin, GPIO.HIGH)

# Function to turn the MOSFET off
def mosfet_off():
    GPIO.output(mosfet_driver_pin, GPIO.LOW)

mosfet_on()
print("MOSFET is ON")
time.sleep(4)
mosfet_off()
print("MOSFET is OFF")

GPIO.cleanup()
