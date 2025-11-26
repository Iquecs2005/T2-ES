from typing import Callable, List, Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from domain.entities.recipe import Recipe
from domain.interfaces.recipe_repository import RecipeRepository
from infra.db.models.recipe_model import RecipeModel
from infra.mappers import recipe_mapper


class SqlAlchemyProductRepository(RecipeRepository):
    """SQLAlchemy implementation of the recipe repository port."""

    def __init__(self, session_factory: Callable[[], Session]):
        self._session_factory = session_factory

    def add(self, recipe: Recipe) -> Recipe:
        session = self._session_factory()
        try:
            model = RecipeModel(
                nome=recipe.nome,
                data_insercao=recipe.data_insercao,
            )
            session.add(model)
            session.commit()
            session.refresh(model)
            return recipe_mapper.to_domain(model)
        except IntegrityError:
            session.rollback()
            raise
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
