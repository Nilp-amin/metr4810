#usr/bin/etc python3

from machine import Pin, ADC, I2C

from vl53l0x import VL53L0X

LDR_THRESHOLD = 2000 


def hardware_init():
    global ldr
    global green_led
    global vl53l0x

    ldr = ADC(28) 

    i2c = I2C(0, scl=Pin(1), sda=Pin(0))
    vl53l0x = VL53L0X(i2c)

    green_led = Pin(25, Pin.OUT)
    green_led.off()


def average_ldr(samples):
    total = 0
    for _ in range(samples):
        total = total + ldr.read_u16()

    return total / samples 

def test_ldr():
    while True:
        ldr_reading = average_ldr(50)
        if ldr_reading < LDR_THRESHOLD:
            print(ldr_reading)
            green_led.on()
        else:
            green_led.off()

def test_tof():
    while(1):
        print("Hello world")

if __name__ == "__main__":
    hardware_init()

    test_tof()