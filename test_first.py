import pytest 

from app import app

@pytest.fixture
def client():
    yield app.test_client()

def test_first():
    tester = app.test_client()
    rv = tester.get('/')

    assert rv.status_code == 200 
    assert rv.data == b'Hello, Asim'

def test_second(client):
    rv = client.get('/')
    
    assert rv.status_code == 200 
    assert rv.data == b'Hello, Asim'

