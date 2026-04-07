import pigpio

pi1 = pigpio.pi()

SERVO_PIN = 18

# FS90R Pulse Widths (µs):
# 1500 = Stop
# 700 to 1500 = Clockwise (lower is faster)
# 1500 to 2300 = Counter-Clockwise (higher is faster)

class FS90R:
    """A class to represent an FS90R servo"""
    def __init__(self, pi: pigpio.pi, servoPin: int):
        self.pi: pigpio.pi = pi
        self.servoPin: int = servoPin
        self.inverted = False

    def setInverted(self, inverted: bool):
        """Sets whether to invert commands to the motor"""
        self.inverted = inverted
    
    def run(self, speed: float):
        """Runs the servo at a speed. -1 is full speed reverse, 1 is full speed forward"""
        if self.inverted:
            speed = speed * -1
        if speed > 1:
            speed = 1
        if speed < -1:
            speed = -1
        speed = (800 * speed) + 700
        self.pi.set_servo_pulsewidth(self.servoPin, speed)
    
    def dealocate(self):
        """Stops running the servo and releases pigpio resources"""
        self.pi.set_servo_pulsewidth(self.servoPin, 0)
        self.pi.stop()