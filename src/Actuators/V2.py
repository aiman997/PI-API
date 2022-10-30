import RPi.GPIO as GPIO
import time
import sys

V2_State = False

class V2():

    def __init__(self):
        try:
            print("V2 is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global V2_State

        try:
            GPIO.output(pin, GPIO.LOW)
            V2_State = True
            return {"V2_State": V2_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global V2_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            V2_State = False
            return {"V2_State": V2_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
