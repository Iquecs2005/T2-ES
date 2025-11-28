from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class User:
    id: Optional[int]
    email: str
    password_hash: str
