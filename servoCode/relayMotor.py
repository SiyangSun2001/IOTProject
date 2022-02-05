import RPi.GPIO as GPIO
import time
import keyboard
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.output(15, False)
GPIO.output(31, False)
GPIO.output(37, False)

#GO DOWN 14 SEC
#GO UP 17 SEC

com  =input("up or down?")
if com == "up":
    GPIO.output(15, True)
    time.sleep(21)
    GPIO.output(15, False)
if com == "down":
    GPIO.output(31, True)
    GPIO.output(37, True)
    GPIO.output(15, True)
    time.sleep(14)
    GPIO.output(15, False)
    GPIO.output(31, False)
    GPIO.output(37, False)
#while True:
 #   if keyboard.is_pressed("r"):
  #      print("pressed")
   #     GPIO.output(15, True)
    #    time.sleep(1)
     #   print("woken up")
   # else:
    #    GPIO.output(15, False)
