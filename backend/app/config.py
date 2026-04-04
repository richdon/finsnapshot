import os

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class DatabaseConfig:
    db_url: str = os.getenv("DATABASE_URL")

@dataclass
class AuthConfig:
    secret_key: str = os.getenv("JWT_SECRET_KEY")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM")
    jwt_expiration: int = int(os.getenv("JWT_EXPIRATION_MINUTES", "60"))
    