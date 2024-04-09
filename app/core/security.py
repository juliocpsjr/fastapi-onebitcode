from passlib.context import CryptContext
from typing import Union, Any
from jose import jwt
from core.config import settings
from datetime import datetime, timedelta

password_context = CryptContext(
    schemes= ['bcrypt'],
    deprecated='auto'
)

# Criptografia da senha
def get_password(password: str) -> str:
    return password_context.hash(password)

# Descriptografia da senha
def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(datetime.UTC) + expires_delta
    else:
        expires_delta = datetime.now(datetime.UTC) + timedelta(
            minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES
        )
    info_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }

    jwt_encoded = jwt.encode(
        info_jwt,
        settings.JWT_SECRET_KEY,
        settings.ALGORITHM
    )

    return jwt_encoded

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(datetime.UTC) + expires_delta
    else:
        expires_delta = datetime.now(datetime.UTC) + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
    info_jwt = {
        "exp": expires_delta,
        "sub": str(subject)
    }

    jwt_encoded = jwt.encode(
        info_jwt,
        settings.JWT_REFRESH_SECRET_KEY,
        settings.ALGORITHM
    )

    return jwt_encoded