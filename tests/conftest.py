import os
import pytest
from dotenv import load_dotenv
from utils.base_session import BaseSession


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def reqres():
    api_url = os.getenv('API_URL')
    return BaseSession(api_url)
