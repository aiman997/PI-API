from fastapi import APIRouter
from .sensors.waterlevel import WL
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
wls = WL()
ads1115 = ADS1115()


@router.get("/wl")
async def waterlevel():
    try:
        state = wls.on(5)
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(0x02)
        adc2 = ads1115.readVoltage(2)
        read = wls.read(adc2['r'])
        #logger.error("wf")
        time.sleep(3)
        state = wls.off(5)
        return {"STATE":state['STATE'], "WL": read}
    except Exception as e:
        return {"ERROR":str(e)}
