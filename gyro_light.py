import time
import random
import board
import my_l3gd20
import busio
from rainbowio import colorwheel
import neopixel

SDA = board.GP20
SCL = board.GP21
# Hardware I2C setup:
I2C = busio.I2C(SCL, SDA)  # uses board.SCL and board.SDA
# Initializes L3GD20 object using default range, 250dps
SENSOR = my_l3gd20.L3GD20_I2C(I2C, address=0x6B)

# SPEED = 1  # Increase to slow down the rainbow. Decrease to speed it up.

num_pixels = 95  # Update this to match the number of LEDs.
sleep_interval_seconds = 0.0535 # time in seconds to sleep between each pixel light up.
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
red = range(0,100)
green = range(0,100)
blue = range(0,100)
pixel_index = 0

while True:
    if abs(pixel_index) < num_pixels:
        
        
        gyro_value = SENSOR.gyro[2]
        gyro_value = calibrate(gyro_value)
        gyro_value = bound(gyro_value)      
        pixels[pixel_index] = (random.randrange(len(red)), random.randrange(len(green)), random.randrange(len(blue)))    
        pixel_index += round(SENSOR.gyro[2])
        print(pixel_index)
        time.sleep(sleep_interval_seconds)
        pixels.fill((0,0,0))
    if abs(pixel_index) >= num_pixels:
        pixel_index = 0
        pixels[pixel_index] = (20, 0, 0)    
        print("Reset")        
    #print("Angular Velocity (rad/s): {}".format(SENSOR.gyro[2]))
