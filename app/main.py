from fastapi import FastAPI
from app.api import ping, ec, ph, temperature, waterlevel, waterflow, solenoidin, solenoidout, mainpump, ecup, phup, phdwn, fan

app = FastAPI()
app.include_router(ping.router)
app.include_router(ec.router)
app.include_router(ph.router)
app.include_router(temperature.router)
app.include_router(waterlevel.router)
app.include_router(waterflow.router)
app.include_router(solenoidin.router)
app.include_router(solenoidout.router)
app.include_router(mainpump.router)
app.include_router(ecup.router)
app.include_router(phup.router)
app.include_router(phdwn.router)
app.include_router(fan.router)
