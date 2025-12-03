from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, String
from infra.db.base import Base

class UserModel(Base):
    __tablename__ = "usuario"

    login = Column(String(30), unique=False, nullable=False, primary_key=True)
    senha = Column(String(30), unique=False, nullable=False)
    data_insercao = Column(DateTime, default=datetime.now(timezone.utc))