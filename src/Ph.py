import Component
import time
import sys

_temperature      = 25.0
_acidVoltage      = 3225#2032.44
_neutralVoltage   = 2722# 1500.0

class Ph():

    # state:on/off   relayPin:'PH'   relayState:GPIO.LOW/GPIO.HIGH
    def __init__(self, sensorName:str, command:str ):
        self.sensorName:str
        self.command:str

    def on():
        GPIO.output(pinmap['PH'], GPIO.LOW)
        return {"Ph_State": PH_State}

    def off():
        GPIO.output(pinmap['PH'], GPIO.LOW)
        data = {"Ph_State": PH_State}
        return data

    def readPH(self,voltage,temperature):
        global _acidVoltage
		    global _neutralVoltage
		    slope     = (7.0-4.0)/((_neutralVoltage-2722.0)/3.0 - (_acidVoltage-2722.0)/3.0)  #((_neutralVoltage-1500.0)/3.0 - (_acidVoltage-1500.0)/3.0)
		    intercept = 7.0 - slope*(_neutralVoltage-2722.0)/3.0 #7.0 - slope*(_neutralVoltage-1500.0)/3.0
		    phValue  = slope*(voltage-2722.0)/3.0+intercept #slope*(voltage-1500.0)/3.0+intercept
		    round(phValue,2)
		    return phValue

    def read(self,):

        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
        adc1 = ads1115.readVoltage(1)
        adc2 = ads1115.readVoltage(2)
        temperature = adc2['r']
        read = readPH(adc1['r'], temperature)
        return {"Ph_Reading": read, "Temp_State":temperature}

    def cal():
        return
