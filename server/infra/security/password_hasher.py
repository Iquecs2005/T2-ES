from werkzeug.security import check_password_hash, generate_password_hash

from domain.services import PasswordHasher


class WerkzeugPasswordHasher(PasswordHasher):
    def hash_password(self, password: str) -> str:
        return generate_password_hash(password)

    def verify_password(self, password: str, password_hash: str) -> bool:
        return check_password_hash(password_hash, password)
