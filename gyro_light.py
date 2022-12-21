import time
import random
import board
import my_l3gd20
import busio
from rainbowio import colorwheel
import neopixel

#Gyroscope config
SDA = board.GP20
SCL = board.GP21
I2C = busio.I2C(SCL, SDA)
SENSOR = my_l3gd20.L3GD20_I2C(I2C, address=0x6B)


#Neopixel setup
num_pixels = 95
sleep_interval_seconds = 0.054 # time in seconds to sleep between each pixel light up.
pixel_pin = board.GP26 
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(board.GP26, num_pixels)
pixel_index = 0

#Gyroscope bound
offset = 0.075

def bound(gyro_value):
    if gyro_value < -5 + offset:
        return -5
    if gyro_value > 5:
        return 5
    return gyro_value

#Gyroscope Calibration of bias
def calibrate(gyro_value):
    return gyro_value + offset

#COLOR config
RED = (255, 0, 0)
ORANGE = (230, 30, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (138, 43, 226)
COLORS = (RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET)


while True:     
    gyro_value = SENSOR.gyro[2]
    gyro_value = calibrate(gyro_value)
    gyro_value = bound(gyro_value)    
    pixel_index += round(SENSOR.gyro[2])               
    print(pixel_index)
    time.sleep(sleep_interval_seconds)
    pixels.fill((0,0,0))
    
#full rotation
    if abs(pixel_index) >= num_pixels:
        pixel_index = 0
        pixels[pixel_index] = (10, 10, 10)    
        print("Reset")
        
#color wheel division
    if abs(pixel_index) <= 18:
        pixels[pixel_index] = (RED)
    if abs(pixel_index) in range(19,38):
        pixels[pixel_index] = (ORANGE)
    if abs(pixel_index) in range(38,56):
        pixels[pixel_index] = (YELLOW)
    if abs(pixel_index) in range(56,75):
        pixels[pixel_index] = (GREEN)
    if abs(pixel_index) in range(75,94):
        pixels[pixel_index] = (BLUE) 
    #print("Angular Velocity (rad/s): {}".format(SENSOR.gyro[2]))