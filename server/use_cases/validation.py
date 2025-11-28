import re

from domain.exceptions import ValidationError


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def normalize_email(email: str) -> str:
    if email is None:
        raise ValidationError("Email is required")
    normalized = email.strip().lower()
    if not normalized or not EMAIL_PATTERN.match(normalized):
        raise ValidationError("Invalid email")
    return normalized


def validate_password(password: str) -> str:
    if password is None:
        raise ValidationError("Password is required")
    cleaned = password.strip()
    if len(cleaned) < 6:
        raise ValidationError("Password must be at least 6 characters long")
    return cleaned
