import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Mp_State = False

class MP():

    def __init__(self):
        try:
            print("Mp is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global Mp_State

        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            Mp_State = True
            return {'STATE': Mp_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global Mp_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            Mp_State = False
            return {'STATE': Mp_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
