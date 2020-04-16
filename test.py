#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

BUTTON = 18 #Définit le numéro du port GPIO qui alimente la led
LED = 31 

GPIO.setup(BUTTON, GPIO.IN) #Active le contrôle du GPIO
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.input(BUTTON)==0:
            print ("Open")
            time.sleep(0.5)
        else:
            print ("Close")
            ledState=GPIO.input(LED)
            ledState= not ledState
            GPIO.output(LED, ledState)
            time.sleep(0.5)


finally:
    GPIO.cleanup()
    print ("bye")
