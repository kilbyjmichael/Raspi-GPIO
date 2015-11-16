import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(18, gpio.OUT, initial=0)
gpio.setup(24, gpio.IN, pull_up_down=gpio.PUD_UP)

button_was_pushed = False

try:
    while True:
        input_state = gpio.input(24)
        if button_was_pushed == True and input_state == False:
            button_was_pushed = False
            #print(button_was_pushed)
            print("Pressed")
            time.sleep(0.2)
            gpio.output(18, 0)
            print("LED ->> OFF")
        elif button_was_pushed == False and input_state == False:
            button_was_pushed = True
            #print(button_was_pushed)
            print("Pressed")
            time.sleep(0.2)
            gpio.output(18, 1)
            print("LED ->> ON")
        #print(input_state,button_was_pushed)
            
except KeyboardInterrupt:
    gpio.cleanup()
