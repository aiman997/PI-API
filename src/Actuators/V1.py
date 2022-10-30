import RPi.GPIO as GPIO
import time
import sys

V1_State = False

class V1():

    def __init__(self):
        try:
            print("V1 is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global V1_State

        try:
            GPIO.output(pin, GPIO.LOW)
            V1_State = True
            return {"V1_State": V1_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global V1_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            V1_State = False
            return {"V1_State": V1_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
