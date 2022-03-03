



class midi232:
    def __init__(self, comm):
        self.time = comm[0]
        self.instrument = comm[1]
        self.tone = comm[2]


input = [midi232(["1","pennywhistle", "play_c"])]
## filter out the objects that we are responsible for
temp = []
for obj in input :
    if obj.instrument == "pennywhistle":
        temp.append(obj)

for item in temp:
    print(item.tone)