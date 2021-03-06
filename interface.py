#!/usr/bin/python
import mraa
import pyupm_i2clcd as lcd
import time
import random

from Servo import *

def authenticate():
    print("TODO: Entering authenticate() stub")

    myLCD.clear()
    myLCD.setColor(255, 255, 0)
    myLCD.setCursor(0, 0)
    myLCD.write("Authenticating")

    time.sleep(2)

    return bool(random.getrandbits(1))

def granted():
    print("TODO: Entering granted() stub")
    
    myLCD.clear()
    myLCD.setColor(0, 255, 0)
    myLCD.setCursor(0, 0)
    myLCD.write("Welcome home,")
    myLCD.setCursor(1, 0)
    name = random.choice(["Stefan", "Demetra", "Gabrielle"])
    myLCD.write(name)

    servo.write(170)
    time.sleep(5)
    servo.write(0)

def denied():
    print("TODO: Entering denied() stub")
    
    myLCD.clear()
    myLCD.setColor(255, 0, 0)
    myLCD.setCursor(0, 0)
    myLCD.write("Unauthorized")
    myLCD.setCursor(1, 0)
    myLCD.write("Calling 911")

    time.sleep(5)

def greeting():
    myLCD.clear()
    myLCD.setColor(255, 255, 255)
    myLCD.setCursor(0, 0)
    myLCD.write("FaceLock")
    myLCD.setCursor(1, 0)
    myLCD.write("Press button")

    servo.write(0)

BUTTON_PIN = 2
button = mraa.Gpio(BUTTON_PIN)
button.dir(mraa.DIR_IN)

## The LCD can only display 16 characters per line
myLCD = lcd.Jhd1313m1(0, 0x3E, 0x62)

servo = Servo("Lock")
servo.attach(3)

greeting()

while True:

    if button.read():
        
        permissionGranted = authenticate()

        if permissionGranted:
            granted()
        else:
            denied()
        
        greeting()


    time.sleep(0.1)
