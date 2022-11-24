from fastapi import APIRouter
from .sensors.ph import PH
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
phs = PH()
ads1115 = ADS1115()


@router.get("/ph")
async def ph():
    try:
        phs.on(7)
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(0x02)
        adc0 = ads1115.readVoltage(1)
        temp = 25
        read = phs.read(adc0['r'], temp)
        time.sleep(3)
        phs.off(7)
        return {"PH": read}
    except Exception as e:
        return {"ERROR":str(e)}
