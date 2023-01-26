
from pytest_voluptuous import S  # плагин для читаемого ассерта
from voluptuous import Schema, PREVENT_EXTRA, Required, Optional
import requests
from requests import Response

from utils.base_session import regres_session


def test_create_user_schema():

    create_user_schema = Schema(
        {
            "name": str,
            "job": str,
            "id": str,
            "createdAt": str
        },
    )

    result: Response = regres_session().post(url='api/users')

    assert result.json() == S(create_user_schema)

