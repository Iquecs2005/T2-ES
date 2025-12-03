from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI
from app.dependencies import (
    get_env_config_service,
    get_add_recipe_use_case,
    get_get_recipe_use_case,
    get_add_user_use_case,
    get_get_user_use_case,
)
from app.routes import (
    register_docs_routes,
    register_recipe_routes,
    register_user_routes,
)
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

    register_docs_routes(application)
    register_recipe_routes(
        application,
        add_use_case=get_add_recipe_use_case(),
        get_use_case=get_get_recipe_use_case(),
    )
    register_user_routes(
        application,
        add_use_case=get_add_user_use_case(),
        get_use_case=get_get_user_use_case(),
    )

    return application


app = create_app()

if __name__ == "__main__":
    app.run(debug=False)
