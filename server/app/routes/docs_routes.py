from flask import redirect
from flask_openapi3 import Tag

docs_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)


def register_docs_routes(app) -> None:
    @app.get("/", tags=[docs_tag])
    def home():
        """Redireciona para a interface padrão de documentação."""
        return redirect("/openapi")
