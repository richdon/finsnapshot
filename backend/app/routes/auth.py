from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from schemas.user import UserCreate, UserResponse
from services.auth_service import AuthService
from database.db_models import User

router = APIRouter(prefix="/auth")

auth_service = AuthService()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="email has been registered")
    hashed_password = auth_service.hash_password(user.password.get_secret_value())
    new_user = User(
        email=user.email,
        full_name=user.full_name,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
