from urllib.parse import unquote

from flask_openapi3 import Tag
from app.schemas import (
    ErrorSchema,
    RecipeSchema,
    RecipeViewSchema,
    apresenta_receita
)
from domain.exceptions import RecipeNotFound
from domain.use_cases.add_recipe import AddRecipeUseCase

receita_tag = Tag(
    name="Receita",
    description="Adição, visualização e remoção de receitas à base",
)

def register_recipe_routes(
    app,
    add_use_case: AddRecipeUseCase,
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
            print("a")
            receita = add_use_case.execute(
                titulo=form.titulo,
                descricao=form.descricao,
                modo_preparo=form.modo_preparo,
                preco=form.preco,
            )
            return apresenta_receita(receita), 200
        except Exception:
            return {"mesage": "Não foi possível salvar novo item :/"}, 400
