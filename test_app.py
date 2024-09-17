import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    rv = client.get('/')
    assert b"Welcome to my Flask App!" in rv.data

def test_about(client):
    """Test the about page."""
    rv = client.get('/about')
    assert b"This is a simple DevOps project to showcase CI/CD and Docker." in rv.data

# # test_app.py
# import pytest
# from app import app

# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         yield client

# def test_home(client):
#     response = client.get('/')
#     assert response.data == b"Hello, World!"
#     assert response.status_code == 200