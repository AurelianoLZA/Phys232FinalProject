import time
import csv

import play_tone_test
from Phys232FinalProject import play_tone


class midi232:
    def __init__(self, comm):
        self.time = comm[0]
        self.instrument = comm[1]
        self.tone = comm[2]

file = open("songcsv.csv")
csvreader = csv.reader(file)
input = []
for row in csvreader:
    input.append(midi232([row[0], row[1], row[2]]))

# input = [midi232(["1","pennywhistle", "C"]),
#          midi232(["3", "pennywhistle", "D"]),
#          midi232(["4", "pennywhistle","D_sharp"]),
#          midi232(["5", "pennywhistle","stop"]),
#          midi232(["5.3", "pennywhistle","E"]),
#          midi232(["6.3", "pennywhistle","F"]),
#          midi232(["7.3", "pennywhistle","F_sharp"]),
#          midi232(["8.3", "pennywhistle","G"]),
#          midi232(["9.3", "pennywhistle","stop"]),
#          midi232(["9.6", "pennywhistle","G_sharp"]),
#          midi232(["10.6", "pennywhistle","A"]),
#          midi232(["11.6", "pennywhistle","A_sharp"]),
#          midi232(["11.6", "pennywhistle","B"]),
#          midi232(["11.6", "pennywhistle","stop"])]



## filter out the objects that we are responsible for
temp = []
for obj in input :
    if obj.instrument.strip() == "pennywhistle":
        temp.append(obj)


init_time = time.monotonic()

while temp:

    if time.monotonic() - init_time >= float(temp[0].time):
        # play the tone || stop the tone
        play_tone.play(temp[0].tone)
        #print(temp[0].tone)
        temp.pop(0)


