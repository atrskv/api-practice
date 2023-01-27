from requests import Response
from pytest_voluptuous import S
from utils.base_session import regres_session

from schemas import schemas


def test_create_user():

    # GIVEN:
    name = 'aleksei'
    job = 'qa'

    # WHEN:
    result: Response = regres_session().post(

        url='/api/users',

        json={
            'name': name,
            'job': job
        }
    )

    # THEN:
    assert result.status_code == 201
    assert result.json() == S(schemas.create_user)

    assert result.json()['name'] == name
    assert result.json()['job'] == job


def test_update_user():

    # GIVEN:
    name = 'aleksei'
    job = 'qa'
    new_name = 'Aleksei'
    new_job = 'qa_automation'

    # TBD: MOVE TO FIXTURE?
    prepare_user: Response = regres_session().post(

        url='/api/users',

        json={
            'name': name,
            'job': job
        }
    )

    # WHEN:
    result: Response = regres_session().put(

        url='/api/users/2',

        json={
            'name': new_name,
            'job': new_job
        }
    )

    # THEN:
    assert result.status_code == 200
    assert result.json() == S(schemas.update_user)

    assert result.json()['job'] == new_job
    assert result.json()['name'] == new_name


def test_register_user():

    # GIVEN:
    email = 'eve.holt@reqres.in'
    password = 'qwerty'

    # WHEN:
    result: Response = regres_session().post(

        url='/api/register',

        json={
            'email': email,
            'password': password
        }
    )

    # THEN:
    assert result.status_code == 200
    assert result.json() == S(schemas.register_user)

    assert len(result.json()['token']) == 17


def test_login_user():

    # GIVEN:
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'

    # WHEN:
    result: Response = regres_session().post(

        url='/api/login',
        json={
            'email': email,
            'password': password
    }
)
    # THEN:
    assert result.status_code == 200
    assert result.json() == S(schemas.login_user)

    assert len(result.json()['token']) == 17


def test_unsuccessful_login_user():

    # GIVEN:
    email = 'peter@klaven'

    # WHEN:
    result: Response = regres_session().post(
        url='/api/login',
        json={
            'email': email
    }
)
    # THEN:
    assert result.json() == S(schemas.unsuccessful_login_user)
    assert result.json()['error'] == 'Missing password'
