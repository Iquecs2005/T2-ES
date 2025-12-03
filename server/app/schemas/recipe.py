from typing import List, Optional

from pydantic import BaseModel
from domain.entities.recipe import Recipe

class RecipeSchema(BaseModel):
    """Payload esperado para criação de receita."""

    titulo: str
    descricao: str
    modo_preparo: str
    preco: float

class RecipeViewSchema(BaseModel):
    """Representação de uma receita."""

    id: int
    titulo: str
    descricao: str
    modo_preparo: str
    preco: float

def apresenta_receita(receita: Recipe) -> dict:
    """Converte a entidade de domínio para resposta JSON."""
    return {
        "id": receita.id,
        "titulo": receita.titulo,
        "descricao": receita.descricao,
        "modo_preparo": receita.modo_preparo,
        "preco": receita.preco,
    }