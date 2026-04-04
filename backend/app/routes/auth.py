from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from schemas.user import UserLogin, UserCreate, UserResponse, TokenResponse
from services.auth_service import AuthService
from database.db_models import User

router = APIRouter(prefix="/auth")

auth_service = AuthService()

@router.post("/register", response_model=UserResponse)
def register(new_user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == new_user.email).first():
        raise HTTPException(status_code=400, detail="email has been registered")
    hashed_password = auth_service.hash_password(new_user.password.get_secret_value())
    new_user = User(
        email=new_user.email,
        full_name=new_user.full_name,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin,  db: Session = Depends(get_db)):
    if not (matched_user := db.query(User).filter(User.email == user.email).first()):
        raise HTTPException(status_code=404, detail="email has not been registered")
    
    if not auth_service.verify_password(user.password.get_secret_value(), matched_user.password_hash):
        raise HTTPException(status_code=401, detail="invalid password")

    token = auth_service.create_access_token(matched_user.email, matched_user.user_id)
    return TokenResponse(access_token=token)
