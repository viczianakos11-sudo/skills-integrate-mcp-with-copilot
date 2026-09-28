import hashlib
import hmac
import secrets


PBKDF2_ITERATIONS = 310_000


def hash_password(password: str) -> dict[str, str]:
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS
    )
    return {"salt": salt.hex(), "password_hash": password_hash.hex()}


def verify_password(password: str, credential: dict[str, str]) -> bool:
    try:
        salt = bytes.fromhex(credential["salt"])
        expected_hash = bytes.fromhex(credential["password_hash"])
    except (KeyError, TypeError, ValueError):
        return False

    actual_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS
    )
    return hmac.compare_digest(actual_hash, expected_hash)