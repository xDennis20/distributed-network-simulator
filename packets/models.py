from dataclasses import dataclass, field
from itertools import count
from datetime import datetime

generador_id = count(1)
@dataclass(frozen=True)
class Paquete:
    origen: str
    destino: str
    contenido: str
    prioridad: int
    tiempo_evento: datetime
    nodos_recorridos: list[str] = field(default_factory=list)
    id: int = field(default_factory=generador_id.__next__)