import pytest
from app import app, db, User
from flask_bcrypt import Bcrypt


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def init_database(client):
    # Create the database and the user for testing within an app context
    with app.app_context():
        db.create_all()

        # Create a test user
        bcrypt = Bcrypt()
        hashedp = bcrypt.generate_password_hash('test').decode('utf-8')
        user = User(username='test', email='test@exa.com', password=hashedp)
        db.session.add(user)
        db.session.commit()

        yield client

        # Cleanup
        db.drop_all()


def login(client):
    """Helper function to log in a user"""
    client.post('/login', data={'email': 'test@exa.com', 'password': 'test'})


def test_home(init_database):
    """Test the home page loads successfully."""
    client = init_database
    login(client)  # Log in the user
    rv = client.get('/')
    assert rv.status_code == 200


def test_about(init_database):
    """Test the about page loads successfully."""
    client = init_database
    login(client)  # Log in the user
    rv = client.get('/about')
    assert rv.status_code == 200


def test_personal_info(init_database):
    """Test the personal info page loads successfully."""
    client = init_database
    login(client)  # Log in the user
    rv = client.get('/personal-info')
    assert rv.status_code == 200
