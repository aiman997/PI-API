def test_wl(test_app):
    response = test_app.get("/wl")
    assert response.status_code == 200
    assert response.json()['WL'] > 0
    assert type(response.json()) is dict
