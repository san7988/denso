
import RPi.GPIO as GPIO
from time import sleep

def control_motor(speed_code):
	
	CONST_SPEED = 25
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	
	pwm=GPIO.PWM(16, 100)
	
	pwm.start(0)

	GPIO.output(25, True)
	GPIO.output(12, False)
	pwm.ChangeDutyCycle(CONST_SPEED*speed_code)
	
	sleep(2)
	
	#GPIO.output(16, False)
	
	#pwm.ChangeDutyCycle(75)
	#GPIO.output(16, True)
	#sleep(3)
	#GPIO.output(16, False)
	pwm.stop()
	GPIO.cleanup()
