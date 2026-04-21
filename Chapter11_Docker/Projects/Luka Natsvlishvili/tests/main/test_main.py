def test_init_db(client):
    response = client.get('/')
    assert response.status_code == 200