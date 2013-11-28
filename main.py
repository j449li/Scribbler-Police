"""
    Author: Difie Zhang
    
    Edited by: Daniel Joseph, Mariam Al-Azizi, Arash Mortazavi
 
    Date: November 27, 2013
 
    Description: This is the main logic of the program.
    
    ->Stationary until a speeding object is detected
    ->Executes a backward-turn maneuver once a speeding object is detected
    ->Attempts to track the object
    
"""

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
    if speed > SPEED_LIMIT:
        print "Speeding car detected at: " + str(speed) + "cm per second."
    else:
        print "Car detected at: " + str(speed) + "cm per second."
    
    
sweep(direction)

Tracking.track()
    
    
