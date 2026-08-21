from typing import cast
from decouple import config
from sqlalchemy import URL

SECRET_KEY = cast(str, config("SECRET_KEY", default=None))
ALGORITHM = cast(str, config("ALGORITHM", default="HS256"))
ACCESS_TOKEN_EXPIRE_MINUTES = cast(int, config("ACCESS_TOKEN_EXPIRE_MINUTES", default=43200)) # 30d


DB_URL = cast(str, config("DB_URL", default="sqlite:///database.db"))

required_settings = {
    "SECRET_KEY": SECRET_KEY,
}

missing_settings = [
    name for name, value in required_settings.items() if not value
]

if missing_settings:
    raise RuntimeError(
        f"Missing required configuration settings: {', '.join(missing_settings)}"
    )
