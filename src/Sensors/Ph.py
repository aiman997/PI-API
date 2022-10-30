import RPi.GPIO as GPIO
import time
import sys

acidVoltage    = 3225
neutralVoltage = 2722 
PH_State       = False
PH_Reading     = 0.0


class Ph():
    
    def __init__(self):
        try:
            print("PH is  initialized")
            #with open('phdata.txt','r') as f:
                #neutralVoltageLine = f.readline()              #2531
                #neutralVoltageLine = neutralVoltageLine.strip('neutralVoltage=')
                #_neutralVoltage    = float(neutralVoltageLine)
                #acidVoltageLine    = f.readline()           #3024
                #acidVoltageLine    = acidVoltageLine.strip('acidVoltage=')
                #_acidVoltage       = float(acidVoltageLine)
        
        except:
            print ("phdata.txt ERROR ! Please run DFRobot_PH_Reset")
            sys.exit(1)
    
    def on(self, pin):
        global Ph_State
        
        try:
            GPIO.output(pin, GPIO.LOW)
            PH_State = True
            return {"Ph_State": PH_State}

        except Exception as e:
            return f'Error: {str(e)}'

    def off(self, pin):
        global PH_State
        
        try:
            GPIO.output(pin, GPIO.HIGH)
            PH_State = False
            return {"Ph_State": PH_State}
        
        except Exception as e:
            return f'Error: {str(e)}'

    def read(self, voltage, temperature):
        
        slope     = (7.0-4.0)/((neutralVoltage-2722.0)/3.0 - (acidVoltage-2722.0)/3.0)
        intercept = 7.0 - slope*(neutralVoltage-2722.0)/3.0 
        phValue  = slope*(voltage-2722.0)/3.0+intercept 
        round(phValue,2)
        return phValue
    
    def cal(self,voltage):      #2532 ph7 solution
        if (voltage > 2500 and voltage < 2600):
            print(">>>Buffer Solution:7.0")
            f=open('phdata.txt','r+')
            flist=f.readlines()
            flist[0]='neutralVoltage='+ str(voltage) + '\n'
            f=open('phdata.txt','w+')
            f.writelines(flist) 
            f.close()
            print (">>>PH:7.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
            time.sleep(5.0)
        elif (voltage>3000 and voltage<3100):
            print (">>>Buffer Solution:4.0")
            f=open('phdata.txt','r+')
            flist=f.readlines()
            flist[1]='acidVoltage='+ str(voltage) + '\n'
            f=open('phdata.txt','w+')
            f.writelines(flist)
            f.close()
            print (">>>PH:4.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
            time.sleep(5.0)
        else:
            print (">>>Buffer Solution Error Try Again<<<")

        
    def reset(self):
        _acidVoltage    = 2032.44
        _neutralVoltage = 1500.0

        try:
            f=open('phdata.txt','r+')
            flist=f.readlines()
            flist[0]='neutralVoltage='+ str(_neutralVoltage) + '\n'
            flist[1]='acidVoltage='+ str(_acidVoltage) + '\n'
            f=open('phdata.txt','w+')
            f.writelines(flist)
            f.close()
            print (">>>Reset to default parameters<<<")
        
        except:
            f=open('phdata.txt','w')
            #flist=f.readlines()
            flist   ='neutralVoltage='+ str(_neutralVoltage) + '\n'
            flist  +='acidVoltage='+ str(_acidVoltage) + '\n'
            #f=open('data.txt','w+')
            f.writelines(flist)
            f.close()
            print (">>>Reset to default parameters<<<")


