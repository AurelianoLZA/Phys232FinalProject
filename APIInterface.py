import time
import play_tone

class midi232:
    def __init__(self, comm):
        self.time = comm[0]
        self.instrument = comm[1]
        self.tone = comm[2]

input = []
with open("./songcsv.csv") as f:
    lines = f.readlines()
    for line in lines:
        command = list(line.split(","))
        input.append(midi232(command))

## filter out the objects that we are responsible for
temp = []
for obj in input :
    if obj.instrument.strip() == "pennywhistle":
        temp.append(obj)
init_time = time.monotonic()

while temp:
    if time.monotonic() - init_time >= float(temp[0].time):
        # play the tone || stop the tone
        play_tone.play(temp[0].tone.strip())
        #print(temp[0].tone)
        temp.pop(0)



