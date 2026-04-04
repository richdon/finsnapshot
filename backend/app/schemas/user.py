from typing import Annotated
from pydantic import BaseModel, SecretStr, Field


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: Annotated[SecretStr, Field(min_length=5)]

    
class UserResponse(BaseModel):
    user_id: int
    full_name: str
    email: str
    model_config = {"from_attributes": True}


class UserLogin(BaseModel):
    email: str
    password: Annotated[SecretStr, Field(min_length=5)]


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
