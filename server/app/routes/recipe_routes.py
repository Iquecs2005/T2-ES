from flask_openapi3 import Tag
from app.schemas import (
    ErrorSchema,
    RecipeSchema,
    RecipeViewSchema,
    apresenta_receita,
)
from domain.exceptions import RecipeNotFound
from domain.use_cases.add_recipe import AddRecipeUseCase
from domain.use_cases.view_recipe import ViewRecipeUseCase

receita_tag = Tag(
    name="Receita",
    description="Adicao, visualizacao e remocao de receitas a base",
)


def register_recipe_routes(
    app,
    add_use_case: AddRecipeUseCase,
    view_use_case: ViewRecipeUseCase,
) -> None:
    @app.post(
        "/receita",
        tags=[receita_tag],
        responses={
            "200": RecipeViewSchema,
            "400": ErrorSchema,
        },
    )
    def add_receita(form: RecipeSchema):
        try:
            receita = add_use_case.execute(
                titulo=form.titulo,
                descricao=form.descricao,
                modo_preparo=form.modo_preparo,
                preco=form.preco,
            )
            return apresenta_receita(receita), 200
        except Exception:
            return {"mesage": "Nao foi possivel salvar novo item :/"}, 400

    @app.get(
        "/receita/<int:receita_id>",
        tags=[receita_tag],
        responses={
            "200": RecipeViewSchema,
            "404": ErrorSchema,
        },
    )
    def get_receita(receita_id: int):
        try:
            receita = view_use_case.execute(receita_id)
            return apresenta_receita(receita), 200
        except RecipeNotFound as exc:
            return {"mesage": str(exc)}, 404
