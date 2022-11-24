def test_fan(test_app):
    response = test_app.get("/fan")
    assert response.status_code == 200
    assert response.json()['PITP'] > 0
    assert type(response.json()) is dict
