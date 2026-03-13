from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Paquete:
    id: int
    fuente: str
    destino: str
    contenido: str
    prioridad: int
    tiempo_evento: datetime