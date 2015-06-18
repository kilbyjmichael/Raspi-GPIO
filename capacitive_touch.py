import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(21, gpio.IN)

try:
    while True:
        input_state = gpio.input(21)
        if not input_state:
            print("Not Input Stat3 Detected")
            print("\a")

except KeyboardInterrupt:
    gpio.cleanup()
