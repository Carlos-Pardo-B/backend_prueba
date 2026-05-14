from fastapi import APIRouter
from app.api.v1.endpoints import productos

api_router = APIRouter()
api_router.include_router(productos.router, prefix="/productos", tags=["productos"])
