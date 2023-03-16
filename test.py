
from app import app # Flask instance of the API
from pytest import ExitCode

HOME_PAGE="/"


def test_home_page():
    response = app.test_client().get(HOME_PAGE)

    assert response.status_code == 200
    #assert response.data.decode('utf-8') == 'Waye'
    assert "Waye" in response.text
    assert b"Waye" in response.data
    #Html = response.data.decode()
    #print(Html)
    #print(response.data)