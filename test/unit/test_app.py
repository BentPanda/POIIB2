from src.app import app
from src.app import create_user


def test_create_user() -> None:
    payload = {
        "name": "Wojciech",
        "lastname": "Oczkowski",
    }
    with app.test_request_context(json=payload):
        actual = create_user()
    assert actual.status_code == 201
