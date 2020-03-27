import unbounded

def test_import():
    assert unbounded

def test_config():
    assert not unbounded.create_app().testing
    assert unbounded.create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Riddled Road your fate awaits!' in response.data
