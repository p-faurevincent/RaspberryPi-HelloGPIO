#!/usr/bin/env python3
#-- coding: utf-8 --


import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

D1 = 32
D2 = 36
D3 = 38
D4 = 40

GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)
GPIO.setup(D4, GPIO.OUT)

def displayD(n):
  if n == 0:
    print("D1")
    GPIO.output(D2, False)
    GPIO.output(D3, False)
    GPIO.output(D4, False)
    GPIO.output(D1, True)

  if n == 1:
    print("D2")
    GPIO.output(D1, False)
    GPIO.output(D3, False)
    GPIO.output(D4, False)
    GPIO.output(D2, True)

  if n == 2:
    print("D3")
    GPIO.output(D1, False)
    GPIO.output(D2, False)
    GPIO.output(D4, False)
    GPIO.output(D3, True)

  if n == 3:
    print("D4")
    GPIO.output(D1, False)
    GPIO.output(D2, False)
    GPIO.output(D3, False)
    GPIO.output(D4, True)




try:
  while True:
    i = 0
    print("i=", i)
    n = i % 4
    print("n=", n)



finally:
    GPIO.cleanup()
    print ("bye")
