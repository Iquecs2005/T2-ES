from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

@dataclass
class User:
    """Domain representation of a user."""

    login: str
    senha: str
    data_insercao: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __init__(self, login, senha, data_insercao = None):
        self.login = login
        self.senha = senha

        if (data_insercao == None):
            self.data_insercao = datetime.now(timezone.utc)
        else:
            self.data_insercao = data_insercao
