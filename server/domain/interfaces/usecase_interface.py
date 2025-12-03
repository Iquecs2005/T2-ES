from abc import ABC, abstractmethod
from typing import Any


class UseCase(ABC):
    """Base interface for use cases."""

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError
