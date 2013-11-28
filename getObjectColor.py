"""
    Author: Ernest Ho
    
    Edited by: Jiazhou Li, Ye Li, Difie Zhang, Arash Mortazavi
 
    Date: November 27, 2013
 
    Description: This module holds image-processing algorithms used by other
    modules.
    
"""

from myro import *
import colorsys

def compressImage(picture,ratio):
    """
    Compresses the image file by a certain factor to make the processing
    of the image faster
    """
    
    pic = copyPicture(picture)
    picture = makePicture(getWidth(pic)/ratio,getHeight(pic)/ratio)
    for x in xrange(0,getWidth(pic),ratio):
        for y in xrange(0,getHeight(pic),ratio):
            pixel = getPixel(pic,x,y)
            setPixel(picture,x/ratio,y/ratio,getColor(pixel))
    return picture

def getObjectColor(picture,clrL,clrH):
    """
    Goes through the picture pixel by pixel, looking for pixels of the desired
    hue, saturation and value.
    
    returns:
              -average x-position and average y-position of the desired pixels.
              -the number of desired pixels found
    """
    
    avg_x=0
    avg_y=0
    pxs=0
    
    for y in range(getHeight(picture)):
        for x in range(getWidth(picture)):
            pixel = getPixel(picture,x,y)
            
            RGB = [0,0,0]
            for i in xrange(3):
                if getRGB(pixel)[i] != 0:
                    RGB[i] = getRGB(pixel)[i]/255.0
                else:
                    RGB[i] = 0.0
            HSV = colorsys.rgb_to_hsv(RGB[0],RGB[1],RGB[2])
            if (clrL > clrH): #RED
                if (HSV[0] >= clrL/360.0 or HSV[0] <= clrH/360.0) and HSV[1] >= 0.5 and HSV[2] >= 0.5:
                    #setColor(pixel,white)
                    avg_x=(avg_x+x)/2
                    avg_y=(avg_y+y)/2
                    pxs+=1
                else:
                    setColor(pixel,black)
            else:
                if (HSV[0] >= clrL/360.0 and HSV[0] <= clrH/360.0) and HSV[1] >= 0.5 and HSV[2] >= 0.5:
                    #setColor(pixel,white)
                    avg_x=(avg_x+x)/2
                    avg_y=(avg_y+y)/2
                    pxs+=1
                else:
                    setColor(pixel,black)
                    
    return pxs,avg_x,avg_y
