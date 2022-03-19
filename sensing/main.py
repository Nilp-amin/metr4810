#usr/bin/etc python3

from machine import Pin, ADC
import time

LDR_THRESHOLD = 2000 

green_led = Pin(25, Pin.OUT)
laser = Pin(0, Pin.OUT)
ldr = ADC(28) 

def hardware_init():
    laser.on()
    green_led.off()

def average_ldr(samples):
    total = 0
    for _ in range(samples):
        total = total + ldr.read_u16()

    return total / samples 

if __name__ == "__main__":
    hardware_init()

    while True:
        ldr_reading = average_ldr(50)
        if ldr_reading < LDR_THRESHOLD:
            print(ldr_reading)
            green_led.on()
        else:
            green_led.off()