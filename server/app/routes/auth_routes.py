from flask_openapi3 import Tag
from pydantic import BaseModel

from app.schemas import ErrorSchema, LoginSchema, SignUpSchema, UserViewSchema
from app.dependencies import (
    get_login_user_use_case,
    get_register_user_use_case,
)
from domain.exceptions import (
    DuplicateUserError,
    InvalidCredentialsError,
    ValidationError,
)

auth_tag = Tag(name="Auth", description="Cadastro e login de usuários")


def register_auth_routes(app) -> None:
    @app.post(
        "/auth/signup",
        tags=[auth_tag],
        responses={"201": UserViewSchema, "400": ErrorSchema, "409": ErrorSchema},
    )
    def signup(body: SignUpSchema):
        use_case = get_register_user_use_case()
        try:
            user = use_case.execute(body.email, body.password)
            return UserViewSchema(id=user.id, email=user.email), 201
        except ValidationError as exc:
            return ErrorSchema(mesage=str(exc)), 400
        except DuplicateUserError as exc:
            return ErrorSchema(mesage=str(exc)), 409

    @app.post(
        "/auth/login",
        tags=[auth_tag],
        responses={"200": UserViewSchema, "400": ErrorSchema, "401": ErrorSchema},
    )
    def login(body: LoginSchema):
        use_case = get_login_user_use_case()
        try:
            user = use_case.execute(body.email, body.password)
            return UserViewSchema(id=user.id, email=user.email), 200
        except ValidationError as exc:
            return ErrorSchema(mesage=str(exc)), 400
        except InvalidCredentialsError as exc:
            return ErrorSchema(mesage=str(exc)), 401
