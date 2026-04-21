from flask_login import current_user

def test_login(client):
    with client:
        client.post('/login', data={'username': 'nika', 'password': 'nika1234'}, follow_redirects=True)
        assert current_user.is_authenticated == True