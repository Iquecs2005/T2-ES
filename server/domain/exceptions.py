class CoreError(Exception):
    """Base class for domain-level exceptions."""

class RecipeNotFound(CoreError):
    """Raised when a product lookup fails."""

class RecipeInvalidTitle(CoreError):
    """Raised when a product has a invalid title"""
class DomainError(Exception):
    """Base exception for domain errors."""


class ValidationError(DomainError):
    """Raised when input data is invalid."""


class DuplicateUserError(DomainError):
    """Raised when trying to create a user that already exists."""


class InvalidCredentialsError(DomainError):
    """Raised when authentication data is invalid."""
