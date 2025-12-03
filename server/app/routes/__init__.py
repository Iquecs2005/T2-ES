from app.routes.docs_routes import register_docs_routes
from app.routes.recipe_routes import register_recipe_routes
from app.routes.user_routes import register_user_routes

__all__ = [
    "register_docs_routes",
    "register_recipe_routes",
    "register_user_routes",
]
