from typing import List, Optional

from pydantic import BaseModel
from domain.entities.user import User
from datetime import datetime

class UserSchema(BaseModel):
    """Payload esperado para criação de receita."""

    login: str
    senha: str

class UserViewSchema(BaseModel):
    """Representação de uma User."""

    login: str
    data_insercao: datetime

def apresenta_user(user: User) -> dict:
    """Converte a entidade de domínio para resposta JSON."""
    return {
        "login": user.login,
        "data_insercao": user.data_insercao,
    }