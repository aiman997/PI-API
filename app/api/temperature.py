from fastapi import APIRouter
from .sensors.temperature import TP
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
tps = TP()
ads1115 = ADS1115()


@router.get("/temperature")
async def temperature():
    try:
        tps.on(8)
        logger.error("temperature")
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(0x02)
        adc = ads1115.readVoltage(2)
        read = tps.read(adc['r'])
        tps.off(8)
        return {"TEMPERATURE": read}
    except Exception as e:
        return {"ERROR":str(e)}
