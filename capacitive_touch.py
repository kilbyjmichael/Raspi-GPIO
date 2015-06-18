import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(21, gpio.IN)
gpio.setup(4, gpio.OUT, initial=0)

try:
    while True:
        input_state = gpio.input(21)
        if not input_state:
            print("Not Input Stat3 Detected")
            gpio.output(4, 1)
            time.sleep(.3)
            gpio.output(4, 0)

except KeyboardInterrupt:
    gpio.cleanup()
