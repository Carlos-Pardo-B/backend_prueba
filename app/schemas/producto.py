from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProductoBase(BaseModel):
    name: str
    stock: int


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    name: Optional[str] = None
    stock: Optional[int] = None


class ProductoOut(ProductoBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
