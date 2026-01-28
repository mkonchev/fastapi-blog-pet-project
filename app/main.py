from fastapi import FastAPI
from app.api.endpoints import users
# from database.database import get_db


app = FastAPI()

app.include_router(users.router)


@app.get("/")
def health_check():
    return {"UserService": "works"}
