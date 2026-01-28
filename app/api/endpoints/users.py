from fastapi import APIRouter, Depends, HTTPException
from services.user_service import UserService


router = APIRouter(prefix="/users", tags=["users"])


def get_user_service() -> UserService:
    return UserService()


@router.get("/profile")
def get_profile(service: UserService = Depends(get_user_service)):
    user = service.get_current_user()

    return {
        "message": f"Hello, {user.get('username', 'guest')}",
        "user_id": user["user_id"],
        "is_admin": service.is_admin(user)
    }


@router.get("/admin")
def get_admin(service: UserService = Depends(get_user_service)):
    user = service.get_current_user()

    try:
        service.validate_user_access(user)
    except PermissionError:
        raise HTTPException(
            status_code=403,
            detail="You don't have admin privileges"
        )

    return {
        "message": "Welcome to admin panel",
        "user_id": user["user_id"],
        "username": user.get("username")
    }
