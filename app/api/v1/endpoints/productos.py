from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.crud import producto as crud
from app.schemas.producto import ProductoCreate, ProductoUpdate, ProductoOut

router = APIRouter()


@router.get("/", response_model=List[ProductoOut])
def list_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(db, skip=skip, limit=limit)


@router.post("/", response_model=ProductoOut, status_code=201)
def create_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crud.create(db, producto)


@router.get("/{producto_id}", response_model=ProductoOut)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    db_prod = crud.get(db, producto_id)
    if not db_prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_prod


@router.put("/{producto_id}", response_model=ProductoOut)
def update_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    db_prod = crud.update(db, producto_id, producto)
    if not db_prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_prod


@router.delete("/{producto_id}", response_model=ProductoOut)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    db_prod = crud.delete(db, producto_id)
    if not db_prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_prod
