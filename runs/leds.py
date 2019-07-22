#!/usr/bin/env python
#coding: utf8
import sys
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

if ( sys.argv[1] == "aus"):
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
if ( sys.argv[1] == "1aus"):
    GPIO.output(24, GPIO.LOW)
if ( sys.argv[1] == "2aus"):
    GPIO.output(23, GPIO.LOW)
if ( sys.argv[1] == "3aus"):
    GPIO.output(4, GPIO.LOW)
if ( sys.argv[1] == "an"):
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(4, GPIO.HIGH)
if ( sys.argv[1] == "1an"):
    GPIO.output(24, GPIO.HIGH)
if ( sys.argv[1] == "2an"):
    GPIO.output(23, GPIO.HIGH)
if ( sys.argv[1] == "3an"):
    GPIO.output(4, GPIO.HIGH)


if ( sys.argv[1] == "startup"):
    n = 0
    while n < 5 :
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(2)
        n += 1
    time.sleep(1)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(24, GPIO.LOW)
    time.sleep(3)
    GPIO.output(23, GPIO.LOW)
    time.sleep(3)
    GPIO.output(4, GPIO.LOW)
  


