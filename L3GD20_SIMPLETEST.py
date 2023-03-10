# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import my_l3gd20
import busio

SDA = board.GP20
SCL = board.GP21
# Hardware I2C setup:
I2C = busio.I2C(SCL, SDA)  # uses board.SCL and board.SDA
# Initializes L3GD20 object using default range, 250dps
SENSOR = my_l3gd20.L3GD20_I2C(I2C, address=0x6B)
# Initialize L3GD20 object using a custom range and output data rate (ODR).
#SENSOR = my_l3gd20.L3GD20_I2C(
#   I2C, rng=my_l3gd20.L3DS20_RANGE_500DPS, rate=my_l3gd20.L3DS20_RATE_200HZ
# )

# Possible values for rng are:
# adafruit_l3gd20.L3DS20_Range_250DPS, 250 degrees per second. Default range
# adafruit_l3gd20.L3DS20_Range_500DPS, 500 degrees per second
# adafruit_l3gd20.L3DS20_Range_2000DPS, 2000 degrees per second

# Possible values for rate are:
# adafruit_l3gd20.L3DS20_RATE_100HZ, 100Hz data rate. Default data rate
# adafruit_l3gd20.L3DS20_RATE_200HZ, 200Hz data rate
# adafruit_l3gd20.L3DS20_RATE_400HZ, 400Hz data rate
# adafruit_l3gd20.L3DS20_RATE_800HZ, 800Hz data rate

# Hardware SPI setup:
# import digitalio
# CS = digitalio.DigitalInOut(board.D5)
# SPIB = board.SPI()
# SENSOR = adafruit_l3gd20.L3GD20_SPI(SPIB, CS)
# SENSOR = adafruit_l3gd20.L3GD20_I2C(
#    SPIB,
#    CS,
#    rng=adafruit_l3gd20.L3DS20_RANGE_500DPS,
#    rate=adafruit_l3gd20.L3DS20_RATE_200HZ,
# )

while True:
    #print("Angular Velocity (rad/s): {}".format(SENSOR.gyro[2]))
    print(SENSOR.gyro[0], SENSOR.gyro[1], SENSOR.gyro[2])
    #print()
    time.sleep(0.1)