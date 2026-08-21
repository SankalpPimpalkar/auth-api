import jwt
from app.config import SECRET_KEY, ALGORITHM

def create_accesstoken(payload: dict) -> str:
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token