from collections import deque
from packets.models import Paquete
import heapq

class Node:
    def __init__(self,nombre: str):
        self.validar_nombre(nombre)
        self.nombre = nombre
        self.cola_entrada: list = []
        self.cola_salida: deque = deque()
        self.tabla_enrutamiento: dict[str,str] = {}
        self._estado: str = "activo"

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: str) -> None:
        if nuevo_estado in ["activo","desactivado"]:
            self._estado = nuevo_estado
        else:
            raise ValueError("Error: Estado invalido")

    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        if len(nombre.strip()) == 0:
            raise ValueError("Error: Nombre vacio")
        return True

    def agregar_paquete(self, paquete: Paquete) -> None:
        heapq.heappush(self.cola_entrada,(paquete.prioridad,paquete.id,paquete))

nodo = Node("A")