def test_pec(test_app):
    response = test_app.get("/pec")
    assert response.status_code == 200
    assert response.json() == {"STATE":False}
    assert type(response.json()) is dict

