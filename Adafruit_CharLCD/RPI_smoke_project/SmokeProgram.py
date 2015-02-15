import SmokeAnalysis
import ButtonChecker

#global variables
global beeperEnabled
beeperEnabled=True
global deviceEnabled
deviceEnabled=True

x=0

# Keep checking smoke level and button state
while True:
    if x > 200:
        SmokeLevel = SmokeAnalysis.SmokeDetection()
        x = 0
    x = x + 1
    ButtonChecker.buttonCheck()