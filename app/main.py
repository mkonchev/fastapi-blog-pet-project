from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.api.endpoints import users
from app.api.endpoints import auth
from app.database.database import engine, Base, get_db


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     print("Database tables created successfully")
#     yield
#     await engine.dispose()
#     print("Database connection closed")

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def health_check():
    return {"UserService": "works"}


# @app.get("/db_health")
# async def db_health(db: AsyncSession = Depends(get_db)):
#     try:
#         await db.execute(text("SELECT 1"))
#         return {"status": "healthy", "database": "connected"}
#     except Exception as e:
#         raise HTTPException(
#             status_code=503,
#             detail=f"Database connection failed: {str(e)}"
#         )
