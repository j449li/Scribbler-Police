from myro import *
import time
import getObjectColor

def track () :

    # set-up initial colour
    clrL=[340,60,175]
    clrH=[5,150,250]
    
    pixelCount = [0,0,0]
    
    colour = -1 #colour
    
    while 1 == 1:  # to be determined
	
	#forward(1)
        
	sensitivity = 35;            
        
        
	if colour < 0:     #target colour is not yet determined
	    
	    for colour in xrange(3):
		p = takePicture()
		p = getObjectColor.compressImage(p,4)		    

		temp = copyPicture(p)
		pixelCount[colour],avg_x,avg_y=getObjectColor.getObjectColor(temp, clrL[colour], clrH[colour])
	    
	    #calculate the most dominant colour
	    max = 0
	    for index in xrange(3):
		if (pixelCount[index] > max):
		    max = pixelCount[index]
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
	    
	#see if the robot is going to hit something
	obstacleStatus = getObstacle()
	if obstacleStatus[1] > 1100:    #middle sensor is most important
	    stop()
	    return
        
        if pxs < 5:
	    stop()
        elif avg_x < (127-sensitivity)/4 and avg_x > (55)/4 :
	    motors(0.8,1)
        elif avg_x > (127+sensitivity)/4 and avg_x < (195)/4:
	    motors(1,0.8)
	elif avg_x < (55)/4:
	    motors(0.65,1)
	elif avg_x > (195)/4:
	    motors(1,0.65)	    
	else:
	    motors(1,1)

	