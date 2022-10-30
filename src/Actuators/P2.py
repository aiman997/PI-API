import RPi.GPIO as GPIO
import time
import sys

P2_State = False

class P2():

    def __init__(self):
        try:
            print("P2 is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global P2_State

        try:
            GPIO.output(pin, GPIO.LOW)
            P2_State = True
            return {"P2_State": P2_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global P2_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            P2_State = False
            return {"P2_State": P2_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
