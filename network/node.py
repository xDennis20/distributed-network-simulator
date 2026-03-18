from collections import deque
from packets.models import Paquete
from typing import Optional
import heapq

class Node:
    def __init__(self,nombre: str):
        self.validar_nombre(nombre)
        self.nombre = nombre
        self.cola_entrada: list = []
        self.cola_salida: deque = deque()
        self.vecinos: list[str] = []
        self.tabla_enrutamiento: dict[str,Optional[str]] = {}
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

    def procesar_paquete(self) -> str:
        if not self.cola_entrada:
            return "VACIO"
        paquete_procesar = heapq.heappop(self.cola_entrada)
        paquete = paquete_procesar[2]
        if paquete.destino == self.nombre:
            return "ENTREGADO"
        if self.tabla_enrutamiento.get(paquete.destino) is None:
            return "DESCARTADO"
        else:
            siguiente_salto = self.tabla_enrutamiento.get(paquete.destino)
            if siguiente_salto is not None:
                self.cola_salida.append((paquete, siguiente_salto))
            return "ENRUTADO"

    def mandar_paquete(self) -> tuple:
        return self.cola_salida.popleft()

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nombre={self.nombre}, paquetes= {len(self.cola_entrada)}"
