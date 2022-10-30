import sys
import time
import board
import busio
from flask import Flask
from flask import json, request, render_template, redirect, url_for
from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
sys.path.append('./modules')
from DFRobot_ADS1115 import ADS1115
sys.path.append('./Sensors')
from EC      import EC
from Ph      import Ph
from TP      import Tp
from Wl      import Wl
from Wf      import Wf
sys.path.append('./Actuators')
from P1      import P1
from P2      import P2
from P3      import P3
from Mp      import Mp
from V1      import V1
from V2      import V2

ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16

ads1115 = ADS1115()
ec      = EC()
ph      = Ph()
tp      = Tp()
wl      = Wl()
wf      = Wf()
p1      = P1()
p2      = P2()
p3      = P3()
mp      = Mp()
v1      = V1()
v2      = V2()

PH_State     = False
PH_Reading   = 0.0
EC_State     = False
EC_Reading   = 0.0
TEMP_State   = False
TEMP_Reading = 0.0
WL_State     = False
WL_Reading   = 0.0
MPUMP_State   = False
ECUP_State   = False
PHUP_State   = False
PHDWN_State  = False


app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
i2c = busio.I2C(board.SCL, board.SDA)

# GPIO LAYOUT
# CHANNEL | | GPIO_NO | |  COMP  |
#---------|-|---------|-|--------|
#   01    | |   08    | |  Ph    |
#   02    | |   11    | |  EC    |
#   03    | |   07    | |  Tp    |
#   04    | |   19    | |  Wl    |
#   05    | |   12    | |  Wf    |
#   06    | |   20    | |  P1    |
#   07    | |   16    | |  P2    |
#   08    | |   21    | |  P3    |
#   09    | |   26    | |  Mp    |
#   10    | |   19    | |  V1    |
#   11    | |   06    | |  V2    |
#   12    | |   05    | |  F1    |

act_HIGH_List = [20, 26, 11, 19, 13 ,6, 21,5,7]
act_LOW_List = [5]
pinmap = {"EC": 11, "PH": 8, "Tp":7, "Wl":19, "ECUP":20, "PHUP":12, "PHDWN":16, "MPUMP":21} 


cpu = CPUTemperature()
print("PI CPU Temperature: ")
print(cpu.temperature)

for i in act_HIGH_List:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

for i in act_LOW_List:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)


@app.route('/PhOn', methods=['GET'])
def PhOn():
    try:
        return ph.on(pinmap['PH'])
    
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/PhOff', methods=['GET'])
def PhOff():
    try:
        return ph.off(pinmap['PH'])

    except Exception as e:
        return f'Error: {str(e)}'


@app.route('/PhRead', methods=['GET'])
def PhRead():
    try:
        PhOn()
        #temp.on(pinmap['Tp'])
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
        adc3 = ads1115.readVoltage(2)
        #adc2 = ads1115.readVoltage(2)
        tp = 25.0
        read = ph.read(adc3['r'],tp)
        data = {"PhRead": read,"PhState": False, "temperature": tp, "TpState": False}
        PhOff()
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        return response

    except Exception as e:
        return  f'Error: {str(e)}'


@app.route('/EcOn', methods=['GET'])
def EcOn():
    try:
        return ec.on(pinmap['EC'])
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/EcOff', methods=['GET'])
def EcOff():
    try:
        return ec.off(pinmap['EC'])

    except Exception as e:
        return f'Error: {str(e)}'


@app.route('/EcRead', methods=['GET'])
def EcRead():
    try:
        EcOn()
        #temp.on(pinmap['Tp'])
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
        adc0 = ads1115.readVoltage(1)
        #adc2 = ads1115.readVoltage(2)
        tp = 25.0
        read = ec.read(adc0['r'],tp)
        print(adc0['r'])
        print(read)
        data = {"EcRead": read,"EcState": False, "temperature": tp, "TpState": False}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/TpOn', methods=['GET'])
def TpOn():
    try:
        return tp.on(pinmap['Tp'])
    except Exception as e:
        return  f'Error: {str(e)}'

@app.route('/TpOff', methods=['GET'])
def TpOff():
    try:
        return tp.off(pinmap['Tp'])
    
    except Exception as e:
        return  f'Error: {str(e)}'

@app.route('/TpRead', methods=['GET'])
def TpRead():
    try:
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
        adc0 = ads1115.readVoltage(1)
        read = tp.read(adc0['r'])
        print(adc0['r'])
        data = {"TpRead": read,"TpState": False}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        return response

    except Exception as e:
        return f'Error: {str(e)}'


@app.route('/WlOn', methods=['GET'])
def WlOn():
    try:
        return wl.on(pinmap['Wl'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/WlOff', methods=['GET'])
def WlOff():
    try:
        return wl.off(pinmap['Wl']) 

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/WlRead', methods=['GET'])
def WlRead():
    try:
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
        adc0 = ads1115.readVoltage(1)
        read = tp.read(adc0['r'])
        #read = float(AnalogIn(ads, ADS.P0).voltage)
        Wl_Reading = wl.read(read)
        data = {"Wl_Reading": Wl_Reading}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        return response

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/WfOn', methods=['GET'])
def WfOn():
    try:
        return wl.on(pinmap['Wl'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/WfOff', methods=['GET'])
def WfOff():
    try:
        return wl.off(pinmap['Wl']) 

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/WfRead', methods=['GET'])
def WfRead():
    try:
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
        adc0 = ads1115.readVoltage(1)
        read = wf.read(adc0['r'])
        #read = float(AnalogIn(ads, ADS.P0).voltage)
        Wf_Reading = wl.read(read)
        data = {"Wf_Reading": Wf_Reading}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        return response

    except Exception as e:
        return f'Error: {str(e)}'


@app.route('/EcUpOn', methods=['GET'])
def EcUpOn():
    try:
        #data = {"ECUP_State": ECUP_State}
        #response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        return p1.on(pinmap['ECUP'])

    except Exception as e:
        return 'Error: {str(e)}'

@app.route('/EcUpOff', methods=['GET'])
def EcUpOff():
    try:
        return p1.off(pinmap['ECUP'])
    
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/ECUPtest', methods=['GET'])
def EcUpTest():
    try:
        GPIO.output(pinmap['ECUP'], GPIO.HIGH)
        global ECUP_State
        ECUP_State = True
        data = {"ECUP_State": ECUP_State}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        print(response)
        time.sleep(3)
        GPIO.output(pinmap['ECUP'],GPIO.LOW)
        return response

    except Exception as e:
        str = f'Error: {str(e)}'
    return str

@app.route('/PhUpOn', methods=['GET'])
def PhUpOn():
    try:
        return p2.on(pinmap['PHUP']) 

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/PhUpOff', methods=['GET'])
def PhUpOff():
    try:
        return p2.off(pinmap['PHUP'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/PhUptest', methods=['GET'])
def PhUpTest():
    try:
        GPIO.output(pinmap['PHUP'], GPIO.HIGH)
        global PHUP_State
        PHUP_State = True
        data = {"PHUP_State": PHUP_State}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        print(response)
        time.sleep(25)
        GPIO.output(pinmap['PHUP'], GPIO.LOW)
        return response

    except Exception as e:
        str = f'Error: {str(e)}'
    return str


@app.route('/PhDwnOn', methods=['GET'])
def PhDwnOn():
    try:
        return p3.on(pinmap['PHDWN'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/PhDwnOff', methods=['GET'])
def PhDwnOff():
    try:
        return p3.off(pinmap['PHDWN'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/PhDwnTest', methods=['GET'])
def PhDwnTest():
    try:
        GPIO.output(pinmap['PHDWN'], GPIO.HIGH)
        global PHDWN_State
        PHDWN_State = True
        data = {"PHDWN_State": PHDWN_State}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        print(response)
        time.sleep(10)
        GPIO.output(pinmap['PHDWN'], GPIO.LOW)
        return response

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/MpOn', methods=['GET'])
def MpOn():
    try:
        return mp.on(pinmap['Mp'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/MpOff', methods=['GET'])
def MpOff():
    try:
        return mp.off(pinmap['Mp'])

    except Exception as e:
        return f'Error: {str(e)}'


@app.route('/MpTest', methods=['GET'])
def MPUMPtest():
    try:
        GPIO.output(pinmap['Mp'], GPIO.HIGH)
        global MPUMP_State
        MPUMP_State = True
        data = {"MPUMP_State": MPUMP_State}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        print(response)
        time.sleep(300)
        GPIO.output(pinmap['MPUMP'], GPIO.LOW)
        return response

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/ValInOn', methods=['GET'])
def ValInOn():
    try:
        return v1.on(pinmap['ValIn'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/ValInOff', methods=['GET'])
def ValInOff():
    try:
        return v1.off(pinmap['ValIn'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/ValOutOn', methods=['GET'])
def ValOutOn():
    try:
        return v2.on(pinmap['ValOut'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/ValOutOff', methods=['GET'])
def ValOutOff():
    try:
        return v2.off(pinmap['ValOut'])

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/Tick', methods=['GET'])
def Tick():
    try:
        global PH_Reading
        #PH_Reading = float( AnalogIn(ads, ADS.P0).voltage)
        data = {"PH_State":PH_State,"PH_Reading":PH_Reading,"EC_State":EC_State,"EC_Reading":EC_Reading,"TEMP_State":TEMP_State,"TEMP_Reading":TEMP_Reading,"WL_State":WL_State,"WL_Reading":WL_Reading,"MPUMP_State":MPUMP_State,"ECUP_State":ECUP_State,"PHUP_State":PHUP_State,"PHDWN_State":PHDWN_State}
        response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
        print(data)
        print(response)
        return response

    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
