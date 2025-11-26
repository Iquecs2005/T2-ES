from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship
from infra.db.base import Base

class RecipeModel(Base):
    __tablename__ = "receita"

    id: Optional[int] = Column("pk_receita", Integer, primary_key=True)
    nome = Column(String(140), unique=True, nullable=False)
    data_insercao = Column(DateTime, default=datetime.utcnow)
