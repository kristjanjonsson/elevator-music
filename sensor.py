import RPi.GPIO as GPIO
import time
import os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
            reading += 1

    return reading

class Sensor:
    """Class for reading the light sensor and comparing against older measurements."""

    def __init__(self):
        self.last_reading = self.get_light_sensor_reading()
        self.current_reading = self.get_light_sensor_reading()
        self.threshold = 100

    def get_light_sensor_reading(self):
        return RCtime(18) # 18 refers to GPIO pin #18 on RPi

    def significant_change_since_last_reading(self):
        if (abs(self.current_reading - self.last_reading) > self.threshold):
            return True
