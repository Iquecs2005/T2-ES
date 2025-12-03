from domain.entities.recipe import Recipe
from infra.db.models.recipe_model import RecipeModel


def to_domain(model: RecipeModel) -> Recipe:
    return Recipe(
        id=model.id,
        titulo=model.titulo,
        descricao=model.descricao,
        modo_preparo=model.modo_preparo,
        preco=model.preco,
        data_insercao=model.data_insercao,
    )
