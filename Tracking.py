"""
    Author: Ye Li
    
    Edited by: Jiazhou Li, Ernest Ho, Mariam Al-Azizi
 
    Date: November 27, 2013
 
    Description: This program allows the scribbler robot to follow an object
    that has the colour red, green or blue.
    
    The robot takes takes pictures of what is infront of it. The pictures
    are passed into image-processing algorithms to find a (red, green, or blue)
    object. The robot then tracks the object by moving forward, but at the same
    time adjusting itself so that the object it is tracking is in the view
    of the camera.
    
    The algorithm terminates when the object or an obstacle is directly infront
    of the robot.
    
"""

from myro import *
import getObjectColor

def track () :

    # set-up initial colour
    clrL=[340,60,175] #Low-end R,G,B values
    clrH=[5,150,250]  #High-end R,G,B values
    
    pixelCount = [0,0,0]
    
    colour = -1 #initial colour to track is not determined yet
    
    while 1 == 1:
        
	sensitivity = 35;  #used to determine at which point does the robot adjust its position relative to the object          
        
	if colour < 0:     #target colour is not yet determined
	    #Determines the color of the object it is going to be tracking
	    
	    for colour in xrange(3):
		p = takePicture()
		p = getObjectColor.compressImage(p,4)		    

		temp = copyPicture(p)
		pixelCount[colour],avg_x,avg_y=getObjectColor.getObjectColor(temp, clrL[colour], clrH[colour])
	    
	    #calculate the most dominant colour
	    maxx = 0
	    for index in xrange(3):
		if (pixelCount[index] > maxx):
		    maxx = pixelCount[index]
		    colour = index
		    
	    pxs=pixelCount[colour]
	    
	    
	    if colour == 0:
		print "car colour: red"
	    elif colour == 1:
		print "car colour: green"
	    elif colour == 2:
		print "car colour: blue"	    
	    
	else:
	    
	    p = takePicture()
	    p = getObjectColor.compressImage(p,4)
	    pxs,avg_x,avg_y=getObjectColor.getObjectColor(p, clrL[colour], clrH[colour])
	    #print pxs,avg_x,avg_y
	    
	    show(p)	    
	    
	#sees if the robot is going to hit something
	obstacleStatus = getObstacle()
	if obstacleStatus[1] > 1100:    #middle sensor is most important
	    stop()
	    return
        
	#Depending on the position of avg_x on the image, the robot will turn so that the avg_x is at the middle of the picture 
	if pxs < 5:        #Not enough pixels to conclude something to follow
	    stop()
	elif avg_x < (127-sensitivity)/4 and avg_x > (55)/4 :   #Turn slightly left because avg_x is still close to the center
	    motors(0.8,1)
        elif avg_x > (127+sensitivity)/4 and avg_x < (195)/4:   #Turn slightly right because avg_x is still close to the center
	    motors(1,0.8)
	elif avg_x < (55)/4:                                    #Turn faster left because avg_x is almost off the picture
	    motors(0.65,1)
	elif avg_x > (195)/4:                                   #Turn faster right because avg_x is almost off the picture
	    motors(1,0.65)	    
	else:                                                   #The avg_x is at the center of the image, continue going forward
	    motors(1,1)

	