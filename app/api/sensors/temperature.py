import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class TP():

    def __init__(self):
        try:
            print("Tp is initialized")

        except:
            print ("phdata.txt ERROR ! Please run DFRobot_PH_Reset")
            sys.exit(1)
        
    
    def on(self, pin):
        global Tp_State

        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            Tp_State = True
            return {"Tp_State": Tp_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global Tp_State

        try:
            GPIO.output(pin, GPIO.HIGH)
            Tp_State = False
            return {"Tp_State": Tp_State}
        
        except Exception as e:
            return f'Error: {str(e)}'
    
    def read(self, voltage):
        try:
            tp = voltage
            temp_c = float(tp) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return tp  
        except:
            return 'failed'
