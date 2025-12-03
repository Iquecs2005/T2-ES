from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship
from infra.db.base import Base

class RecipeModel(Base):
    __tablename__ = "receita"

    id: Optional[int] = Column("pk_receita", Integer, primary_key=True)
    titulo = Column(String(140), unique=False, nullable=False)
    descricao = Column(String(300), unique=False, nullable=False)
    modo_preparo = Column(String(1000), unique=False, nullable=False)
    preco = Column(Float, nullable=False)
    data_insercao = Column(DateTime, default=datetime.now(timezone.utc))
