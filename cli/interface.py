from network.topology import Grafo
from persistence.datos_json import cargar_json
import re

grafo = Grafo()
grafo.construir_red(cargar_json())


patron_apagar = r"(Apagando|Apagar)\s+(Nodo|Nodos)\s+([a-z]{1})"
patron_prender = r"(Prender?)\s+(Nodo)\s+([a-z]{1})"
patron_registrar = r"(Registrar)\s+(paquetes?)"
patron_ticks = r"(Simular|Dar)\s+([0-9]+)\s+(pasos?)"
patron_salir = r"(Salir)\s*"

def iniciar_cli():
    salir = False
    while not salir:
        comando = input("-> ")

        if re.search(patron_registrar,comando,re.IGNORECASE):
            print("Registrar paquete")
        elif re.search(patron_apagar,comando,re.IGNORECASE):
            print("Apagando Nodo")
        elif re.search(patron_prender,comando,re.IGNORECASE):
            print("Prender nodo")
        elif re.search(patron_ticks,comando,re.IGNORECASE):
            print("Simulando")
        elif re.search(patron_salir,comando,re.IGNORECASE):
            print("Saliendo del sistema...")
            salir = True
        else:
            print("Comando desconocido")
