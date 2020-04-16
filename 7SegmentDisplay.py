#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

A = 11 
B = 15 
C = 29
D = 31
E = 33
F = 35
G = 37

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)

def display(n):
  if n == 0:
    print("zero")
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, False)

  if n == 1:
    print("one")
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)

  if n == 2:
    print("two")
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, True)

  if n == 3:
    print("three")
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, True)

  if n == 4:
    print("four")
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, True)
    GPIO.output(G, True)

  if n == 5:
    print("five")
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, False)
    GPIO.output(F, True)
    GPIO.output(G, True)

  if n == 6:
    print("six")
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)

  if n == 7:
    print("seven")
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)

  if n == 8:
    print("eight")
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)

  if n == 9:
    print("nine")
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, False)
    GPIO.output(F, True)
    GPIO.output(G, True)

def smartDisplay(n):
  AState = True
  BState = True
  CState = True
  DState = True
  EState = True
  FState = True
  GState = True

  if n in [1, 4]:
    AState = False
  if n in [5, 6]:
    BState = False
  if n in [2]:
    CState = False
  if n in [1, 4, 7]:
    DState = False
  if n in [1, 3, 4, 5, 7, 9]:
    EState = False
  if n in [1, 2, 3, 7]:
    FState = False
  if n in [0, 1, 7]:
    GState = False

  GPIO.output(A, AState)
  GPIO.output(B, BState)
  GPIO.output(C, CState)
  GPIO.output(D, DState)
  GPIO.output(E, EState)
  GPIO.output(F, FState)
  GPIO.output(G, GState)



try:
  while True:
    i = 0
    while i <= 9:
      print(i)
      smartDisplay(i)
      i += 1
      time.sleep(1)

    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)




finally:
    GPIO.cleanup()
    print ("bye")
