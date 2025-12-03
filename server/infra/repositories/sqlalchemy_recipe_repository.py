from typing import Callable, Optional

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
            model = RecipeModel(
                titulo=recipe.titulo,
                descricao=recipe.descricao,
                modo_preparo=recipe.modo_preparo,
                preco=recipe.preco,
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

    def get_by_id(self, recipe_id: int) -> Optional[Recipe]:
        session = self._session_factory()
        try:
            model = (
                session.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
            )
            return recipe_mapper.to_domain(model) if model else None
        finally:
            session.close()
