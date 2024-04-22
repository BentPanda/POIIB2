from unittest.mock import Mock

import pytest
from flask.views import MethodView

from src.controllers import CreateUserController
from src.views import CreateUserView


@pytest.fixture
def create_user_view():
    controller = Mock(CreateUserController)
    return CreateUserView(
        controller=controller,
    )


def test_is_method_view_subclass(create_user_view):
    assert isinstance(create_user_view, MethodView)


def test_raises_on_post_method(create_user_view):
    with pytest.raises(NotImplementedError):
        create_user_view.post()
