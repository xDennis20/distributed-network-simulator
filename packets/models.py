from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)
class Paquete:
    id: int
    fuente: str
    destino: str
    contenido: str
    prioridad: int
    tiempo_evento: datetime
    nodos_recorridos: list[str] = field(default_factory=list)