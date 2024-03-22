# Import the RPi.GPIO packages
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Choose your pin-numbering Scheme
# We can have:
# 1. GPIO.BOARD - Board numbering scheme. 
# 2. GPIO.BCM - Braodcom chip-specific pin numbers.

GPIO.setup(18, GPIO.OUT) # Set pin 18 as our output pin

# Then we can output Digital Signals
GPIO.output(18, GPIO.HIGH) 

# Or PWM signals (which you will learn more later on)
pwm = GPIO.PWM(18, 1000)
pwm.start(50)