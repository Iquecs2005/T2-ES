from flask_openapi3 import APIBlueprint, Tag
from pydantic import BaseModel, EmailStr, Field

from app.dependencies import (
    get_login_user_use_case,
    get_register_user_use_case,
)
from domain.exceptions import (
    DuplicateUserError,
    InvalidCredentialsError,
    ValidationError,
)


auth_tag = Tag(name="Auth", description="User authentication")

router = APIBlueprint("auth", __name__, url_prefix="/auth", abp_tags=[auth_tag])


class SignUpBody(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, description="User password")


class LoginBody(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, description="User password")


@router.post("/signup", tags=[auth_tag])
def signup(body: SignUpBody):
    use_case = get_register_user_use_case()

    try:
        user = use_case.execute(body.email, body.password)
        return {"id": user.id, "email": user.email}, 201
    except ValidationError as exc:
        return {"error": str(exc)}, 400
    except DuplicateUserError as exc:
        return {"error": str(exc)}, 409


@router.post("/login", tags=[auth_tag])
def login(body: LoginBody):
    use_case = get_login_user_use_case()

    try:
        user = use_case.execute(body.email, body.password)
        return {"id": user.id, "email": user.email}, 200
    except ValidationError as exc:
        return {"error": str(exc)}, 400
    except InvalidCredentialsError as exc:
        return {"error": str(exc)}, 401
