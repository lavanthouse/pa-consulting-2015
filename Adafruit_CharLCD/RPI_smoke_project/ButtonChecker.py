#!/usr/bin/python
# Import libraries that we need to give the code the information it needs
import math
import time
import SmokeAnalysis
import buzz

import Adafruit_CharLCD as LCD

currentSelection = 0
deviceEnabled = True

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# create some custom characters
lcd.create_char(1, [2, 3, 2, 2, 14, 30, 12, 0])
lcd.create_char(2, [0, 1, 3, 22, 28, 8, 0, 0])
lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

# Show button state.
lcd.clear()
lcd.message('Press buttons...')

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, '', (1,1,1)),
            (LCD.LEFT,   ''  , (1,0,0)),
            (LCD.UP,     ''    , (1,0,1)),
            (LCD.DOWN,   ''  , (1,1,0)),
            (LCD.RIGHT,  '' , (1,0,1)) )

# Function to display the exact smoke level as text on the LCD screen
def displayExactSmokeLevel():
        currentSelection = 1
        #import exact smoke level from detector
        smokeLevel=SmokeAnalysis.ReadSmokeLevel()
        #print smoke level
        lcd.message('Level is %3.0f'%smokeLevel) 
        return

# Function to turn the beeper on
def beeperon():
        currentSelection = 0
        #Is beeper on?
        #If no turn beeper on.
        #If yes do nothing.
        lcd.message('Beeper is on')
        global beeperEnabled
        beeperEnabled=True
        buzz.enableBeeper(beeperEnabled)
        return

# Function to turn the beeper off
def beeperoff():
        currentSelection = 0
        #Is beeper off?
        #If no turn beeper off.
        #If yes do nothing.
        lcd.message('Beeper is off')
        global beeperEnabled
        beeperEnabled=False
        buzz.enableBeeper(beeperEnabled)
        return

# Function to display whether the smoke level is 'low', 'medium' or 'high'
def displayLMHLevel():
        currentSelection = 2
        #Import exact smoke level.
        #Determine whether level is 'low', 'medium' or 'high'.
        #Print level (low/ medium/ high)
        if SmokeAnalysis.SmokeDetection() == 1:
                lcd.message('Level is low.')
        if SmokeAnalysis.SmokeDetection() == 2:
                lcd.message('Level is medium.')
        if SmokeAnalysis.SmokeDetection() == 3:
                lcd.message('Level is high.')
        return
                
                
# Function to turn the smoke detection on and off
def onoff():
        currentSelection = 0
        #Is programme 'off'?
        #If yes turn on.
        global deviceEnabled
        deviceEnabled = not deviceEnabled
        #If no print "Press again to turn off"
        #If button is pressed again turn off.
        buzz.enableDevice(deviceEnabled)
        if deviceEnabled == True:
                SmokeAnalysis.SmokeDetection()
                lcd.message('On')
        else:
                lcd.message('Off')
        return

print 'Press Ctrl-C to quit.'

# Function to check continuously whether and which button has been pressed
# If a button has been pressed, run the appropriate functions
def buttonCheck():
        if lcd.is_pressed(LCD.SELECT):
              lcd.clear()
              onoff()
              while lcd.is_pressed(LCD.SELECT):
                      print ("Wait for release")
        if lcd.is_pressed(LCD.RIGHT):
                lcd.clear()
                displayLMHLevel()
        if lcd.is_pressed(LCD.LEFT):
                lcd.clear()
                displayExactSmokeLevel()
        if lcd.is_pressed(LCD.UP):
                lcd.clear()
                beeperon()
        if lcd.is_pressed(LCD.DOWN):
                lcd.clear()
                beeperoff()
        return
