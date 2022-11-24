from fastapi import APIRouter
from .actuators.solenoidvalveout import SVO
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
svoa = SVO()
ads1115 = ADS1115()


@router.get("/svo")
async def svo():
    try:
        state = svoa.on(6)
        time.sleep(3)
        state = svoa.off(6)
        #logger.error(type(state))
        return state
    except Exception as e:
        return {"ERROR":str(e)}
