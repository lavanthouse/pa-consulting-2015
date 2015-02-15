# import libraries to give the code the information that it needs
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PINBuzzer = 16

#set up variables to store the pin numbers
LEDRed = 26
LEDYellow = 13
LEDGreen = 6

YellowOn=False
RedOn=False

# Set up the GPIO
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDYellow, GPIO.OUT)
GPIO.setup(LEDGreen, GPIO.OUT)
GPIO.setup(PINBuzzer, GPIO.OUT, initial=0)

# Initialise variables
led_choice = 0
count = 0
LEDChosen = 0


beeperEnabled = True
deviceEnabled = True

# Function to turn the buzzer on or off
def enableBeeper(enabled):
    global beeperEnabled
    beeperEnabled = enabled
    if beeperEnabled == False:
        GPIO.output(PINBuzzer,GPIO.LOW)
    elif RedOn == True:
        GPIO.output(PINBuzzer,GPIO.HIGH)

# Function to turn the device on or off      
def enableDevice(enabled):
    global deviceEnabled
    deviceEnabled = enabled
    if deviceEnabled == False:
        GPIO.output(LEDGreen,GPIO.LOW)
        GPIO.output(LEDRed,GPIO.LOW)
        GPIO.output(PINBuzzer,GPIO.LOW)
        GPIO.output(LEDYellow,GPIO.LOW)
        
# Function to give suitable outputs for a high smoke level
def highlevel():
    GPIO.output(LEDGreen,GPIO.LOW)
    GPIO.output(LEDYellow,GPIO.LOW)
    if deviceEnabled == True:
        global YellowOn
        global RedOn
        YellowOn=False
        if RedOn==False:
            if beeperEnabled == True:
                GPIO.output(PINBuzzer,GPIO.HIGH)
            GPIO.output(LEDRed,GPIO.HIGH)
            RedOn=True
        else:
            GPIO.output(PINBuzzer,GPIO.LOW)
            GPIO.output(LEDRed,GPIO.LOW)
            RedOn = False
       
# Function to give suitable outputs for a medium smoke level       
def midlevel():
    GPIO.output(LEDGreen,GPIO.LOW)
    GPIO.output(LEDRed,GPIO.LOW)
    GPIO.output(PINBuzzer,GPIO.LOW)
    global RedOn
    global YellowOn
    RedOn=False
    if deviceEnabled == True:
        if YellowOn == False:
            GPIO.output(LEDYellow,GPIO.HIGH)
            YellowOn=True
        else: 
            GPIO.output(LEDYellow,GPIO.LOW)
            YellowOn = False

# Function to give suitable outputs for a low smoke level 
def lowlevel(): 
    GPIO.output(LEDRed,GPIO.LOW)
    GPIO.output(LEDYellow,GPIO.LOW)
    GPIO.output(PINBuzzer,GPIO.LOW)
    global YellowOn
    YellowOn=False
    global RedOn
    RedOn=False
    if deviceEnabled == True:
        GPIO.output(LEDGreen,GPIO.HIGH)
    
# Run the high, medium and low level functions
highlevel()
midlevel()
lowlevel()

