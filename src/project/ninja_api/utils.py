import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings

def create_access_token(user_id: int, username: str) -> str:
    """Генерирует JWT Access Token для пользователя."""
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {
        "sub": str(user_id),                # subject — кому выдан токен
        "username": username,
        "exp": expire,                      # expiration — когда истекает
        "iat": datetime.now(timezone.utc),  # issued at — когда выдан
    }
    # PyJWT сам кодирует словарь и возвращает строковый токен
    encoded_jwt = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt
