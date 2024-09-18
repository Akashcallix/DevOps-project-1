import pytest


@pytest.fixture
def client():
    from app import app  # Import your Flask app
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home page loads successfully."""
    rv = client.get('/')
    assert rv.status_code == 200


def test_about(client):
    """Test the about page loads successfully."""
    rv = client.get('/about')
    assert rv.status_code == 200


def test_personal_info(client):
    """Test the personal info page loads successfully."""
    rv = client.get('/personal-info')
    assert rv.status_code == 200
