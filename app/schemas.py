from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    marca: str
    imagen: str

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id_producto: int  # cambiado aquí también

    class Config:
        orm_mode = True
