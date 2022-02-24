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
        while (time.monotonic()- init_time < input_object.time):
            if input_object.tone == "C": play_c()
            elif input_object.tone == "C_sharp": play_c_sharp()
            elif input_object.tone == "D" : play_d()
            elif input_object.tone == "E" : play_e()
            elif input_object.tone == "F" : play_f()
            elif input_object.tone == "F_sharp" : play_f_sharp()
            elif input_object.tone == "G": play_g()
            elif input_object.tone == "G_sharp" : play_g_sharp()
            elif input_object.tone == "A" : play_a()
            elif input_object.tone == "A_sharp" : play_a_sharp()
            elif input_object.tone == "B" : play_b()


