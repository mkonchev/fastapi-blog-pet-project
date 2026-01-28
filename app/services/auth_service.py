from datetime import datetime
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.auth import UserDB

class AuthService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

    fake_users_db = {
        "admin": UserDB(
            id=1,
            username="admin",
            email="admin@example.com",
            hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            is_active=True,
            role="admin",
            created_at=datetime.now()
        ),
        "user": UserDB(
            id=2,
            username="user",
            email="user@example.com",
            hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            is_active=True,
            role="user",
            created_at=datetime.now()
        )
    }


    def get_user_from_db(username: str) -> UserDB | None:
        return fake_users_db.get(username)

    async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserDB: