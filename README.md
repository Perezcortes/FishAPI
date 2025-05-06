# 🐟 API fishapi Para productos de pesca 

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.95.0-009688?logo=fastapi&style=for-the-badge" alt="FastAPI">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.0-red?logo=python&style=for-the-badge" alt="SQLAlchemy">
</div>

API RESTful desarrollada con **FastAPI** y **SQLAlchemy** para gestionar productos de una tienda. Esta API permite listar, crear (individual o en lote), actualizar y eliminar productos.

---

## 📁 Estructura del proyecto

```
perezcortes-fishapi/
├── requirements.txt
└── app/
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    ├── schemas.py
    └── routes/
        └── productos.py
```

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Perezcortes/FishAPI.git
cd perezcortes-fishapi
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copia el archivo de ejemplo `.env.example` y crea tu propio `.env`:

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales:

```
DATABASE_URL=mysql+pymysql://root:'Tu contraseña'fishapi''@localhost/'nombre de la DB'
```

> 📌 Asegúrate de que el servidor MySQL esté corriendo y que exista la base de datos, ejemplo: `fishapi_db`.

---

## 🚀 Ejecución del servidor

```bash
uvicorn app.main:app --reload
```

## 🧪 Documentación con Swagger
FastAPI genera automáticamente la documentación de la API en Swagger:

Swagger UI: http://127.0.0.1:8000/docs

Redoc UI: http://127.0.0.1:8000/redoc



La API estará disponible en: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Endpoints disponibles

### Productos

| Método | Endpoint                        | Descripción                            |
|--------|----------------------------------|----------------------------------------|
| GET    | `/productos/`                   | Obtener todos los productos            |
| POST   | `/productos/`                   | Crear un nuevo producto                |
| POST   | `/productos/bulk`               | Crear productos en lote                |
| DELETE | `/productos/{producto_id}`      | Eliminar un producto por ID            |
| DELETE | `/productos/rango/{inicio}/{fin}` | Eliminar productos por rango de IDs |
| PUT    | `/productos/productos/{id}`     | Actualizar un producto por ID          |

---

## 🧾 Requisitos

Archivo `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
pymysql
python-dotenv
```

---

## 📌 Notas

- Se recomienda usar herramientas como [Insomnia](https://insomnia.rest/) o [Postman](https://www.postman.com/) para probar los endpoints.
- La API incluye configuración CORS para permitir peticiones desde `http://localhost:3000` (por ejemplo, un frontend en React).

---

## 👤 Autor

[📧 9531447499a@gmail.com](mailto:9531447499a@gmail.com)  
[💻 GitHub: @Perezcortes](https://github.com/Perezcortes)
