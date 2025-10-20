# validator.py
from datetime import datetime
from regex_utils import find_all_multiple

def validar_fecha_str(fecha_str):
    """Intenta validar una fecha real con datetime."""
    for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y', '%d/%m/%y'):
        try:
            dt = datetime.strptime(fecha_str, fmt)
            return True, dt
        except ValueError:
            continue
    return False, None

def analizar_texto(texto):
    """Analiza el texto y devuelve un dict con resultados."""
    resultados = find_all_multiple(texto)
    for tipo, valores in resultados.items():
        if tipo == 'Fecha':
            resultados[tipo] = [
                f"{f} ✅ válida" if validar_fecha_str(f)[0] else f"{f} ❌ inválida"
                for f in valores
            ]
    return resultados