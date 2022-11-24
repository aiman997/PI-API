def test_wf(test_app):
    response = test_app.get("/wf")
    assert response.status_code == 200
    assert response.json()['WF'] => 0
    assert type(response.json()) is dict
