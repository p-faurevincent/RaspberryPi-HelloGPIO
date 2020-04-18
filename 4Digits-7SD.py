#!/usr/bin/env python3
#-- coding: utf-8 --


import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte


A = 7
B = 11
C = 13
D = 15
E = 31
F = 33
G = 16
DOT = 18

D1 = 32
D2 = 36
D3 = 38
D4 = 40


GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(DOT, GPIO.OUT)

GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)
GPIO.setup(D4, GPIO.OUT)



def displayNumber(n):
  AState = True
  BState = True
  CState = True
  DState = True
  EState = True
  FState = True
  GState = True
  DOTState = False 

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
  GPIO.output(DOT, DOTState)


def displayDigit(d):
  if d == 0:
    #print("D1")
    GPIO.output(D2, True)
    GPIO.output(D3, True)
    GPIO.output(D4, True)
    GPIO.output(D1, False)

  if d == 1:
    #print("D2")
    GPIO.output(D1, True)
    GPIO.output(D3, True)
    GPIO.output(D4, True)
    GPIO.output(D2, False)

  if d == 2:
    #print("D3")
    GPIO.output(D1, True)
    GPIO.output(D2, True)
    GPIO.output(D4, True)
    GPIO.output(D3, False)

  if d == 3:
    #print("D4")
    GPIO.output(D1, True)
    GPIO.output(D2, True)
    GPIO.output(D3, True)
    GPIO.output(D4, False)

def displayDigitNumber(d,n):
  displayDigit(d)
  displayNumber(n)



number = 0
n0 = 0
n1 = 0
n2 = 0
n3 = 0

try:
  while True:

    n0 = number / 1000 % 10
    n1 = number / 100 % 10
    n2 = number / 10 % 10
    n3 = number% 10

    print ("number ", number, " n0 ", n0, " n1 ", n1, " n2 ", n2, " n3 ", n3)


#    print("i=", i)
    d = d % 4
#    print("n=", n)
    # displayDigitNumber(d,d)
    number = number + 1
    time.sleep(0.005)


finally:
    GPIO.cleanup()
    print ("bye")
