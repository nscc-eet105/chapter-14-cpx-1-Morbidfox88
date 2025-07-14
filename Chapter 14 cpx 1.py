#Chad Collard
#Chapter 14 cpx 1
#7/14/2025

from adafruit_circuitplayground import cp

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0,),
}

notes = {"A4": 440, "B4": 494, "C5": 523, "D5": 587}


def fill_pixels(color):
    cp.pixels.fill(color)


while True:
    if cp.touch_A1:
        cp.start_tone(notes["A4"])
        fill_pixels(colors["red"])
    elif cp.touch_A2:
        cp.start_tone(notes["B4"])
        fill_pixels(colors["green"])
    elif cp.touch_A3:
        cp.start_tone(notes["C5"])
        fill_pixels(colors["blue"])
    elif cp.touch_A4:
        cp.start_tone(notes["D5"])
        fill_pixels(colors["white"])
    else:
        cp.stop_tone()
        cp.pixels.fill(colors["black"])
