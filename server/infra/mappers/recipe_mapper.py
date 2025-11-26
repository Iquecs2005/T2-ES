from typing import List

from domain.entities.recipe import Recipe
from infra.db.models.recipe_model import RecipeModel

def to_domain(model: RecipeModel) -> Recipe:
    return Recipe(
        id=model.id,
        nome=model.nome,
        data_insercao=model.data_insercao,
    )
