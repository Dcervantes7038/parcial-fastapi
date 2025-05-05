import json
import os
from typing import Type, TypeVar, List
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class GestorArchivos:
    """Clase genérica para operaciones CRUD sobre archivos JSON."""
    def __init__(self, modelo: Type[T], ruta_archivo: str):
        self.modelo = modelo
        self.ruta = ruta_archivo
        if not os.path.exists(self.ruta):
            with open(self.ruta, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def _leer_archivo(self) -> List[T]:
        """Lee el archivo JSON y devuelve una lista de instancias del modelo."""
        with open(self.ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return [self.modelo(**item) for item in datos]

    def _escribir_archivo(self, objetos: List[T]) -> None:
        """Vuelca las instancias del modelo al archivo JSON."""
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump([objeto.dict() for objeto in objetos], f, indent=4)

    def get_all(self) -> List[T]:
        """Devuelve todos los objetos en el archivo JSON."""
        return self._leer_archivo()

    def get_by_id(self, id: int) -> T:
        """Devuelve un objeto por su ID. Lanza un error si no se encuentra."""
        for obj in self._leer_archivo():
            if obj.id == id:
                return obj
        raise ValueError(f"Elemento con id={id} no encontrado")

    def add(self, objeto: T) -> None:
        """Agrega un nuevo objeto al archivo JSON."""
        objetos = self._leer_archivo()
        objetos.append(objeto)
        self._escribir_archivo(objetos)

    def update(self, id: int, datos: dict) -> None:
        """Actualiza un objeto existente con el ID dado. Lanza un error si no se encuentra."""
        objetos = self._leer_archivo()
        for idx, obj in enumerate(objetos):
            if obj.id == id:
                objeto_actualizado = self.modelo(**{**obj.dict(), **datos})
                objetos[idx] = objeto_actualizado
                self._escribir_archivo(objetos)
                return
        raise ValueError(f"Elemento con id={id} no encontrado")

    def delete(self, id: int) -> None:
        """Elimina un objeto por su ID. Lanza un error si no se encuentra."""
        objetos = self._leer_archivo()
        nuevos = [obj for obj in objetos if obj.id != id]
        if len(nuevos) == len(objetos):
            raise ValueError(f"Elemento con id={id} no encontrado")
        self._escribir_archivo(nuevos)
