from contextlib import contextmanager
from pathlib import Path
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from domain.config.settings import DATABASE_URL, DATABASE_DIR
from infra.db.base import Base
from infra.repositories import sqlalchemy_user_repository  
from infra.db.models import RecipeModel

DATABASE_DIR.mkdir(parents=True, exist_ok=True)


def _ensure_sqlite_directory(database_url: str) -> None:
    if database_url.startswith("sqlite:///"):
        db_path = Path(database_url.replace("sqlite:///", ""))
        db_path.parent.mkdir(parents=True, exist_ok=True)


def build_engine(database_url: Optional[str] = None):
    url = database_url or DATABASE_URL
    if not url:
        raise RuntimeError("DATABASE_URL não configurado")
    _ensure_sqlite_directory(url)
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    engine = create_engine(url, connect_args=connect_args, future=True, pool_pre_ping=True)

    # Cria o banco se não existir (para SQLite e outros dialetos suportados pelo sqlalchemy_utils)
    if not database_exists(engine.url):
        create_database(engine.url)

    # Cria as tabelas registradas no metadata
    Base.metadata.create_all(engine)
    return engine


engine = build_engine()

SessionLocal = scoped_session(
    sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False, future=True)
)


@contextmanager
def session_scope() -> Session:
    """Context manager para garantir commit/rollback."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
