import requests
from requests import Response

from pprint import pprint

# def test_get():
#     result: Response = requests.get('https://reqres.in/api/users', params={'page': 2}, headers={'User-Agent': 'python-requests/2.28.2'})
#     assert result.status_code == 200
#
#     assert result.json()['page'] == 2
#
#     assert len(result.json()['data']) != 0
#     pprint(result.request.headers)
#     # pprint(result.json())


def test_create_users():

    name = 'morpheus'
    job = 'leader'

    result: Response = requests.post(

        url='https://reqres.in/api/users',
        json={
                "name": name,
                "job": job
        }
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job

    assert isinstance(result.json()['id'], str)