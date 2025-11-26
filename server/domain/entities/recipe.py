from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Recipe:
    """Domain representation of a product."""

    nome: str
    data_insercao: datetime = field(default_factory=datetime.utcnow)
    #data_insercao: datetime = field(default_factory=datetime.now(datetime.timezone.utc))
    id: Optional[int] = None
