import RPi.GPIO as GPIO
import time
import sys

Mp_State = False

class Mp():

    def __init__(self):
        try:
            print("Mp is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global Mp_State

        try:
            GPIO.output(pin, GPIO.LOW)
            Mp_State = True
            return {"Mp_State": Mp_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global Mp_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            Mp_State = False
            return {"Mp_State": Mp_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
