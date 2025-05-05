from pydantic import BaseModel
from typing import List

# Modelo de Usuario
class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

# Modelo de Producto
class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

# Modelo de Pedido
class Pedido(BaseModel):
    id: int
    usuario_id: int
    productos: List[int]  # Lista de IDs de productos
