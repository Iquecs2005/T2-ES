from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

from domain.exceptions import RecipeInvalidTitle

@dataclass
class Recipe:
    """Domain representation of a product."""

    titulo: str
    descricao: str
    modo_preparo: str
    preco: float
    data_insercao: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: Optional[int] = None

    def __init__(self, titulo, descricao, modo_preparo, preco):
        if not isinstance(titulo, str):
            raise TypeError("titulo must be a string")
        if not isinstance(descricao, str):
            raise TypeError("descricao must be a string")
        if not isinstance(modo_preparo, str):
            raise TypeError("modo_preparo must be a string")
        if not isinstance(preco, float) and not isinstance(preco, int):
            raise TypeError("preco must be a float")

        lenTitulo = len(titulo)
        if lenTitulo > 140:
            raise RecipeInvalidTitle("titulo must be less than 140 characters")
        elif lenTitulo == 0:
            raise RecipeInvalidTitle("titulo must not be empty string")

        self.titulo = titulo
        self.descricao = descricao
        self.modo_preparo = modo_preparo
        self.preco = preco

    #data_insercao: datetime = field(default_factory=datetime.now(datetime.timezone.utc))
