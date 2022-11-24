def test_svi(test_app):
    response = test_app.get("/svi")
    assert response.status_code == 200
    assert response.json()['STATE'] == False

