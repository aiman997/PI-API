def test_ec(test_app):
    response = test_app.get("/ec")
    assert response.status_code == 200
    assert response.json()['EC'] > 0
    assert type(response.json()) is dict
