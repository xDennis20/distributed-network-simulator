from collections import deque

class Node:
    def __init__(self,nombre: str):
        self.nombre = nombre
        self.cola_entrada: list = []
        self.cola_salida: deque = deque()
        self.tabla_enrutamiento: dict[str,str] = {}
        self.estado: str = "activo"