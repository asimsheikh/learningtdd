from app import app

def test_first():
    tester = app.test_client()
    rv = tester.get('/')

    assert rv.status_code == 200 
    assert rv.data == b'Hello, Asim'

    rv = tester.get('/people')
    assert rv.data == b'People!'

