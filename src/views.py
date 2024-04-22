from flask import Response, request
from flask.views import MethodView

from src.controllers import CreateUserController, CreateUserRequest


class UserView(MethodView):
    def __init__(self, controller: CreateUserController) -> None:
        self._controller = controller

    def post(self) -> Response:
        body = request.json
        if "name" not in body:
            return Response(status=400)
        controller_req = CreateUserRequest(
            name=body["name"],
            lastname=body["lastname"],
        )
        try:
            self._controller.create(controller_req)
        except NotImplementedError:
            pass
        return Response(status=201)
