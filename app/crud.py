from sqlalchemy.orm import Session
from . import models, schemas

def obtener_productos(db: Session):
    return db.query(models.Producto).all()

def crear_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto
