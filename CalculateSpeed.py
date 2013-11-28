"""
    Author: Difie Zhang
    
    Edited by: Mariam Al-Azizi, Daniel Joseph, Ye Li, Arash Mortazavi
 
    Date: November 26, 2013
 
    Description: This program calculates the speed of an object using
    the two infared sensor at the back of the scribbler robot.
    
    The program measures the time the object took to get from one sensor
    to the other. Then through numerous testing, and statistical analysis
    a relationship between the measured time and approximate speed of the
    object was developed.
    
"""

from myro import *

#enters a testSpeed mode and returns after it detects something going past
def testSpeed() :
    startTime = 0
    endTime = 0
    direction = "STANDBY"; # stores the direction in which the car is heading. Can be STANDBY, LEFT or RIGHT

    while True:
        ir_sensor = getIR()
        if direction == "STANDBY":
            if ir_sensor[0] == 0:
                startTime = currentTime()
                direction = "RIGHT"
            elif ir_sensor[1] == 0:
                startTime = currentTime()
                direction = "LEFT"
        elif direction == "RIGHT":
            if ir_sensor[1] == 0:
                endTime = currentTime()
                break
        elif direction == "LEFT":
            if ir_sensor[0] == 0:
                endTime = currentTime()
                break  
                            
    detectedTime = endTime - startTime                 #time for the object to go from one sensor to the other
    detectedSpeed = 4.4075*((detectedTime)**(-0.79))   #speed in cm/s, constant values are obtained from experimentation and statistical anaylsis
    
    #print "detected speed: " + str(detectedSpeed) #for testing

    #wait for the car to fully go past (like, disappear, then return)
    seesSomething = True
    while seesSomething:
        ir_sensor = getIR()
        if ir_sensor[0] == 1 and ir_sensor[1] == 1:
            seesSomething = False
    
    return detectedSpeed, direction  #returns the speed and heading of the object