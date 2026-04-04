from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from config import AuthConfig

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self):
        self.config = AuthConfig()
        
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
    
    def create_access_token(self, email: str, user_id: str):
        encode = {
            "sub": email,
            "id": user_id,
            "exp": datetime.now() + timedelta(minutes=self.config.jwt_expiration)
        }
        return jwt.encode(encode, self.config.secret_key, algorithm=self.config.jwt_algorithm)
    
    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.config.secret_key, algorithms=[self.config.jwt_algorithm])
            return payload
        except JWTError:
            return None
        
    def token_expired(self, token: str) -> bool:
        try:
            payload = jwt.decode(token, self.config.secret_key, algorithms=[self.config.jwt_algorithm])
            exp = payload.get("exp")
            return datetime.now() > datetime.fromtimestamp(exp)
        except JWTError:
            return True
