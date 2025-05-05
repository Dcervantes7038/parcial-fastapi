from gestor_archivos import GestorArchivos
from pydantic import BaseModel

# Definimos un modelo de prueba rápido
class Item(BaseModel):
    id: int
    nombre: str

# Instanciamos el gestor con un archivo temporal
gestor = GestorArchivos(Item, "data/test_items.json")

# Asegurémonos de empezar limpio (borra el archivo si existe)
import os
if os.path.exists("data/test_items.json"):
    os.remove("data/test_items.json")
gestor = GestorArchivos(Item, "data/test_items.json")

# 1) Probar add()
item1 = Item(id=1, nombre="Prueba uno")
gestor.add(item1)

# 2) Probar get_all()
todos = gestor.get_all()
print("get_all:", todos)

# 3) Probar get_by_id()
uno = gestor.get_by_id(1)
print("get_by_id(1):", uno)

# 4) Probar update()
gestor.update(1, {"nombre": "Prueba UNO modificada"})
mod = gestor.get_by_id(1)
print("Después de update:", mod)

# 5) Probar delete()
gestor.delete(1)
restantes = gestor.get_all()
print("Después de delete, get_all:", restantes)
