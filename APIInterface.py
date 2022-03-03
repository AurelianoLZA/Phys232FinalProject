import time
import csv

import play_tone
from play_tone import *
from queue import Queue
from adafruit_circuitplayground import cp
from time import sleep,monotonic

class midi232:
    def __init__(self, comm):
        self.time = comm[0]
        self.instrument = comm[1]
        self.tone = comm[2]



input = [midi232(["1","pennywhistle", "C"]),
         midi232(["2", "pennywhistle", "stop"]),
         midi232(["10", "abc", "whatever"]),
         midi232(["11", "pennywhistle","F"]),
         midi232(["11", "pennywhistle","stop"])]


## filter out the objects that we are responsible for
temp = []
for obj in input :
    if obj.instrument.strip() == "pennywhistle":
        temp.append(obj)


init_time = time.monotonic()

while not temp:

    if time.monotonic() - init_time >= temp[0].time:
        # play the tone || stop the tone
        play_tone.play(temp[0].tone)
        temp.pop(0)


