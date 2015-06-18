import RPi.GPIO as gpio
import time
from collections import OrderedDict
from random import randint

gpio.setmode(gpio.BCM)

on = 1
off = 0

leds = OrderedDict([(1,21), (2,20), (3,16), (4,19) ,(5,12) ,(6,26)])

gpio.setup(leds[1], gpio.OUT, initial=0)
gpio.setup(leds[2], gpio.OUT, initial=0)
gpio.setup(leds[3], gpio.OUT, initial=0)
gpio.setup(leds[4], gpio.OUT, initial=0)
gpio.setup(leds[5], gpio.OUT, initial=0)
gpio.setup(leds[6], gpio.OUT, initial=0)

def led(led, onOff):
    gpio.output(led, onOff)

def paint_line(onOff):
    for led in leds:
        gpio.output(leds[led], onOff)

def paint__r_triangle():
    led(leds[6], on)
    time.sleep(1.3)
    led(leds[6], off)
    paint_line(on)
    time.sleep(.3)
    paint_line(off)

def paint_waterfall():
    for led in leds:
        gpio.output(leds[led], on)
        print(led, leds[led])
        time.sleep(0.5)
        gpio.output(leds[led], off)
    print("Waterfall Painted")

def paint_square():
    paint_line(on)
    time.sleep(.3)
    paint_line(off)
    led(leds[1], on)
    led(leds[6], on)
    time.sleep(.8)
    paint_line(on)
    time.sleep(.3)
    paint_line(off)
    print("Square Painted")

def paint_circle():
    #first
    led(leds[3], on)
    led(leds[4], on)
    time.sleep(.3)
    led(leds[3], off)
    led(leds[4], off)
    #second
    led(leds[2], on)
    led(leds[5], on)
    time.sleep(.3)
    led(leds[2], off)
    led(leds[5], off)
    #third
    led(leds[1], on)
    led(leds[6], on)
    time.sleep(.3)
    led(leds[1], off)
    led(leds[6], off)
    #reverse

    #second
    led(leds[2], on)
    led(leds[5], on)
    time.sleep(.3)
    led(leds[2], off)
    led(leds[5], off)
    #third
    led(leds[3], on)
    led(leds[4], on)
    time.sleep(.3)
    led(leds[3], off)
    led(leds[4], off)
    print("Circle Painted")

def paint_random(iters, seconds):
    for x in range(0,iters):
        led_num = randint(1,6)
        led(leds[led_num], on)
        time.sleep(seconds)
        led(leds[led_num], off)
        print("Boom!", led_num)

def main():
    try:
        paint_line(on)
        time.sleep(2)
        paint_line(off)
        paint_waterfall()
        time.sleep(1)
        paint_random(103, .1)
        paint_square()
        while True:
            paint_circle()
            time.sleep(2)
        gpio.cleanup()
    
    except KeyboardInterrupt:
        gpio.cleanup()

    except RuntimeError:
        gpio.cleanup()

if __name__ == "__main__": main()
