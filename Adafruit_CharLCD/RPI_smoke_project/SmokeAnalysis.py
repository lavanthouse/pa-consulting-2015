import time
import buzz
import random
import math
import botbook_mcp3002 as mcp
import RPi.GPIO as GPIO
SmokeSensor = 21
GPIO.setup(SmokeSensor,GPIO.IN)

SmokeLevel = 0

HIGH_MED_BOUNDARY = 35
MED_LOW_BOUNDARY = 18

global SmokeLMHLevel
SmokeLMHLevel = 1

global level
level = 100
multiplier = 1

def ReadSmokeLevel():
    return mcp.readAnalog()
    
def SmokeDetection():
    SmokeLevel = ReadSmokeLevel()
    print ("Current Smoke Level is %i"%SmokeLevel)
    if SmokeLevel < MED_LOW_BOUNDARY:
        print ("Low Level Smoke Detected")
        SmokeLMHLevel = 1
        buzz.lowlevel()
    elif SmokeLevel > HIGH_MED_BOUNDARY:
        print ("High Level Smoke Detected")
        SmokeLMHLevel = 3
        buzz.highlevel()
    else:
        print ("Medium Level Smoke Detected")
        SmokeLMHLevel = 2
        buzz.midlevel()
        
    return SmokeLMHLevel

        
        

    
