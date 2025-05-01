from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routes import productos

# Crear las tablas
models.Base.metadata.create_all(bind=engine)

# Inicializar la aplicación
app = FastAPI()

# Configurar CORS (puedes limitar el origen si prefieres)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # o ["*"] durante desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir el router de productos
app.include_router(productos.router)
