from myro import *

import time

#initialize("COM3")

def sweep(direction):
    INNER_MOTOR = 0.57   #constants, test-proven at Nov.24th
    TIME = 3.7
    
    if direction == "RIGHT":
        motors(-1,-1*INNER_MOTOR)
        time.sleep(TIME)
        stop()
    elif direction == "LEFT":
        motors(-1*INNER_MOTOR,-1)
        time.sleep(TIME)
        stop()        
