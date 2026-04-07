from MotorUtils import *
import keyboard
import pigpio

pi = pigpio.pi()
spoolServoPin = 18
turnServoPin = 20

spoolServo = FS90R(pi, spoolServoPin)
turnServo = FS90R(pi, turnServoPin)

spoolServo.setInverted(False)
turnServo.setInverted(True)
