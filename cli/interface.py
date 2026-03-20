from network.topology import Grafo
from persistence.datos_json import cargar_json
from packets.models import Paquete
from datetime import datetime
import re

grafo = Grafo()
grafo.construir_red(cargar_json())

patron_apagar = r"(Apagando|Apagar)\s+(Nodo|Nodos)\s+([a-z]{1})"
patron_prender = r"(Prender?)\s+(Nodo)\s+([a-z]{1})"
patron_registrar = r"(Registrar|Agregar)\s+(paquetes?)"
patron_ticks = r"(Simular|Dar)\s+([0-9]+)\s+(pasos?)"
patron_salir = r"(Salir)\s*"

def iniciar_cli():
    salir = False
    while not salir:
        comando = input("-> ")

        if re.search(patron_registrar,comando,re.IGNORECASE):
            print("Registrando Paquete: ")
            origen = input("Origen: ").upper()
            nodo_origen = grafo.nodos.get(origen)
            while len(origen) > 1 or len(origen.strip()) == 0 or nodo_origen is None:
                if nodo_origen is None:
                    print("Error: El origen del paquete no existe en la red")
                print("Error: Origen tiene mas de un caracter o esta vacio")
                print("Por favor intente de nuevo")
                origen = input("Origen: ").upper()
                nodo_origen = grafo.nodos.get(origen)

            destino = input("Destino: ").upper()
            nodo_destino = grafo.nodos.get(destino)
            while len(destino) > 1 or len(destino.strip()) == 0 or nodo_destino is None:
                if nodo_destino is None:
                    print("Error: El destino del paquete no existe en la red")
                print("Error: Destino o destino contienen mas de un valor o estan vacios")
                print("Por favor intente de nuevo")
                destino = input("Destino: ").upper()
                nodo_destino = grafo.nodos.get(destino)

            contenido = input("Contenido: ")
            while True:
                try:
                    prioridad = int(input("Prioridad (Solo numeros enteros): "))
                    break
                except ValueError:
                    print("Error: Ingrese un valor entero")

            tiempo_evento = datetime.now()
            paquete = Paquete(origen,destino,contenido,prioridad,tiempo_evento)
            nodo_origen.agregar_paquete(paquete)
            print(f"✔ Paquete {paquete.id} encolado en el nodo {paquete.origen}")

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

iniciar_cli()