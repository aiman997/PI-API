from fastapi import APIRouter
from .sensors.ec import EC
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
ecs = EC()
ads1115 = ADS1115()


@router.get("/ec")
async def ec():
    try:
        state = ecs.on(11)
        ads1115.setAddr_ADS1115(0x48)
        ads1115.setGain(0x02)
        adc0 = ads1115.readVoltage(0)
        temp = 25
        read = ecs.read(adc0['r'], temp)
        time.sleep(3)
        state = ecs.off(11)
        return {"STATE":state['STATE'], "EC": read}
    except Exception as e:
        return {"ERROR":str(e)}
