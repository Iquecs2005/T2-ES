from typing import List, Optional

from pydantic import BaseModel
from domain.entities.recipe import Recipe

class RecipeSchema(BaseModel):
    """Payload esperado para criação de receita."""

    nome: str

class RecipeViewSchema(BaseModel):
    """Representação de uma receita."""

    id: int
    nome: str

def apresenta_receita(receita: Recipe) -> dict:
    """Converte a entidade de domínio para resposta JSON."""
    return {
        "id": receita.id,
        "nome": receita.nome,
    }