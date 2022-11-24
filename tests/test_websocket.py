def test_websocket(test_app):
    with test_app.websocket_connect("/ws/ec") as websocket:
        websocket.send_text('5')
        data = websocket.receive_text()
        assert data == "Sensor #ec period: 5"
        data = websocket.receive_text()
        assert data == str({'WARNING': 'Please set period to an intger grater than 10 seconds.'})
        websocket.send_text('11')
        data = websocket.receive_text()
        assert data == "Sensor #ec period: 11"
        data = websocket.receive_text()
        assert data == str({'ec': 123})