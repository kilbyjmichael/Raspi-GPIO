import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(21, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
    while True:
        input_state = gpio.input(21)
        if input_state == False:
            print("Connected")
            time.sleep(1)
        elif input_state == True:
            print("NOT CONNECTED!")
            time.sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()
