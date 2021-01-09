import pytest
from api_utils.api import APIClient


def pytest_addoption(parser):
    """Parser parameters for testing"""
    parser.addoption('--url',
                     action='store',
                     default='http://127.0.0.1:5000',
                     help='Target link for request')

@pytest.fixture()
def api_client(request):
    """Getting url for api tests"""
    base_url = request.config.getoption('--url')

    return APIClient(base_url)