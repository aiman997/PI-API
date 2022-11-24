def test_svo(test_app):
    response = test_app.get("/svo")
    assert response.status_code == 200
    assert response.json() == {"STATE":False}

