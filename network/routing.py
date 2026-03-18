from strategy.bfs import recorrer_bfs

def inicializar_enrutadores(nodos: dict):
    for nodo in nodos.values():
        recorrer_bfs(nodo,nodos)