from network.node import Node
from packets.models import Paquete

class Grafo:
    def __init__(self):
        self.nodos: dict[str,Node] = {}

    def agregar_nodo(self,valor: str) -> None:
        nodo = Node(valor)
        self.nodos[valor] = nodo

    def construir_red(self, nodos: dict[str,list[str]]) -> None:
        for nombre,vecino in nodos.items():
            self.agregar_nodo(nombre)
            nodo = self.nodos.get(nombre)
            nodo.vecinos = vecino

    def generador_ticks(self):
        while True:
            for nodo in self.nodos.values():
                nodo.procesar_paquete()
            for nodo in self.nodos.values():
                if len(nodo.cola_salida) > 0:
                    paquete = nodo.mandar_paquete()
                    self.pasar_paquete(paquete)
            yield "Tick completado"

    def pasar_paquete(self, paquete: tuple[Paquete,str]):
        paquete, siguiente_salto = paquete
        nodo_destino = self.nodos.get(siguiente_salto)
        nodo_destino.agregar_paquete(paquete)

    def __str__(self):
        return f"Grafo: {self.nodos}"