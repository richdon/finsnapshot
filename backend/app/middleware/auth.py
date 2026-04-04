from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.auth_service import AuthService
from sqlalchemy.orm import Session
from database.session import get_db
from database.db_models import User


auth_service = AuthService()

security = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(security), 
                     db: Session = Depends(get_db)):
    if auth_service.token_expired(token.credentials):
        raise HTTPException(status_code=401, detail="token has expired")
    
    if not (payload := auth_service.decode_token(token.credentials)):
        raise HTTPException(status_code=403, detail="invalid token")
    
    if not (user := db.query(User).filter(User.user_id == payload["id"]).first()):
        raise HTTPException(status_code=401, detail="invalid token: user not found")

    if user.email != payload["sub"]:
       raise HTTPException(status_code=401, detail="invalid token: credential do not match")  
       
    return user
