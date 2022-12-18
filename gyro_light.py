import time
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
sleep_interval_seconds = 0.05 # time in seconds to sleep between each pixel light up.
pixel_pin = board.GP26  # This is the default pin on the 5x5 NeoPixel Grid BFF.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(board.GP26, num_pixels)

pixel_index = 0

while True:
    pixels[pixel_index] = (10, 0, 0)
    time.sleep(sleep_interval_seconds)
    pixel_index += 1 #only lights up pixel 0
    if pixel_index > num_pixels:
        print("Reset")
        pixels.fill((0,0,0))
        pixel_index = 0
    #print("Angular Velocity (rad/s): {}".format(SENSOR.gyro[2]))
    #print(round(SENSOR.gyro[2], 0))
    #print()
    #time.sleep(1)
    # run from 0 to 255