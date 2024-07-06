import pytest
import responses
import requests
from UserApi.constants.constants import *
from Verify.HttpStatusCode import HttpStatus
from Verify.verify import *
from Verify.logger import Log


@pytest.fixture(scope="module")
def api_client():
    return requests.Session()


@responses.activate
def test_single_get_user_mock_data(api_client):
    mock_url = f'{url}/users/2'

    mocked_response = {
        "data": {
            "id": 2,
            "email": "selimerdinc@selimerdinc.com",
            "first_name": "Selim",
            "last_name": "Erdinç",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    responses.add(responses.GET, mock_url, json=mocked_response, status=200)
    response = api_client.get(mock_url)

    Verify.assert_status_code(response, HttpStatus.OK)

    Verify.assert_json_contains(response, ['data', 'support'])

    Verify.assert_json_data(response, {
        "data": {
            "id": 2,
            "email": "selimerdinc@selimerdinc.com",
            "first_name": "Selim",
            "last_name": "Erdinç",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    })

    Log.test_pass()


def test_single_get_user(api_client):
    response = api_client.get(f'{url}/users/2')

    Verify.assert_status_code(response, HttpStatus.OK)

    Verify.assert_json_contains(response, ['data', 'support'])

    Verify.assert_json_data(response, {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    })

    Log.test_pass()


def test_single_get_user_not_found(api_client):
    response = api_client.get(f'{url}/users/23')

    Verify.assert_status_code(response, HttpStatus.NOT_FOUND)

    Verify.assert_json_data(response, {})

    Log.test_pass()


@responses.activate
def test_single_get_user_mock_not_found(api_client):
    mock_url = f'{url}/users/23'

    mocked_response = {
        "data": {
            "detail": "user-not-found"
        }
    }
    responses.add(responses.GET, mock_url, json=mocked_response, status=404)
    response = api_client.get(mock_url)

    Verify.assert_status_code(response, HttpStatus.NOT_FOUND)

    Verify.assert_json_data(response, {
        "data": {
            "detail": "user-not-found"
        }
    })

    Log.test_pass()

def test_register_not_valid_user(api_client):

    payload = {
        'email': 'playrightApiTesting@selimerdinc.com',
        'password': 'selim',
    }

    response = api_client.post(f'{url}/register',json=payload)

    Verify.assert_status_code(response, HttpStatus.BAD_REQUEST)


    Verify.assert_json_data(response, {
    "error": "Note: Only defined users succeed registration"
})

    Log.test_pass()

@responses.activate
def test_register_mock_not_valid_user(api_client):
    mock_url = f'{url}/register'
    responses.add(responses.POST, mock_url, status=201, json={
        'detail': 'user-created-success',
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    })

    payload = {
        'email': 'playrightApiTesting@selimerdinc.com',
        'password': 'selim'
    }

    response = api_client.post(f'{url}/register',json=payload)

    Verify.assert_status_code(response, HttpStatus.CREATED)


    Verify.assert_json_data(response, {
        'detail': 'user-created-success',
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
})

    Log.test_pass()