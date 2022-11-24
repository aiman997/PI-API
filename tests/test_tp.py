def test_ph(test_app):
    response = test_app.get("/ph")
    assert response.status_code == 200
    assert response.json()['PH'] > 0
