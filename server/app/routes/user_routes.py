from flask_openapi3 import Tag
from app.schemas import ErrorSchema, UserSchema, UserViewSchema, apresenta_user
from domain.exceptions import UserNotFound
from domain.use_cases.add_user import AddUserUseCase
from domain.use_cases.get_user import GetUserUseCase

receita_tag = Tag(
    name="Receita",
    description="Adição, visualização e remoção de receitas à base",
)


def register_user_routes(
    app,
    add_use_case: AddUserUseCase,
    get_use_case: GetUserUseCase,
) -> None:
    @app.post(
        "/user",
        tags=[receita_tag],
        responses={
            "200": UserViewSchema,
            "400": ErrorSchema,
        },
    )
    def add_user(form: UserSchema):
        try:
            user = add_use_case.execute(
                login=form.login,
                senha=form.senha,
            )
            return apresenta_user(user), 200
        except Exception:
            return {"mesage": "Não foi possível salvar novo item :/"}, 400

    @app.get(
        "/user",
        tags=[receita_tag],
        responses={
            "200": UserViewSchema,
            "404": ErrorSchema,
        },
    )
    def get_user(query: UserSchema):
        try:
            user = get_use_case.execute(login=query.login, senha=query.senha)
            return apresenta_user(user), 200
        except UserNotFound as error:
            return {"message": str(error)}, 404
