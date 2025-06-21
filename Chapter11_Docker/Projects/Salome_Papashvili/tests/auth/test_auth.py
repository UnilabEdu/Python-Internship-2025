from flask_login import current_user

def test_login(client):
    with client:
        client.post("/login", data={"username": "Admin", "password": "password12345"})
        assert current_user.is_authenticated == True
