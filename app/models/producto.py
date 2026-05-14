from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class Producto(Base):
    __tablename__ = "Productos"

    id        = Column(Integer, primary_key=True, index=True)
    name      = Column(String, nullable=False)
    stock     = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())