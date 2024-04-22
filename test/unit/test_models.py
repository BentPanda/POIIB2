import pytest
from pydantic import BaseModel
from src.models import User



@pytest.fixture
def payload() -> dict:
    return {
        "first_name": "Andrzej",
        "last_name": "Duda",
        "address": {
            "street": "Krakowskie Przedmieście",
            "city": "Warszawa",
        },
        "height": 165,
    }


def test_model_is_pydantic_model_subclass() -> None:
    user = User()
    assert isinstance(user, BaseModel)


def test_can_load_first_name_json_payload(payload: dict) -> None:
    user = User(**payload)
    assert user.first_name == "Andrzej"


def test_can_load_last_name_json_payload(payload: dict) -> None:
    user = User(**payload)
    assert user.last_name == "Duda"


def test_can_load_address_street_json_payload(payload: dict) -> None:
    user = User(**payload)
    assert user.address.street == "Krakowskie Przedmieście"


def test_can_load_address_city_json_payload(payload: dict) -> None:
    user = User(**payload)
    assert user.address.city == "Warszawa"


def test_can_load_address_height_json_payload(payload: dict) -> None:
    user = User(**payload)
    assert user.height == 165
