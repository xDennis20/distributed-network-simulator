# 🌐 Simulador de Enrutamiento de Redes Distribuidas

## 📖 Sobre el Proyecto
Este proyecto es un simulador backend paso a paso (basado en ticks) que modela el enrutamiento de paquetes de datos a través de una red distribuida. 
Resuelve el problema de encontrar la ruta más eficiente para el envío de información, priorizando paquetes críticos y reaccionando dinámicamente a caídas de nodos en tiempo real.

## ✨ Características Principales
* **Enrutamiento Dinámico:** Recálculo de rutas en tiempo real ante la caída de un nodo (usando BFS).
* **Sistema de Prioridades:** Gestión de paquetes mediante Colas de Prioridad (`heapq`).
* **Arquitectura Orientada a Eventos:** Simulación controlada por "ticks" de tiempo.
* **Carga de Topología:** Generación de la red a partir de archivos JSON.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Estructuras de Datos:** Grafos, Colas de Prioridad (Heap), Deques, Diccionarios.
* **Patrones:** Single Responsibility Principle (SRP), Inyección de Dependencias.
* **Librerías Nativas:** `collections`, `heapq`, `dataclasses`, `json`.

## 🧠 Arquitectura del Nodo
Cada dispositivo (Nodo) en la red está diseñado de forma independiente con:
1. **Cola de Entrada (Ingress):** Ordena los paquetes entrantes por nivel de prioridad.
2. **Cola de Salida (Egress):** Cola FIFO para despachar los paquetes procesados.
3. **Tabla de Enrutamiento:** Mapa local para decidir el siguiente salto óptimo.

## 🚀 Cómo ejecutarlo
(Aquí pondremos las instrucciones de la terminal cuando el código esté listo, por ejemplo: `python main.py`)