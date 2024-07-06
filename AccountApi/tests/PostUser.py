import pytest
import responses
import requests
from AccountApi.constants.constants import *
from Verify.HttpStatusCode import HttpStatus
from Verify.verify import *
from Verify.logger import Log


@pytest.fixture(scope="module")
def api_client():
    return requests.Session()


@responses.activate
def test_post_user_when_password_does_not_valid(api_client):
    mock_url = f'{url}/User'
    responses.add(responses.POST, mock_url, status=400, json={
        "code": 1300,
        "message": "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer."
    })

    payload = {
        'userName': 'playrightApiTesting',
        'password': 'selim',
    }

    response = api_client.post(mock_url, json=payload)

    Verify.assert_status_code(response, HttpStatus.BAD_REQUEST)
    Verify.assert_json_data(response, {
        "code": 1300,
        "message": "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer."
    })

    Log.test_pass()


@responses.activate
def test_post_user_when_user_not_found(api_client):
    mock_url = f'{url}/User'
    responses.add(responses.POST, mock_url, status=404, json={
        "code": 0,
        "message": "user-not-found"
    })

    payload = {
        'userName': 'playrightApiTesting',
        'password': 'Se.123!',
    }

    response = api_client.post(mock_url, json=payload)

    Verify.assert_status_code(response, HttpStatus.NOT_FOUND)
    Verify.assert_json_data(response, {
        "code": 0,
        "message": "user-not-found"
    })

    Log.test_pass()


@responses.activate
def test_post_user_when_user_not_acceptable(api_client):
    mock_url = f'{url}/User'
    responses.add(responses.POST, mock_url, status=406, json={
        "code": 1204,
        "message": "User exists!"
    })

    payload = {
        'userName': 'playrightApiTesting',
        'password': 'Se.123!',
    }

    response = api_client.post(mock_url, json=payload)

    Verify.assert_status_code(response, HttpStatus.CONFLICT)
    Verify.assert_json_data(response, {
        "code": 1204,
        "message": "User exists!"
    })

    Log.test_pass()


@responses.activate
def test_post_user_when_valid_user(api_client):
    mock_url = f'{url}/User'
    responses.add(responses.POST, mock_url, status=201, json={
        "username": "playrightApiTesting",
        "password": "Se.123!"
    })

    payload = {
        'userName': 'playrightApiTesting',
        'password': 'Se.123!',
    }

    response = api_client.post(mock_url, json=payload)

    Verify.assert_status_code(response, HttpStatus.CREATED)
    Verify.assert_json_data(response, {
        "username": "playrightApiTesting",
        "password": "Se.123!"
    })

    Log.test_pass()