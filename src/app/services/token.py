import jwt
from ...app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from ..models.token import TokenData, Token
from datetime import datetime, timedelta, timezone
from ..utils.exceptions import TokenInvalidError
from typing import Dict, Any

def create_accesstoken(data: TokenData, expiry_delta: timedelta | None = None) -> Token:

    if expiry_delta:
        expire = datetime.now(timezone.utc) + expiry_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    data.exp = expire
    token = jwt.encode(data.model_dump(), SECRET_KEY, algorithm=ALGORITHM)
    return Token(access_token=token)

def verify_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except (jwt.PyJWTError, AttributeError):
        raise TokenInvalidError("Could not validate credentials.")