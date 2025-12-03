from typing import Callable, List, Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from domain.entities.recipe import Recipe
from domain.interfaces.recipe_repository import RecipeRepository
from infra.db.models.recipe_model import RecipeModel
from infra.mappers import recipe_mapper


class SqlAlchemyRecipeRepository(RecipeRepository):
    """SQLAlchemy implementation of the recipe repository port."""

    def __init__(self, session_factory: Callable[[], Session]):
        self._session_factory = session_factory

    def add(self, recipe: Recipe) -> Recipe:
        session = self._session_factory()
        try:
            print("c")
            model = RecipeModel(
                titulo=recipe.titulo,
                descricao=recipe.descricao,
                modo_preparo=recipe.modo_preparo,
                preco=recipe.preco,
                data_insercao=recipe.data_insercao,
            )
            print("InicioProblema")
            session.add(model)
            print("depois do add")
            session.commit()
            print("depois do commit")
            session.refresh(model)
            print("depois do refresh")
            return recipe_mapper.to_domain(model)
        except IntegrityError:
            session.rollback()
            raise
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
