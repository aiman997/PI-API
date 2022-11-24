from fastapi import APIRouter
from .actuators.fan import FAN
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
fana = FAN()
ads1115 = ADS1115()


@router.get("/fan")
async def fan():
    try:
        status= fana.check(13)
        return status
    except Exception as e:
        return {"ERROR":str(e)}
