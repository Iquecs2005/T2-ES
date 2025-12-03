from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship
from infra.db.base import Base

class UserModel(Base):
    __tablename__ = "usuario"

    login = Column(String(30), unique=False, nullable=False, primary_key=True)
    senha = Column(String(30), unique=False, nullable=False)
    data_insercao = Column(DateTime, default=datetime.now(timezone.utc))