from myro import *
import time
import getObjectColor

def track () :

    # set-up initial colour
    clrL=[]
    clrH=[]
    clrL[0] = 340     #pre-set constants: RED
    clrH[0] = 5
    clrL[1] = 270     #pre-set constants: PURPLE
    clrH[1] = 315    
    clrL[2] = 175     #pre-set constants: BLUE
    clrH[2] = 260    
    
    colour = -1 #colour
    
    while 1 == 1:  # to be determined
	
	#forward(1)
        
	sensitivity = 35;            
        
        
	if c < 0:
	    
	    pxs = 0
	    
	    while pxs < 100:
		
		for colour in xrange(2):
		    
		    p = takePicture()
		    p = getObjectColor.compressImage(p,4)
		    pxs,avg_x,avg_y=getObjectColor.getObjectColor(p, clrL[colour], clrH[colour])
		    
		    if pxs > 100:
			break
		    show(p)
	else:
	    
	    p = takePicture()
	    p = getObjectColor.compressImage(p,4)
	    pxs,avg_x,avg_y=getObjectColor.getObjectColor(p, clrL[colour], clrH[colour])
	    #print pxs,avg_x,avg_y
	    
	    show(p)	    
	    
	#see if the robot is going to hit something
	obstacleStatus = getObstacle()
	if obstacleStatus[1] > 1000:    #middle sensor is most important
	    stop()
	    return
        
        if pxs < 5:
	    stop()
        elif avg_x < (127-sensitivity)/4:
	    motors(0.6,1)
	    time.sleep(0.005)
        elif avg_x > (127+sensitivity)/4:
	    motors(1,0.6)
	    time.sleep(0.005)
	else:
	    motors(1,1)
	    time.sleep(0.005)
	