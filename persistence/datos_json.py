import json
from pathlib import Path

def cargar_json():
    ruta_exacta = Path(__file__).parent / "topologia.json"

    with open(ruta_exacta, mode="r") as topologia:
        archivo = json.load(topologia)

    return archivo