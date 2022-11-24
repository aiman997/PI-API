def test_phd(test_app):
    response = test_app.get("/phd")
    assert response.status_code == 200
    assert response.json() == {"STATE":False}
    assert type(response.json()) is dict

