from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db
from fastapi import HTTPException

router = APIRouter(prefix="/productos", tags=["productos"])

# Endpoint para obtener todos los productos
@router.get("/", response_model=List[schemas.ProductoOut])
def obtener_productos(db: Session = Depends(get_db)):
    productos = db.query(models.Producto).all()
    return productos

# Endpoint para crear un solo producto
@router.post("/", response_model=schemas.ProductoOut)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = models.Producto(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

# Endpoint para crear productos en lote
@router.post("/bulk", response_model=List[schemas.ProductoOut])
def crear_productos_en_lote(productos: List[schemas.ProductoCreate], db: Session = Depends(get_db)):
    nuevos_productos = []
    for producto_data in productos:
        nuevo_producto = models.Producto(**producto_data.dict())
        db.add(nuevo_producto)
        nuevos_productos.append(nuevo_producto)
    db.commit()
    for p in nuevos_productos:
        db.refresh(p)
    return nuevos_productos

# Endpoint para eliminar un producto
@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(models.Producto).filter(models.Producto.id_producto == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}

# Endpoint para eliminar productos en un rango
@router.delete("/rango/{inicio}/{fin}")
def eliminar_productos_rango(inicio: int, fin: int, db: Session = Depends(get_db)):
    productos = db.query(models.Producto).filter(models.Producto.id_producto.between(inicio, fin)).all()
    if not productos:
        raise HTTPException(status_code=404, detail="No se encontraron productos en el rango especificado")
    for producto in productos:
        db.delete(producto)
    db.commit()
    return {"mensaje": f"Productos con ID del {inicio} al {fin} eliminados correctamente"}

# Endpoint para actualizar un producto
@router.put("/productos/{id_producto}", response_model=schemas.ProductoOut)
def actualizar_producto(id_producto: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = db.query(models.Producto).filter(models.Producto.id_producto == id_producto).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Actualizar los campos que no sean None
    for key, value in producto.dict(exclude_unset=True).items():
        setattr(db_producto, key, value)

    db.commit()
    db.refresh(db_producto)
    return db_producto
