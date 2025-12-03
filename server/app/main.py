from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI
from app.dependencies import (
    get_env_config_service,
    get_engine,
)
from app.routes import register_auth_routes, register_docs_routes
from infra.logging import configure_logging

config_service = get_env_config_service()

info = Info(
    title=config_service.get_service_name(),
    version=config_service.get_service_version(),
)

def create_app() -> OpenAPI:
    configure_logging()
    application = OpenAPI(__name__, info=info)
    CORS(application)
    # Garante criação do banco/tabelas na inicialização
    get_engine()
    register_docs_routes(application)
    register_auth_routes(application)

    return application

app = create_app()

if __name__ == "__main__":
    app.run(debug=False)
