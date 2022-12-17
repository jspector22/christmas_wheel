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

num_pixels = 95  # Update this to match the number of LEDs.
SPEED = 1  # Increase to slow down the rainbow. Decrease to speed it up.
pixel_pin = board.GP26  # This is the default pin on the 5x5 NeoPixel Grid BFF.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(board.GP26, 95)


i = 0
pix_position = i % len(pixels)
reset_led = False

while True:
    pixels[pix_position] = (10, 0, 0)
    time.sleep(0.05)
    i += 1 #only lights up pixel 0
    pix_position += 1 #loops but goes out of range
    if i == len(pixels):
        reset_led = True
        continue
    if reset_led == True:
        print("Reset")
        pixels.fill((0,0,0))
        i=0
        reset_led = False        
        continue
    #print("Angular Velocity (rad/s): {}".format(SENSOR.gyro[2]))
    #print(round(SENSOR.gyro[2], 0))
    #print()
    #time.sleep(1)
    # run from 0 to 255