from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.routes import auth
from app.db.session import engine
from app.db.base import Base

from app.models.user import User  # noqa
from app.models.query import Query  # noqa


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        # to back : Alembic   
        await conn.run_sync(Base.metadata.create_all)        
    yield
        
        
app = FastAPI(
    title="RAG Lab Support API",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
    description="Medical equipment technical support with RAG",
    version="1.0.0"
)

app.include_router(auth.router,prefix=f"{settings.API_V1_STR}/auth", tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "RAG Lab Support API is running", "status": "healthy"}

