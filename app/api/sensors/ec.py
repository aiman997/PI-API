import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

_kvalue                 = 1.0
_kvalueLow              = 1.0
_kvalueHigh             = 1.0
_cmdReceivedBufferIndex = 0
_voltage                = 0.0
_temperature            = 26.6

State = False


class EC():

    def begin(self):
        global _kvalueLow
        global _kvalueHigh
        try:
            print("EC is initialized")
        except:
            print("ecdata.txt ERROR ! Please run DFRobot_EC_Reset")
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
            return {"STATE": State}
                
        except Exception as e:
            return f'Error: {str(e)}'
            
    def read(self,voltage,temperature):
        global _kvalueLow
        global _kvalueHigh
        global _kvalue
        
        rawEC = voltage / 3.61276185#1000*voltage *0.000001  #1000*voltage/820.0/200.0
        valueTemp = rawEC * _kvalue
        
        if(valueTemp > 2.5):
            _kvalue = _kvalueLow
        elif(valueTemp < 2.0):
            _kvalue = _kvalueLow

        value = rawEC * _kvalue * 2.60869565
        value = value / (1.0+0.02*(temperature-25.0))
        return value

    def calibration(self,voltage,temperature):
         rawEC = 1000*voltage/820.0/200.0
         if (rawEC>0.9 and rawEC<1.9):
             compECsolution = 1.413*(1.0+0.0185*(temperature-25.0))
             KValueTemp = 820.0*200.0*compECsolution/1000.0/voltage
             round(KValueTemp,2)
             print (">>>Buffer Solution:1.413us/cm")
             f=open('ecdata.txt','r+')
             flist=f.readlines()
             flist[0]='kvalueLow='+ str(KValueTemp) + '\n'
             f=open('ecdata.txt','w+')
             f.writelines(flist)
             f.close()
             print (">>>EC:1.413us/cm Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
             time.sleep(5.0)

         elif (rawEC>9 and rawEC<16.8):
             compECsolution = 12.88*(1.0+0.0185*(temperature-25.0))
             KValueTemp = 820.0*200.0*compECsolution/1000.0/voltage
             print (">>>Buffer Solution:12.88ms/cm")
             f=open('ecdata.txt','r+')
             flist=f.readlines()
             flist[1]='kvalueHigh='+ str(KValueTemp) + '\n'
             f=open('ecdata.txt','w+')
             f.writelines(flist)
             f.close()
             print (">>>EC:12.88ms/cm Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
             time.sleep(5.0)
         else:
            print (">>>Buffer Solution Error Try Again<<<")
    
    def reset(self):
        _kvalueLow              = 1.0;
        _kvalueHigh             = 1.0;
        
        try:
            f=open('ecdata.txt','r+')
            flist=f.readlines()
            flist[0]='kvalueLow=' + str(_kvalueLow)  + '\n'
            flist[1]='kvalueHigh='+ str(_kvalueHigh) + '\n'
            f=open('ecdata.txt','w+')
            f.writelines(flist)
            f.close()
            print (">>>Reset to default parameters<<<")
        
        except:
            f=open('ecdata.txt','w')
            #flist=f.readlines()
            flist   ='kvalueLow=' + str(_kvalueLow)  + '\n'
            flist  +='kvalueHigh='+ str(_kvalueHigh) + '\n'
            #f=open('data.txt','w+')
            f.writelines(flist)
            f.close()
            print (">>>Reset to default parameters<<<")

