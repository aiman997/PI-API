import RPi.GPIO as GPIO
import time
import sys

P1_State = False

class P1():

    def __init__(self):
        try:
            print("P1 is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global P1_State

        try:
            GPIO.output(pin, GPIO.LOW)
            P1_State = True
            return {"P1_State": P1_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global P1_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            P1_State = False
            return {"P1_State": P1_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
