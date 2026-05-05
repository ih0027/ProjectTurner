from MotorUtils import *
import keyboard
import pigpio
import time

#Turn timing constants
TURN_LEFT_TIME = 0.65
TURN_RIGHT_TIME = TURN_LEFT_TIME

#Spool timing constants
RETRACT_SPOOL_TIME = 1.4
EXTEND_SPOOL_TIME = RETRACT_SPOOL_TIME

#Other timing constants
PAUSE_TIME = 1
END_PAUSE_TIME = 1

#Initialize hardware
pi = pigpio.pi()
spoolServoPin = 3
turnServoPin = 2
spoolServo = FS90R(pi, spoolServoPin, stopFrequency= 1435)
turnServo = FS90R(pi, turnServoPin, stopFrequency=1495)
spoolServo.setInverted(False)
turnServo.setInverted(True)

resolvingInput = False

def runServoForTimeAndPause(servo: FS90R, runPower: float, runTime: float):
    """Runs a servo for a specified time at a specified power and then pauses"""
    servo.runForTime(runPower, runTime)
    time.sleep(PAUSE_TIME)

def turnPageForward():
    global resolvingInput
    """Turns the page forward. Forward is defined as taking the right page and moving it to the left"""
    if resolvingInput:
        return
    resolvingInput = True
    runServoForTimeAndPause(turnServo, -1.0, TURN_LEFT_TIME)
    runServoForTimeAndPause(spoolServo, -1.0, RETRACT_SPOOL_TIME)
    runServoForTimeAndPause(turnServo, 1.0, TURN_RIGHT_TIME)
    runServoForTimeAndPause(spoolServo, 1.0, EXTEND_SPOOL_TIME)
    time.sleep(END_PAUSE_TIME)
    resolvingInput = False

def turnPageReverse():
    global resolvingInput
    """NOT CURRENTLY IMPLEMENTED:  Turns the page backward. Backward is defined as taking the left page and moving it to the right."""
    if resolvingInput:
        return
    resolvingInput = True
    runServoForTimeAndPause(spoolServo, -1.0, RETRACT_SPOOL_TIME)
    runServoForTimeAndPause(turnServo, -1.0, TURN_LEFT_TIME)
    runServoForTimeAndPause(spoolServo, 1.0, EXTEND_SPOOL_TIME)
    runServoForTimeAndPause(turnServo, 1.0, TURN_RIGHT_TIME)
    time.sleep(END_PAUSE_TIME)
    resolvingInput = False

keyboard.on_press_key("left", lambda e: turnPageForward())
keyboard.on_press_key("right", lambda e:turnPageReverse())
keyboard.wait()