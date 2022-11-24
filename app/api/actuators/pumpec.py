import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


State = False

class PEC():

    def beginn(self):
        try:
            print("PEC is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global State

        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            P1_State = True
            return {"STATE": State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global State

        try:
            GPIO.output(pin, GPIO.HIGH)
            State = False
            return {"STATE": State}
        
        except Exception as e:
            return f'Error: {str(e)}'
