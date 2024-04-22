from src.controllers import CreateUserController
from src.db_flask import DBFlask
from src.repositories import UserRepository
from src.views import UserView

app = DBFlask(__name__)


app.add_url_rule(
    "/user",
    "create_user",
    view_func=UserView.as_view(
        "create_user",
        controller=CreateUserController(
            repository=UserRepository(app.db_session_factory)
        ),
    )
)

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
