from network.node import Node
from strategy.bfs import recorrer_bfs
from  persistence.datos_json import cargar_json

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

    def inicializar_enrutadores(self):
        for nodo in self.nodos.values():
            recorrer_bfs(nodo,self.nodos)
            print(nodo.tabla_enrutamiento)


    def __str__(self):
        return f"Grafo: {self.nodos}"
