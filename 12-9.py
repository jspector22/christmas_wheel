import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP26, 95)

i=0

while i <= range(len(pixels)):
  
    if i < 94:
        i += 1
        pixels[i] = (10, 0, 0)
        time.sleep(0.1)
    else:
        i = 0
        pixels.fill((0,10,0))
        time.sleep(1)
        

