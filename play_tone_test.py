#import bell_ring as ph
def play_c():
  # ph.close_hole1()
  # ph.close_hole2()
  # ph.close_hole3()
  # ph.close_hole5()
  # ph.close_hole6()
  print("play C")

def play_c_sharp():
  # ph.close_hole1()
  # ph.close_hole2()
  # ph.close_hole3()
  # ph.close_hole5()
  # ph.close_half_hole6()
  print("play C#")

def play_d():
  # ph.close_hole1()
  # ph.close_hole2()
  # ph.close_hole3()
  # ph.close_hole5()
  print("play d")

def play_d_sharp():
  # ph.close_hole1()
  # ph.close_hole2()
  # ph.close_hole3()
  # ph.close_half_hole5()
  print("play d#")

def play_e():
  # ph.close_hole1()
  # ph.close_hole2()
  # ph.close_hole3()
  # ph.close_hole5()
  print("play e#")

def play_f():
  # ph.close_hole1()
  # ph.close_hole2()
  # ph.close_hole3()
  print("play f")

def play_f_sharp():
  # ph.close_hole1()
  # ph.close_hole2()
  # ph.close_half_hole3()
  print("play f#")

def play_g():
  # ph.close_hole1()
  # ph.close_hole2()
  print("play g")

def play_g_sharp():
  # ph.close_hole1()
  # ph.close_half_hole2()
  print("play g#")

def play_a():
  # ph.close_hole1()
  print("play a")

def play_b():
# blow the wind
#   ph.cole()
  print("play b")

def play_a_sharp():
  # ph.close_half_hole1()
  print("play C")

def stop_tone():
  #stop blow wind
  # ph.open_hole1()
  # ph.open_hole2()
  # ph.open_hole3()
  # ph.open_hole4()
  # ph.open_hole5()
  # ph.open_hole6()
  print("stop the tone")

def play(tone):
  stop_tone()
  if tone == "C": play_c()
  elif tone == "C_sharp": play_c_sharp()
  elif tone == "D" : play_d()
  elif tone == "E" : play_e()
  elif tone== "F" : play_f()
  elif tone == "F_sharp" : play_f_sharp()
  elif tone == "G": play_g()
  elif tone == "G_sharp" : play_g_sharp()
  elif tone == "A" : play_a()
  elif tone == "A_sharp" : play_a_sharp()
  elif tone == "B" : play_b()
  elif tone == "stop" : stop_tone()