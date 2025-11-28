from pathlib import Path
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from domain.config.settings import DATABASE_URL


Base = declarative_base()


def _ensure_sqlite_directory(database_url: str) -> None:
    if database_url.startswith("sqlite:///"):
        db_path = Path(database_url.replace("sqlite:///", ""))
        db_path.parent.mkdir(parents=True, exist_ok=True)


def create_engine_from_url(database_url: Optional[str] = None):
    url = database_url or DATABASE_URL
    _ensure_sqlite_directory(url)
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, connect_args=connect_args, future=True)


def create_session_factory(engine=None, database_url: Optional[str] = None):
    eng = engine or create_engine_from_url(database_url)
    return sessionmaker(bind=eng, autoflush=False, autocommit=False, future=True)


def init_db(engine) -> None:
    Base.metadata.create_all(bind=engine)
