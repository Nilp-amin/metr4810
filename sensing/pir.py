#usr/bin/env python3

from machine import Pin, ADC

import time

def hardware_init():
    global green_led
    global pir_sensor
    
    green_led = Pin(25, Pin.OUT)
    green_led.off()

    pir_sensor = Pin(28, Pin.IN)

if __name__ == "__main__":
    hardware_init()

    while(1):
        if pir_sensor.value():
            green_led.on()
        else:
            green_led.off()