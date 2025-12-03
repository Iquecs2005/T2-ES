from flask_openapi3 import Tag
from app.schemas import (
    ErrorSchema,
    RecipeSchema,
    RecipeViewSchema,
    RecipeSearchByIdSchema,
    apresenta_receita,
)
from domain.exceptions import RecipeNotFound
from domain.use_cases.add_recipe import AddRecipeUseCase
from domain.use_cases.get_recipe import GetRecipeUseCase

receita_tag = Tag(
    name="Receita",
    description="Adição, visualização e remoção de receitas à base",
)


def register_recipe_routes(
    app, add_use_case: AddRecipeUseCase, get_use_case: GetRecipeUseCase
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
            return {"mesage": "Não foi possível salvar novo item :/"}, 400

    @app.get(
        "/receita",
        tags=[receita_tag],
        responses={
            "200": RecipeViewSchema,
            "404": ErrorSchema,
        },
    )
    def get_receita(query: RecipeSearchByIdSchema):
        try:
            receita = get_use_case.execute(id=query.id)
            return apresenta_receita(receita), 200
        except RecipeNotFound as error:
            return {"message": str(error)}, 404
