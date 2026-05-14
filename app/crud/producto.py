from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoUpdate


def get(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()


def create(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def update(db: Session, producto_id: int, data: ProductoUpdate):
    db_producto = get(db, producto_id)
    if not db_producto:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_producto, field, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def delete(db: Session, producto_id: int):
    db_producto = get(db, producto_id)
    if not db_producto:
        return None
    db.delete(db_producto)
    db.commit()
    return db_producto
