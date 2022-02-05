from gpiozero import Button, LED
import time
button = Button(23)
green = LED(25)

ledState = True

while True:
	button.wait_for_press()
	ledState = False
	if ledState:
		green.on()
	else:
		green.off()
	button.wait_for_release()
