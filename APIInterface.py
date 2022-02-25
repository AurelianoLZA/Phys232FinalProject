import time
from play_tone import *
from queue import Queue
from adafruit_circuitplayground import cp
from time import sleep,monotonic

class Command:
    def __init__(self, comm):
        self.time = comm[0]
        self.instrument = comm[1]
        self.tone = comm[2]


#q = Queue(maxsize  = 100)

while True :
    input_object = Command(input() )# assuming that input is a list with 3 arguments,each is a string
    if input_object.instrument  == "pennywhistle":
        # Put the command into the queue for later use
        init_time = time.monotonic()
        play_tone.play_tone(tone)
        #sleep(input_object.time)
        #while (time.monotonic()- init_time > input_object.time):
        play_tone.stop_tone()


