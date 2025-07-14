from adafruit_circuitplayground import cp
import time# Write your code here :-)

BLACK = (0, 0, 0,)
REST = (.1)

while True:
    for i in range(10):
        cp.pixels[i] = (0, 100, 0)
        time.sleep(REST)
        cp.pixels[i] = (BLACK)


    for i in range(9, -1, -1):
        cp.pixels[i] = (255, 0, 0)
        time.sleep(REST)
        cp.pixels[i] = (BLACK)




