from fastapi import APIRouter
from .actuators.mainpump import MP
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
mps = MP()
ads1115 = ADS1115()


@router.get("/mp")
async def mp():
    try:
        mps.on(21)
        time.sleep(3)
        mps.off(21)
        status = 1
        logger.error({'STATE:',status})
        return {'STATE': status}
    except Exception as e:
        return {"ERROR":str(e)}
