import re

from domain.exceptions import ValidationError


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def normalize_email(email: str) -> str:
    if email is None:
        raise ValidationError("E-mail é obrigatório")
    normalized = email.strip().lower()
    if not normalized or not EMAIL_PATTERN.match(normalized):
        raise ValidationError("E-mail inválido")
    return normalized


def validate_password(password: str) -> str:
    if password is None:
        raise ValidationError("Senha é obrigatória")
    cleaned = password.strip()
    if len(cleaned) < 6:
        raise ValidationError("Senha deve ter pelo menos 6 caracteres")
    return cleaned
