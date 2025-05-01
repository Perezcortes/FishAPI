from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base

class Producto(Base):
    __tablename__ = "productos"

    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    descripcion = Column(Text)
    precio = Column(Float)
    stock = Column(Integer)
    marca = Column(String(100))
    imagen = Column(String(255))
