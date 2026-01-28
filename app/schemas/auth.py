from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    # refresh_token: str


class TokenData(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None
    role: Optional[str] = None


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserDB(UserBase):
    id: int
    hashed_password: str
    is_active: bool
    role: str = "user"
    created_at: datetime

    class Config:
        from_attributes = True


class UserPublic(UserBase):
    id: int
    is_active: bool
    role: str
