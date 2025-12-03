import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = Path(os.getenv("LOG_DIR", PROJECT_ROOT / "log"))

# Por padrão, usa SQLite local para permitir rodar apenas com "python -m app.main".
# Se definir DATABASE_URL no ambiente (ex.: Postgres), ele será usado em vez do SQLite.
DATABASE_DIR = Path(os.getenv("DATABASE_DIR", PROJECT_ROOT / "database"))
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DATABASE_DIR / 'db.sqlite3'}")
