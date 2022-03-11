import play_hole as ph
import time

def play_c():
  ph.stop_wind()
  ph.close_hole1()
  time.sleep(0.1)
  ph.close_hole2()
  ph.close_hole3()
  time.sleep(0.1)
  ph.close_hole4()
  ph.close_hole5()
  time.sleep(0.1)
  ph.close_hole6()
  ph.blow_wind()
  print("play C")

def play_d():
  ph.stop_wind()
  ph.close_hole1()
  time.sleep(0.1)
  ph.close_hole2()
  ph.close_hole3()
  time.sleep(0.1)
  ph.close_hole4()
  ph.close_hole5()
  time.sleep(0.1)
  ph.open_hole6()
  ph.blow_wind()
  print("play d")


def play_e():
  ph.stop_wind()
  ph.close_hole1()
  time.sleep(0.1)
  ph.close_hole2()
  ph.close_hole3()
  time.sleep(0.1)
  ph.close_hole4()
  ph.open_hole5()
  time.sleep(0.1)
  ph.open_hole6()
  ph.blow_wind()
  print("play e")

def play_f():
  ph.stop_wind()
  ph.close_hole1()
  time.sleep(0.1)
  ph.close_hole2()
  ph.close_hole3()
  time.sleep(0.1)
  ph.open_hole4()
  ph.open_hole5()
  time.sleep(0.1)
  ph.open_hole6()
  ph.blow_wind()
  print("play f")


def play_g():
  ph.stop_wind()
  ph.close_hole1()
  time.sleep(0.1)
  ph.close_hole2()
  ph.open_hole3()
  time.sleep(0.1)
  ph.open_hole4()
  ph.open_hole5()
  time.sleep(0.1)
  ph.open_hole6()
  ph.blow_wind()
  print("play g")


def play_a():
  ph.stop_wind()
  ph.close_hole1()
  time.sleep(0.1)
  ph.open_hole2()
  ph.open_hole3()
  time.sleep(0.1)
  ph.open_hole4()
  ph.open_hole5()
  time.sleep(0.1)
  ph.open_hole6()
  ph.blow_wind()
  print("play a")


def play_b():
  ph.stop_wind()
  ph.open_hole1()
  time.sleep(0.1)
  ph.open_hole2()
  ph.open_hole3()
  time.sleep(0.1)
  ph.open_hole4()
  ph.open_hole5()
  time.sleep(0.1)
  ph.open_hole6()
  ph.blow_wind()
  print("play b")

def stop_tone():
  ph.stop_wind()
  print("stop")

def play(tone):
    if tone == "C":
        play_c()
    elif tone == "D" :
        play_d()
    elif tone == "E" :
        play_e()
    elif tone == "F" :
        play_f()
    elif tone == "G":
        play_g()
    elif tone == "A" :
        play_a()
    elif tone == "B" :
        play_b()
    elif tone == "stop" : stop_tone()