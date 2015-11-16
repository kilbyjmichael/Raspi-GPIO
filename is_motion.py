import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(18, gpio.OUT, initial=0)

try:
    gpio.output(18, 1)
    time.sleep(5)
    gpio.output(18, 0)
    time.sleep(2)

except KeyboardInterrupt:
    gpio.cleanup()
