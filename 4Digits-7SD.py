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
    GPIO.output(D2, True)
    GPIO.output(D3, True)
    GPIO.output(D4, True)
    GPIO.output(D1, False)

  if n == 1:
    print("D2")
    GPIO.output(D1, True)
    GPIO.output(D3, True)
    GPIO.output(D4, True)
    GPIO.output(D2, False)

  if n == 2:
    print("D3")
    GPIO.output(D1, True)
    GPIO.output(D2, True)
    GPIO.output(D4, True)
    GPIO.output(D3, False)

  if n == 3:
    print("D4")
    GPIO.output(D1, True)
    GPIO.output(D2, True)
    GPIO.output(D3, True)
    GPIO.output(D4, False)


i = 0


try:
  while True:
    print("i=", i)
    n = i % 4
    print("n=", n)
    displayD(n)
    i = i+1
    time.sleep(0.005)


finally:
    GPIO.cleanup()
    print ("bye")
