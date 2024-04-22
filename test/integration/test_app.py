from src.app import app


def test_create_user_endpoint() -> None:
    client = app.test_client()
    actual = client.post("/users")
    assert actual.status_code == 201
