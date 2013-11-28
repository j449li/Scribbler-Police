"""
    Author: Difie Zhang
    
    Edited by: Daniel Joseph, Mariam Al-Azizi, Arash Mortazavi
 
    Date: November 24, 2013
 
    Description: This program executes a pre-determined maneuver for the robot 
    once a speeding object has been detected.
    
"""

from myro import *

import time

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
