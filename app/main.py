import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.api import ping
from .connectionmanger import ConnectionManager
from fastapi.responses import HTMLResponse

app = FastAPI()

app.include_router(ping.router)

html = """
<!DOCTYPE html>
<html>
	<head>
		<title>Charts</title>
	</head>
	<body>
		<h1>WebSocket Charts</h1>
		<script>
		// js goes here	
		</script>
	</body>
</html>
"""

manager = ConnectionManager()

@app.get("/")
async def get():
	return HTMLResponse(html)

@app.websocket("/ws/{sensor}")
async def websocket_endpoint(websocket: WebSocket, sensor: str):
	if any(sensor == sen for sen in ['ec', 'ph', 'tp', 'wf', 'wl', 'all']):
		await manager.connect(websocket)
		try:
			while True:
				period = await websocket.receive_text()
				await manager.broadcast(f"Sensor #{sensor} period: {period}")
				if period.isnumeric() and int(period) > 10:
					message = {
						"all": str({'ec': 123, 'ph': 123, 'tp': 123, 'wl': 123, 'wf': 123}),
						"ec": str({'ec': 123}),
						"ph": str({'ph': 123}),
						"tp": str({'tp': 123}),
						"wl": str({'wl': 123}),
						"wf": str({'wf': 123})
					}
					await manager.send_message(message[sensor], websocket)
				else:
					await manager.send_message(str({"WARNING": "Please set period to an intger grater than 10 seconds."}), websocket)
		except WebSocketDisconnect:
			manager.disconnect(websocket)