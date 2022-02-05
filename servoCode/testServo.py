from gpiozero import Servo
from time import sleep

servo = Servo(4)

try:
	while True:
		userIn = input("type in x to run, y to return")
		if userIn == "x":
    			servo.min()
		elif userIn == "y":
    			servo.max()
except KeyboardInterrupt:
	print("Program stopped")
