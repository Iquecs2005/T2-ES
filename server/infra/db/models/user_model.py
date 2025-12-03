from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, String

from infra.db.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Optional[int] = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
