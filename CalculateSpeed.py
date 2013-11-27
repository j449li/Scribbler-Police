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
                            
    detectedTime = endTime - startTime
    detectedSpeed = 4.4075*((detectedTime)**(-0.79))   #speed in cm/s
    
    #print "detected speed: " + str(detectedSpeed) #for testing

    #wait for the car to fully go past (like, disappear, then return)
    seesSomething = True
    while seesSomething:
        ir_sensor = getIR()
        if ir_sensor[0] == 1 and ir_sensor[1] == 1:
            seesSomething = False
    
    return detectedSpeed, direction  #speed in cm/s