import RPi.GPIO as gpio
import time
from collections import OrderedDict

gpio.setmode(gpio.BCM)

on = 1
off = 0

leds = OrderedDict([('1',21), ('2',20), ('3',16), ('4',19) ,('5',12) ,('6',26)])

gpio.setup(leds['1'], gpio.OUT, initial=0)
gpio.setup(leds['2'], gpio.OUT, initial=0)
gpio.setup(leds['3'], gpio.OUT, initial=0)
gpio.setup(leds['4'], gpio.OUT, initial=0)
gpio.setup(leds['5'], gpio.OUT, initial=0)
gpio.setup(leds['6'], gpio.OUT, initial=0)

def led(led, onOff):
    gpio.output(led, onOff)

def paint_line(onOff):
    for led in leds:
        gpio.output(leds[led], onOff)


def paint_waterfall():
    for led in leds:
        gpio.output(leds[led], on)
        print(led, leds[led])
        time.sleep(0.5)
        gpio.output(leds[led], off)

def paint_square():
    paint_line(on)
    time.sleep(.3)
    paint_line(off)
    led(leds['1'], on)
    led(leds['6'], on)
    time.sleep(.8)
    paint_line(on)
    time.sleep(.3)
    paint_line(off)

def main():
    try:
        #paint_line(on)
        #time.sleep(2)
        #paint_line(off)
        #paint_waterfall()
        #time.sleep(1)
        while True:
            paint_waterfall()
            time.sleep(2)
        gpio.cleanup()
    
    except KeyboardInterrupt:
        gpio.cleanup()

    except RuntimeError:
        gpio.cleanup()

if __name__ == "__main__": main()
