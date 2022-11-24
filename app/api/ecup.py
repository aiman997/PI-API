from fastapi import APIRouter
from .actuators.pumpec import PEC
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
pecs = PEC()
ads1115 = ADS1115()


@router.get("/pec")
async def pec():
    try:
        pecs.on(26)
        time.sleep(3)
        pecs.off(26)
        status = False
        return {"STATE": status}
    except Exception as e:
        return {"ERROR":str(e)}
