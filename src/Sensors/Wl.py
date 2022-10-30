import RPi.GPIO as GPIO
import time
import sys

Wl_State = False
class Wl():

    def __init__(self):
        try:
            print("Wl is initialized")

        except:
            print ("phdata.txt ERROR ! Please run DFRobot_PH_Reset")
            sys.exit(1)
        
    
    def on(self, pin):
        global Wl_State

        try:
            GPIO.output(pin, GPIO.LOW)
            Wl_State = True
            return {"Wl_State": Wl_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global Wl_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            Wl_State = False
            return {"Wl_State": Wl_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
    
    def read(self, voltage):
        try:
            wl = voltage
            #insert logic 
            return wl  
        except:
            return 'failed'
