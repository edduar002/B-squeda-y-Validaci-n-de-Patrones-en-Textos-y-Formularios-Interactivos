# regex_utils.py
import re

# Diccionario de patrones
PATTERNS = {
    'Correo electrónico': re.compile(r'(?i)\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b'),
    'Teléfono': re.compile(r'\b(?:\+\d{1,3}[ -]?)?(?:\(\d{2,3}\)[ -]?|\d{2,4}[ -]?)?\d{6,8}\b'),
    'Fecha': re.compile(r'\b(?:[0-3]?\d[\/\-][01]?\d[\/\-](?:\d{4}))|(?:\d{4}[\-][01]?\d[\-][0-3]?\d)\b'),
    'Cédula / ID': re.compile(r'\b\d{6,12}\b'),
    'Código Postal': re.compile(r'\b\d{5}\b'),
    'URL': re.compile(r'\b(?:https?:\/\/)?(?:www\.)?[\w\-]+(?:\.[\w\-]+)+(?:[\w\-\._~:\/?#@!$&\'()*+,;=%]*)\b'),
    'Placa de vehículo': re.compile(r'\b(?:[A-Z]{3}\-?\d{3}|[A-Z]{2}\d{3}[A-Z]{2})\b')
}

def find_all(text: str, kind: str):
    """Encuentra todas las coincidencias de un tipo específico."""
    pattern = PATTERNS.get(kind)
    if not pattern:
        raise ValueError(f"Tipo desconocido: {kind}")
    return pattern.findall(text)

def find_all_multiple(text: str, kinds=None):
    """Devuelve un dict con listas de coincidencias por tipo."""
    kinds = kinds or PATTERNS.keys()
    return {k: find_all(text, k) for k in kinds}