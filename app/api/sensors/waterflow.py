import RPi.GPIO as GPIO
import time
import sys
import logging 
from statistics import mean

logger = logging.getLogger(__name__)
GPIO.setmode(GPIO.BCM)
State = False

class WF():

    def __init__(self):
        try:
            print("WF is initialized")

        except:
            print ("wf ERROR")
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
    
    def read(self, pin):

        GPIO.setup(pin, GPIO.IN)
        timestart  = 0.0
        gpiolast   = 0
        pulses     = 0
        constant   = 1.45
        timezero = time.time()
        totalcount = 0
        array = [] 
        while int(time.time() - timezero) <= 10:
            ratecount = 0
            pulses = 0
            timestart = time.time()
            #logger.error(timestart)
            while (pulses <= 5):
                gpiocurrent = GPIO.input(25)
                if gpiocurrent != 0 and gpiocurrent != gpiolast:
                    pulses = pulses + 1
                    logger.error("pulses" + str(pulses))
                gpiolast = gpiocurrent
            ratecount += 1
            totalcount += 1
            logger.error(str("Total_count" + str(totalcount))) 
            litermin = round((ratecount * constant)/(time.time()-timestart),2) 
            logger.error(litermin)
            array.append(litermin)

        return round(mean(array),2)
                 
