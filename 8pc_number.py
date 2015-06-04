import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

leds = {'top' : 12,
        'bottom' : 18,
        'middle' : 16,
        'top_left' : 20,
        'top_right' : 21,
        'bottom_left' : 19,
        'bottom_right' : 13,
        'dot' : 26}

message = [2,1,7,3,6,9,8,1,1,0]

on = 1
off = 0

gpio.setup(leds['top'], gpio.OUT, initial=0)
gpio.setup(leds['bottom'], gpio.OUT, initial=0)
gpio.setup(leds['middle'], gpio.OUT, initial=0)
gpio.setup(leds['top_left'], gpio.OUT, initial=0)
gpio.setup(leds['top_right'], gpio.OUT, initial=0)
gpio.setup(leds['bottom_left'], gpio.OUT, initial=0)
gpio.setup(leds['bottom_right'], gpio.OUT, initial=0)
gpio.setup(leds['dot'], gpio.OUT, initial=0)

def test():
    for led in leds:
        print(led, leds[led])
        gpio.output(leds[led], on)
        time.sleep(2)
        gpio.output(leds[led], off)
        

def one(on_off):
    gpio.output(leds['top_right'], on_off)
    gpio.output(leds['bottom_right'], on_off)

def two(on_off):
    gpio.output(leds['top'], on_off)
    gpio.output(leds['top_right'], on_off)
    gpio.output(leds['middle'], on_off)
    gpio.output(leds['bottom_left'], on_off)
    gpio.output(leds['bottom'], on_off)
    
def three(on_off):
    gpio.output(leds['top'], on_off)
    gpio.output(leds['top_right'], on_off)
    gpio.output(leds['middle'], on_off)
    gpio.output(leds['bottom_right'], on_off)
    gpio.output(leds['bottom'], on_off)

def four(on_off):
    gpio.output(leds['top_left'], on_off)
    gpio.output(leds['middle'], on_off)
    gpio.output(leds['top_right'], on_off)
    gpio.output(leds['bottom_right'], on_off)

def five(on_off):
    gpio.output(leds['top'], on_off)
    gpio.output(leds['top_left'], on_off)
    gpio.output(leds['middle'], on_off)
    gpio.output(leds['bottom_right'], on_off)
    gpio.output(leds['bottom'], on_off)

def six(on_off):
    gpio.output(leds['top'], on_off)
    gpio.output(leds['top_left'], on_off)
    gpio.output(leds['middle'], on_off)
    gpio.output(leds['bottom_right'], on_off)
    gpio.output(leds['bottom_left'], on_off)
    gpio.output(leds['bottom'], on_off)

def seven(on_off):
    gpio.output(leds['top'], on_off)
    gpio.output(leds['top_right'], on_off)
    gpio.output(leds['bottom_right'], on_off)

def eight(on_off):
    gpio.output(leds['top'], on_off)
    gpio.output(leds['top_left'], on_off)
    gpio.output(leds['top_right'], on_off)
    gpio.output(leds['middle'], on_off)
    gpio.output(leds['bottom_right'], on_off)
    gpio.output(leds['bottom_left'], on_off)
    gpio.output(leds['bottom'], on_off)

def nine(on_off):
    gpio.output(leds['top'], on_off)
    gpio.output(leds['top_left'], on_off)
    gpio.output(leds['top_right'], on_off)
    gpio.output(leds['middle'], on_off)
    gpio.output(leds['bottom_right'], on_off)

def zero(on_off):
    gpio.output(leds['top'], on_off)
    gpio.output(leds['bottom_left'], on_off)
    gpio.output(leds['bottom_right'], on_off)
    gpio.output(leds['top_left'], on_off)
    gpio.output(leds['top_right'], on_off)
    gpio.output(leds['bottom'], on_off)

def dash(on_off):
    gpio.output(leds['middle'], on_off)

numbers = {1 : one,
           2 : two,
           3 : three,
           4 : four,
           5 : five,
           6 : six,
           7 : seven,
           8 : eight,
           9 : nine,
           0 : zero}

def flash_digit(digit):
    digit(on)
    time.sleep(.5)
    digit(off)
    time.sleep(.1)

def main():
    try:
        for number in message:
            print(number)
            flash_digit(numbers[number])
        gpio.cleanup()
    
    except KeyboardInterrupt:
        gpio.cleanup()

    except RuntimeError:
        gpio.cleanup()

if __name__ == "__main__": main()
