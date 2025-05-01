from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    marca: str
    imagen: str

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None
    marca: Optional[str] = None
    imagen: Optional[str] = None

    class Config:
        orm_mode = True

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id_producto: int

    class Config:
        orm_mode = True
