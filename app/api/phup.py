from fastapi import APIRouter
from .actuators.pumpphup import PHU
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
phua = PHU()
ads1115 = ADS1115()


@router.get("/phu")
async def phu():
    try:
        phua.on(20)
        #status = "True"
        time.sleep(3)
        phua.off(20)
        status = False
        return {"STATE": status}
    except Exception as e:
        return {"ERROR":str(e)}
