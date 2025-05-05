from fastapi import FastAPI, HTTPException
from models import Usuario, Producto, Pedido
from gestor_archivos import GestorArchivos

# Instanciamos los gestores para cada modelo
gestor_usuarios = GestorArchivos(Usuario, "usuarios.json")
gestor_productos = GestorArchivos(Producto, "productos.json")
gestor_pedidos = GestorArchivos(Pedido, "pedidos.json")

app = FastAPI()

# Endpoints para Producto
@app.get("/productos")
def listar_productos():
    return gestor_productos.get_all()

@app.get("/productos/{id}")
def obtener_producto(id: int):
    try:
        return gestor_productos.get_by_id(id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.post("/productos")
def crear_producto(producto: Producto):
    gestor_productos.add(producto)
    return producto

@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    try:
        gestor_productos.update(id, producto.dict())
        return {"msg": "Producto actualizado correctamente"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    try:
        gestor_productos.delete(id)
        return {"msg": "Producto eliminado correctamente"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

# Endpoints para Usuario
@app.get("/usuarios")
def listar_usuarios():
    return gestor_usuarios.get_all()

@app.get("/usuarios/{id}")
def obtener_usuario(id: int):
    try:
        return gestor_usuarios.get_by_id(id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    gestor_usuarios.add(usuario)
    return usuario

@app.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: Usuario):
    try:
        gestor_usuarios.update(id, usuario.dict())
        return {"msg": "Usuario actualizado correctamente"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    try:
        gestor_usuarios.delete(id)
        return {"msg": "Usuario eliminado correctamente"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoints para Pedido
@app.get("/pedidos")
def listar_pedidos():
    return gestor_pedidos.get_all()

@app.get("/pedidos/{id}")
def obtener_pedido(id: int):
    try:
        return gestor_pedidos.get_by_id(id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

@app.post("/pedidos")
def crear_pedido(pedido: Pedido):
    gestor_pedidos.add(pedido)
    return pedido

@app.put("/pedidos/{id}")
def actualizar_pedido(id: int, pedido: Pedido):
    try:
        gestor_pedidos.update(id, pedido.dict())
        return {"msg": "Pedido actualizado correctamente"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

@app.delete("/pedidos/{id}")
def eliminar_pedido(id: int):
    try:
        gestor_pedidos.delete(id)
        return {"msg": "Pedido eliminado correctamente"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")


