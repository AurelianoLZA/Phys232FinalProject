import play_hole as ph
def play_c():
  ph.close_hole1()
  ph.close_hole2()
  ph.close_hole3()
  ph.close_hole5()
  ph.close_hole6()

def play_c_sharp():
  ph.close_hole1()
  ph.close_hole2()
  ph.close_hole3()
  ph.close_hole5()
  ph.close_half_hole6()

def play_d():
  ph.close_hole1()
  ph.close_hole2()
  ph.close_hole3()
  ph.close_hole5()

def play_d_sharp():
  ph.close_hole1()
  ph.close_hole2()
  ph.close_hole3()
  ph.close_half_hole5()

def play_e():
  ph.close_hole1()
  ph.close_hole2()
  ph.close_hole3()
  ph.close_hole5()

def play_f():
  ph.close_hole1()
  ph.close_hole2()
  ph.close_hole3()

def play_f_sharp():
  ph.close_hole1()
  ph.close_hole2()
  ph.close_half_hole3()

def play_g():
  ph.close_hole1()
  ph.close_hole2()

def play_g_sharp():
  ph.close_hole1()
  ph.close_half_hole2()

def play_a():
  ph.close_hole1()

def play_b():
# blow the wind
  ph.cole()

def play_a_sharp():
  ph.close_half_hole1()

def stop_tone():
  #stop blow wind
  ph.open_hole1()
  ph.open_hole2()
  ph.open_hole3()
  ph.open_hole4()
  ph.open_hole5()
  ph.open_hole6()

def play_tone(tone):
  if tone.tone == "C": play_c()
  elif tone.tone == "C_sharp": play_c_sharp()
  elif tone.tone == "D" : play_d()
  elif tone.tone == "E" : play_e()
  elif tone.tone == "F" : play_f()
  elif tone.tone == "F_sharp" : play_f_sharp()
  elif tone.tone == "G": play_g()
  elif tone.tone == "G_sharp" : play_g_sharp()
  elif tone.tone == "A" : play_a()
  elif tone.tone == "A_sharp" : play_a_sharp()
  elif tone.tone == "B" : play_b()