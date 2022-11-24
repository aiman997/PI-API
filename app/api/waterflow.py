from fastapi import APIRouter
from .sensors.waterflow import WF
from .modules.DFRobot_ADS1115 import ADS1115
import logging
import time

logger = logging.getLogger(__name__)
router = APIRouter()
wfs = WF()
ads1115 = ADS1115()


@router.get("/wf")
async def waterflow():
    try:
        state = wfs.on(6)
        read = wfs.read(25)
        #read = 24
        #logger.error(read)
        #time.sleep(3)
        state = wfs.off(6)
        return {"STATE": state['STATE'], "WF": read}
    except Exception as e:
        return {"ERROR":str(e)}
