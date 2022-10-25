import Component

class Ph(Component):
    # state:on/off   relayPin:'PH'   relayState:GPIO.LOW/GPIO.HIGH
    def info(self, sensorName:str, state:bool, relayPin:str, relayState:str ):
        sensorName:str
        state:bool
        relayPin:str
        relayState:str


    def on():
        GPIO.output(pinmap['PH'], GPIO.LOW)
        return {"Ph_State": PH_State}

    def off():
        GPIO.output(pinmap['PH'], GPIO.LOW)
        data = {"Ph_State": PH_State}
        return data

    def read():
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
        adc1 = ads1115.readVoltage(1)
        adc2 = ads1115.readVoltage(2)
        temperature = adc2['r']
        read = ph.readPH(adc1['r'], temperature)
        data = {"Ph_Reading": read, "Temp_State":temperature}
        return data

    def cal():
        return
