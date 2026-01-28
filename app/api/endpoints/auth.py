from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.config import settings
from app.models.auth import Token, UserDB, UserCreate
from app.utils.auth import verify_password, create_access_token, get_password_hash


router = APIRouter(prefix="/auth", tags=["authentification"])


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_from_db(form_data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )

    token_data = {
        "sub": user.username,
        "user_id": user.id,
        "role": user.role
    }

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES)
    access_token = create_access_token(
        data=token_data,
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
