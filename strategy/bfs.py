from collections import deque
from network.node import Node

def recorrer_bfs(inicio: Node,nodos: dict):
    visitados = set()
    cola = deque()
    nodo_origen = inicio
    cola.append((nodo_origen, nodo_origen))
    visitados.add(inicio.nombre)
    while cola:
        nodo_actual, paso_anterior = cola.popleft()
        for vecino in nodo_actual.vecinos:
            if vecino not in visitados:
                visitados.add(vecino)
                vecino = nodos.get(vecino)
                if vecino.estado == "desactivado":
                    nodo_origen.tabla_enrutamiento[vecino.nombre] = None
                else:
                    if nodo_actual.nombre != inicio.nombre:
                        nodo_origen.tabla_enrutamiento[vecino.nombre] = paso_anterior.nombre
                        cola.append((vecino, paso_anterior))
                    else:
                        nodo_origen.tabla_enrutamiento[vecino.nombre] = vecino.nombre
                        cola.append((vecino, vecino))