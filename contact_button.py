import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(18, gpio.OUT, initial=0)
gpio.setup(21, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
    while True:
        input_state = gpio.input(21)
        if input_state == False:
            print("Connected")
            gpio.output(18, 0)
            time.sleep(.5)
        elif input_state == True:
            print("NOT CONNECTED!")
            gpio.output(18, 1)
            time.sleep(.5)
            
except KeyboardInterrupt:
    gpio.cleanup()
