from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

State = False

cpu = CPUTemperature()

class FAN():

    def __init__(self):
        try:
            print("Fan is initialized")

        except:
            sys.exit(1)
    
    def on(self, pin):
        global State

        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            State = True
            return {'STATE': State}
        
        except Exception as e:
            return f'Error: {str(e)}'

        
    def off(self, pin):
        global State

        try:
            GPIO.output(pin, GPIO.HIGH)
            State = False
            return {'STATE': State}
        
        except Exception as e:
            return f'Error: {str(e)}'
    
    def check(self, pin):
        global State

        try:
            tp = cpu.temperature
            time.sleep(5)

            if tp < 50:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.HIGH)
                State = False
            else:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)
                State = True
               
            return {'STATE':State, 'PITP':tp}
        
        except Exception as e:
            return f'Error: {str(e)}'
