# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
from board import SCL, SDA
import busio
# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
i2c = busio.I2C(SCL, SDA)
print('after I2C')
print(str(i2c))
# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9685 driver.
# pca = PCA9685(i2c, reference_clock_speed=25630710)
pca.frequency = 50
# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.
# This is an example for the Sub-micro servo: https://www.adafruit.com/product/2201
# servo7 = servo.Servo(pca.channels[7], min_pulse=580, max_pulse=2350)
# This is an example for the Micro Servo - High Powered, High Torque Metal Gear:
#   https://www.adafruit.com/product/2307
# servo7 = servo.Servo(pca.channels[7], min_pulse=500, max_pulse=2600)
# This is an example for the Standard servo - TowerPro SG-5010 - 5010:
#   https://www.adafruit.com/product/155
# servo7 = servo.Servo(pca.channels[7], min_pulse=400, max_pulse=2400)
# This is an example for the Analog Feedback Servo: https://www.adafruit.com/product/1404
# servo7 = servo.Servo(pca.channels[7], min_pulse=600, max_pulse=2500)
# This is an example for the Micro servo - TowerPro SG-92R: https://www.adafruit.com/product/169
# servo7 = servo.Servo(pca.channels[7], min_pulse=500, max_pulse=2400)

# The pulse range is 750 - 2250 by default. This range typically gives 135 degrees of
# range, but the default is to use 180 degrees. You can specify the expected range if you wish:
# servo7 = servo.Servo(pca.channels[7], actuation_range=135)
# Initialize the servos (in this case, 0 and 7 for now but will expand)
servo0 = servo.Servo(pca.channels[0], min_pulse=400, max_pulse=2400)
servo1 = servo.Servo(pca.channels[1], min_pulse=400, max_pulse=2400)
servo2 = servo.Servo(pca.channels[2], min_pulse=400, max_pulse=2400)
servo3 = servo.Servo(pca.channels[3], min_pulse=400, max_pulse=2400)
servo4 = servo.Servo(pca.channels[4], min_pulse=400, max_pulse=2400)
servo5 = servo.Servo(pca.channels[5], min_pulse=400, max_pulse=2400)
servo6 = servo.Servo(pca.channels[6], min_pulse=400, max_pulse=2400)

stuff = [servo0, servo1, servo2, servo3, servo4, servo5, servo6]

#Calibrate angle positions open/half closed/open: the first index will point to the servo,
#and the 2nd index the angle such that 0 = open, 1 = half closed, 2 = closed
#Initialize array with 6 servos all with same value, although it is to be manually calibrated.
anglez = [[90, 85, 70],[90, 100, 115],[90, 85, 70],[90, 100, 115],[90, 85, 67],[90, 100, 110],[0,45,90]]

def open_hole1():
    stuff[0].angle = anglez[0][0]

def close_half_hole1():
    stuff[0].angle = anglez[0][1]

def close_hole1():
    stuff[0].angle = anglez[0][2]

def close_hole1():
    stuff[0].angle = anglez[0][2]

def open_hole2():
    stuff[1].angle = anglez[1][0]

def close_half_hole2():
    stuff[1].angle = anglez[1][1]

def close_hole2():
    stuff[1].angle = anglez[1][2]

def open_hole3():
    stuff[2].angle = anglez[2][0]

def close_half_hole3():
    stuff[2].angle = anglez[2][1]

def close_hole3():
    stuff[2].angle = anglez[2][2]

def open_hole4():
    stuff[3].angle = anglez[3][0]

def close_half_hole4():
    stuff[3].angle = anglez[3][1]

def close_hole4():
    stuff[3].angle = anglez[3][2]

def open_hole5():
    stuff[4].angle = anglez[4][0]

def close_half_hole5():
    stuff[4].angle = anglez[4][1]

def close_hole5():
    stuff[4].angle = anglez[4][2]

def open_hole6():
    stuff[5].angle = anglez[5][0]

def close_half_hole6():
    stuff[5].angle = anglez[5][1]

def close_hole6():
    stuff[5].angle = anglez[5][2]