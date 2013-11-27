from myro import *
initialize("COM3")

import CalculateSpeed
import Tracking

speed = 0
direction = ""

SPEED_LIMIT = 8

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

while speed < SPEED_LIMIT:
    speed,direction=CalculateSpeed.testSpeed()
    print speed
    
    
sweep(direction)

Tracking.track()
    
    
