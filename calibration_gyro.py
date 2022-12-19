# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import my_l3gd20
import busio
import neopixel

SDA = board.GP20
SCL = board.GP21
# Hardware I2C setup:
I2C = busio.I2C(SCL, SDA)  

SENSOR = my_l3gd20.L3GD20_I2C(I2C, address=0x6B)
num_pixels = 95  # Update this to match the number of LEDs.
sleep_interval_seconds = 0.05 # time in seconds to sleep between each pixel light up.
pixel_pin = board.GP26  # This is the default pin on the 5x5 NeoPixel Grid BFF.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(board.GP26, num_pixels)

offset = 0.075

def bound(gyro_value):
    if gyro_value < -5 + offset:
        return -5
    if gyro_value > 5:
        return 5
    return gyro_value

def calibrate(gyro_value):
    return gyro_value + offset

#takes num between -5:5 and translates to 0-94 as int
def map_to_px_rng(gyro_value): 
    gyro_value = gyro_value + 5
    gyro_value = gyro_value * 9.4
    gyro_value = round(gyro_value, 0)
    return int(gyro_value)

   
while True:
    gyro_value = SENSOR.gyro[2]
    gyro_value = calibrate(gyro_value)
    gyro_value = bound(gyro_value)
    gyro_value = map_to_px_rng(gyro_value)
    time.sleep(0.1)
    pixels[gyro_value] = (10, 10, 10)
    time.sleep(sleep_interval_seconds)
    pixels.fill((0,0,0))