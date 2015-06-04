import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

red = 18
yellow = 20
green = 21

gpio.setup(red, gpio.OUT, initial=0)
gpio.setup(yellow, gpio.OUT, initial=0)
gpio.setup(green, gpio.OUT, initial=0)

def red_to_green():
    gpio.output(red, 1)
    time.sleep(3)
    gpio.output(yellow, 1)
    time.sleep(0.2)
    gpio.output(red,0)
    time.sleep(0.3)
    gpio.output(yellow, 0)
    time.sleep(.1)
    gpio.output(green, 1)
    time.sleep(1)

def green_to_red():
    gpio.output(green, 1)
    time.sleep(3)
    gpio.output(yellow, 1)
    time.sleep(0.2)
    gpio.output(green,0)
    time.sleep(0.3)
    gpio.output(yellow, 0)
    time.sleep(.1)
    gpio.output(red, 1)
    time.sleep(1)
    
def main():
    try:
        while True:
            red_to_green()
            green_to_red()
        gpio.cleanup()
    
    except KeyboardInterrupt:
        gpio.cleanup()

    except RuntimeError:
        gpio.cleanup()

if __name__ == "__main__": main()
