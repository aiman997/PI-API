import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

P3_State = False

class PHD():

    def __init__(self):
        try:
            print("P3 is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global P3_State

        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            P3_State = True
            return {"P3_State": P3_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global P3_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            P3_State = False
            return {"P3_State": P3_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
