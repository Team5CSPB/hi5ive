from api import create_app
import pytest
from api.app import bp
from flask import Blueprint


@pytest.fixture
def app():
    app = create_app()
    app.register_blueprint(bp) #register blueprints from app on test app because app.py is not run in this configuration
    return app

# testing get user 1, should be testuser as set up now
def test_get_user(client):
    response = client.get('/user/1')
    assert response.is_json, "Response is not JSON"
    assert response.status_code == 200
    assert response.json['username'] == 'john_doe', "Wrong username returned for dummy user 1"
    assert response.json['id'] == 1, 'dummy user 1 should be user id 1'

def test_get_user_none(client):
    response = client.get('/user/5483')
    assert response.is_json, "Response is not JSON"
    assert response.status_code == 404
    assert response.json['error'] == 'User not found'

def test_matches(client):
    response = client.get('/matches/1')
    assert response.is_json, "Response is not JSON"
    assert response.status_code == 200
    assert len(response.json) > 0
    print(response.json)

def test_create_match_duplicate(client):
    response = client.post('/create_match', data={'user1_id': 1, 'user2_id': 2})
    assert response.is_json, "Response is not JSON"
    assert response.status_code == 409
    assert response.json['error'] == 'Match already exists'

def test_create_match_invalid_user(client):
    response = client.post('/create_match', data={'user1_id': 1, 'user2_id': 5483})
    assert response.is_json, "Response is not JSON"
    assert response.status_code == 404
    assert response.json['error'] == 'User not found'

def test_create_match_self(client):
    response = client.post('/create_match', data={'user1_id': 1, 'user2_id': 1})
    assert response.is_json, "Response is not JSON"
    assert response.status_code == 409
    assert response.json['error'] == 'Can\'t match user to self'

def test_create_match(client):
    response = client.post('/create_match', data={'user1_id': 1, 'user2_id': 3})
    assert response.is_json, "Response is not JSON"
    assert response.status_code == 200
    assert response.json['user1_id'] == 1
    assert response.json['user2_id'] == 3

# not sure what else to include here
def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) > 0

# test a link we don't have
def test_get_unknown_route(client):
    response = client.get('/not_a_route')
    assert response.status_code == 404, 'unknown route should return 404'


#* login currently disabled, not fully implemented
# def test_login(client):
#     assert client.get('/login').status_code == 200
#     response = client.post('/login', data={'username': 'john_doe', 'password_hash': 'hashed_password_1'})
#     assert response.is_json
#     #assert response.json['email'] == 'john@example.com'
#     print(response.json)

def test_get_user_by_interests(client):
    response = client.get('/users/interest/reading')
    print(response.json)
    #assert response.is_json, "Response is not JSON"
    assert response.status_code == 200
    assert len(response.json) > 0


# another place holder route
def test_signup(client):
    response = client.get('/signup')
    assert response.status_code == 200
    assert response.is_json
    assert response.json['place'] == 'holder'

# one more place holder
def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 200
    assert response.is_json
    assert response.json['place'] == 'holder'