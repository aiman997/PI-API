import RPi.GPIO as GPIO
import time
import sys

Wf_State = False
class Wf():

    def __init__(self):
        try:
            print("Wf is initialized")

        except:
            print ("wfdata.txt ERROR ! Please run DFRobot_PH_Reset")
            sys.exit(1)
        
    
    def on(self, pin):
        global Wf_State

        try:
            GPIO.output(pin, GPIO.LOW)
            Wf_State = True
            return {"Wf_State": Wf_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global Wf_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            Wf_State = False
            return {"Wf_State": Wf_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
    
    def read(self, voltage):
        try:
            wf = voltage
            #insert logic 
            return wf  
        except:
            return 'failed'
