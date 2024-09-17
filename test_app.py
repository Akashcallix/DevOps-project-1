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
    assert rv.status_code == 200
    assert b"<title>Home</title>" in rv.data
    # Adjust the following based on the actual content
    assert b"<h1>" in rv.data  # Check for presence of an <h1> tag

def test_about(client):
    """Test the about page."""
    rv = client.get('/about')
    assert rv.status_code == 200
    assert b"<title>About</title>" in rv.data
    # Adjust the following based on the actual content
    assert b"<h1>" in rv.data  # Check for presence of an <h1> tag

def test_404(client):
    """Test a 404 error page."""
    rv = client.get('/non-existent-page')
    assert rv.status_code == 404
