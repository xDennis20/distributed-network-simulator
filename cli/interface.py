from network.topology import Grafo
from network.routing import inicializar_enrutadores
from persistence.datos_json import cargar_json
from packets.models import Paquete
from datetime import datetime
from collections import deque
import re

grafo = Grafo()
grafo.construir_red(cargar_json())

patron_apagar = r"(Apagando|Apagar)\s+(Nodo|Nodos)\s+([a-z]{1})"
patron_prender = r"(Prender?|Encender)\s+(Nodo)\s+([a-z]{1})"
patron_registrar = r"(Registrar|Agregar)\s+(paquetes?)"
patron_ticks = r"(Simular|Dar)\s+([0-9]+)\s+(pasos?)"
patron_salir = r"(Salir)\s*"
ticks = grafo.generador_ticks()
inicializar_enrutadores(grafo.nodos)

def iniciar_cli():
    paquetes: deque[Paquete] = deque()
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
            paquetes.appendleft(paquete)
            print(f"✔ Paquete {paquete.id} encolado en el nodo {paquete.origen}")

        elif dato_nodo := re.search(patron_apagar,comando,re.IGNORECASE):
            nodo = grafo.nodos.get(dato_nodo[3].upper())
            if nodo is not None:
                if nodo.estado == "desactivado":
                    print(f"La red '{nodo.nombre}' ya fue apagado anteriormente")
                else:
                    nodo.estado = "desactivado"
                    inicializar_enrutadores(grafo.nodos)
                    print(f"La red '{nodo.nombre}' fue apagado")
            else:
                print("El nodo a apagar no existe en la red")
                continue

        elif dato_nodo := re.search(patron_prender,comando,re.IGNORECASE):
            nodo = grafo.nodos.get(dato_nodo[3].upper())
            if nodo is not None:
                if nodo.estado == "activo":
                    print(f"La red '{nodo.nombre}' esta encendido")
                else:
                    nodo.estado = "activo"
                    inicializar_enrutadores(grafo.nodos)
                    print(f"La red '{nodo.nombre} fue encendido'")
            else:
                print("EL nodo a prender no existe en la red")
                continue

        elif dato_tick := re.search(patron_ticks,comando,re.IGNORECASE):
            for n in range(int(dato_tick[2])):
                eventos = (next(ticks))
                print(f"\n--- ⏱️ TICK {n + 1} ---")

                if not eventos:
                    print("No hay paquetes registrados")
                    break
                else:
                    evento = "\n".join(eventos)
                    print(evento)
            for paquete in paquetes:
                recorrido = f"📦 Paquete #{paquete.id}. " + "->".join(paquete.nodos_recorridos)
                print(recorrido)

        elif re.search(patron_salir,comando,re.IGNORECASE):
            print("Saliendo del sistema...")
            salir = True
        else:
            print("Comando desconocido")

iniciar_cli()