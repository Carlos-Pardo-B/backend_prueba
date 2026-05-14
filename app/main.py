from fastapi import FastAPI
from app.api.v1.router import api_router
from app.config import settings
from app.db.session import engine, Base
import app.models.producto  # noqa: ensure model registered before create_all

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix="/api/v1")
