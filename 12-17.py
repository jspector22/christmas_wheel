import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP26, 95)
i = 0
reset_led = False
while True:
    pixels[i] = (10, 0, 0)
    time.sleep(0.05)
    i = i+1
    if i == 94:
        reset_led = True
        continue
    if reset_led == True:
        print("Reset")
        pixels.fill((0,0,0))
        i=0
        reset_led = False        
        continue