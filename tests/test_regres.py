from requests import Response
from pytest_voluptuous import S
from schemas import schemas


def test_create_user(reqres):

    name = 'aleksei'
    job = 'qa'

    result: Response = reqres.post(

        url='/api/users',

        json={
            'name': name,
            'job': job
        }
    )

    assert result.status_code == 201
    assert result.json() == S(schemas.create_user)
    assert result.json()['name'] == name
    assert result.json()['job'] == job


def test_update_user(reqres):

    name = 'Sasha'
    job = 'qa'
    new_name = 'Aleksei'
    new_job = 'qa_automation'

    prepare_user: Response = reqres.post(

        url='/api/users',

        json={
            'name': name,
            'job': job
        }
    )

    result: Response = reqres.put(

        url='/api/users/2',

        json={
            'name': new_name,
            'job': new_job
        }
    )

    assert result.status_code == 200
    assert result.json() == S(schemas.update_user)
    assert result.json()['job'] == new_job
    assert result.json()['name'] == new_name


def test_register_user(reqres):

    email = 'eve.holt@reqres.in'
    password = 'qwerty'

    result: Response = reqres.post(

        url='/api/register',

        json={
            'email': email,
            'password': password
        }
    )

    assert result.status_code == 200
    assert result.json() == S(schemas.register_user)
    assert len(result.json()['token']) == 17


def test_login_user(reqres):

    email = 'eve.holt@reqres.in'
    password = 'cityslicka'

    result: Response = reqres.post(

        url='/api/login',

        json={
            'email': email,
            'password': password
        }
    )

    assert result.status_code == 200
    assert result.json() == S(schemas.login_user)
    assert len(result.json()['token']) == 17


def test_unsuccessful_login_user(reqres):

    email = 'peter@klaven'

    result: Response = reqres.post(

        url='/api/login',

        json={
            'email': email
        }
    )

    assert result.json() == S(schemas.unsuccessful_login_user)
    assert result.json()['error'] == 'Missing password'
