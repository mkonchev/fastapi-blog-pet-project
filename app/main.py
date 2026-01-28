from fastapi import FastAPI, Depends, HTTPException
# from database.database import get_db


app = FastAPI()


def get_current_user():
    return {"user_id": 1, "username": "admin", "role": "admin"}


@app.get("/profile")
def get_profile(user=Depends(get_current_user)):
    user_id = user["user_id"]
    username = user.get("username", "empty")

    return {
        "message": f"Hello, {username}",
        "user_id": user_id,
        "is_admin": user.get("role") == "admin"
    }


@app.get("/admin")
def get_admin(user=Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="You don't have permission"
        )
    return {
        "message": "Welcome to admin panel",
        "user_id": user["user_id"],
        "username": user["username"]
    }
