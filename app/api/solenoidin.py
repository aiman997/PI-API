from fastapi import APIRouter
from .actuators.solenoidvalvein import SVI
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
svia = SVI()
ads1115 = ADS1115()


@router.get("/svi")
async def svi():
    try:
        svia.on(19)
        time.sleep(3)
        svia.off(19)
        status = False
        return {"STATE": status}
    except Exception as e:
        return {"ERROR":str(e)}
