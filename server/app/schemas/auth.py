from pydantic import BaseModel, EmailStr, Field


class SignUpSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, description="Senha do usuário")


class LoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, description="Senha do usuário")


class UserViewSchema(BaseModel):
    id: int
    email: EmailStr
