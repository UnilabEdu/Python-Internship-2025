def test_add_product_unauthorized(client):
    response = client.get("/add_tour", follow_redirects=True)
    assert response.request.path == "/"

def test_add_product(client):
    with client:
        client.post("/login", data={"username": "Admin", "password": "password12345"})
        response = client.get("/add_tour", follow_redirects=True)
        assert b"Add Tour" in response.data

def test_edit_tour_unauthorized(client):
    response = client.get("/edit_tour/1", follow_redirects=True)
    assert response.request.path == "/"

def test_delete_tour_unauthorized(client):
    response = client.get("/delete_tour/1", follow_redirects=True)
    assert response.request.path == "/"

def test_edit_tour_authorized(client):
    with client:
        client.post("/login", data={"username": "Admin", "password": "password12345"})
        response = client.get("/edit_tour/1", follow_redirects=True)
        assert b"Add Tour" in response.data

def test_delete_tour_authorized(client):
    with client:
        client.post("/login", data={"username": "Admin", "password": "password12345"})
        response = client.get("/delete_tour/1", follow_redirects=True)
        assert response.status_code == 200