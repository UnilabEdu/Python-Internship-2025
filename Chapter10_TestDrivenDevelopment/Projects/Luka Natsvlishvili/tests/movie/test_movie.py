def test_add_movie_unauthorized(client):
    response = client.get('/create_movie', follow_redirects=True)
    assert response.request.path == '/login'

def test_edit_movie_unauthorized(client):
    response = client.get('/edit_movie/1', follow_redirects=True)
    assert response.request.path == '/login'

def test_delete_movie_unauthorized(client):
    response = client.get('/delete_movie/20', follow_redirects=True)
    assert response.request.path == '/login'

def test_create_movie(client):
    with client:
        client.post("/login", data={"username": "luka", "password": "luka1234"}, follow_redirects=True)
        response = client.get('/create_movie', follow_redirects=True)
        assert "ფილმის სახელი" in response.data.decode("utf-8")
