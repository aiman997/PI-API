import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

State = False

class WL():

    def __init__(self):
        try:
            print("Wl is initialized")

        except:
            print ("WL ERROR !")
            sys.exit(1)
        
    
    def on(self, pin):
        global State

        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            State = True
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
    
    def read(self, voltage):
        try:
            wl = str("%.1f"%(voltage/200.*100))+"%\n"
            return wl
        except:
            return 'failed'
