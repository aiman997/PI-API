from fastapi import APIRouter
from .actuators.pumpphdwn import PHD
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
phda= PHD()
ads1115 = ADS1115()


@router.get("/phd")
async def phd():
    try:
        phda.on(16)
        time.sleep(3)
        phda.off(16)
        status = False
        return {"STATE": status}
    except Exception as e:
        return {"ERROR":str(e)}
