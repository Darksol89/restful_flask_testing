import pytest


def test_get_users_list(api_client):
    """Return users list in system"""
    response = api_client.get_method(method='/api/accounts')
    response_json = response.json()

    assert response.status_code == 200
    for item in response_json:
        assert item['id'] != 0