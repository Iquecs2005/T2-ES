class CoreError(Exception):
    """Base class for domain-level exceptions."""

class RecipeNotFound(CoreError):
    """Raised when a product lookup fails."""

class RecipeInvalidTitle(CoreError):
    """Raised when a product has a invalid title"""