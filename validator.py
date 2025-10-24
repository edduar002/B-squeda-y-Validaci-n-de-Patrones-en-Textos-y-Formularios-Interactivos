"""
validator.py
Valida los distintos patrones encontrados por expresiones regulares,
indicando si cada coincidencia es válida o no.
"""

from datetime import datetime
from regex_utils import find_all_multiple


# ============================================================
# Funciones de validación individuales
# ============================================================

def validar_fecha_str(fecha_str):
    """Valida si una fecha existe realmente y está en formato coherente."""
    if '/' in fecha_str and '-' in fecha_str:
        return False

    formatos = ('%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y', '%d/%m/%y', '%Y/%m/%d')
    for fmt in formatos:
        try:
            datetime.strptime(fecha_str, fmt)
            return True
        except ValueError:
            continue
    return False


def validar_correo(correo):
    """Valida que el correo tenga un formato razonable y dominio válido."""
    return "@" in correo and "." in correo.split("@")[-1]


def validar_telefono(tel):
    """Valida que el número telefónico tenga entre 7 y 13 dígitos totales."""
    numeros = [c for c in tel if c.isdigit()]
    return 7 <= len(numeros) <= 13


def validar_cedula(cedula):
    """Valida cédulas numéricas entre 6 y 12 dígitos."""
    return cedula.isdigit() and 6 <= len(cedula) <= 12


def validar_codigo_postal(cp: str):
    """
    Valida si un código postal es correcto (5 o 6 dígitos numéricos).

    Acepta tanto códigos internacionales de 5 dígitos
    como colombianos de 6 dígitos (por ejemplo, 110111).
    """
    cp = cp.strip()  # eliminar espacios o saltos de línea
    return cp.isdigit() and 5 <= len(cp) <= 6


def validar_url(url):
    """Valida que la URL tenga dominio y formato correcto."""
    return url.startswith(("http://", "https://", "www."))


def validar_placa(placa):
    """Valida placas en formato colombiano (ABC-123 o CD456EF)."""
    import re
    return bool(re.match(r'^[A-Z]{3}-?\d{3}$', placa) or re.match(r'^[A-Z]{2}\d{3}[A-Z]{2}$', placa))


# ============================================================
# Función principal de análisis
# ============================================================

def analizar_texto(texto):
    """
    Analiza el texto y devuelve un diccionario con los resultados,
    marcando cada coincidencia como válida o inválida.
    """
    resultados = find_all_multiple(texto)

    for tipo, valores in resultados.items():
        validados = []
        for v in valores:
            if tipo == 'Fecha':
                valido = validar_fecha_str(v)
            elif tipo == 'Correo electrónico':
                valido = validar_correo(v)
            elif tipo == 'Teléfono':
                valido = validar_telefono(v)
            elif tipo == 'Cédula / ID':
                valido = validar_cedula(v)
            elif tipo == 'Código Postal':
                valido = validar_codigo_postal(v)
            elif tipo == 'URL':
                valido = validar_url(v)
            elif tipo == 'Placa de vehículo':
                valido = validar_placa(v)
            else:
                valido = True  # Por defecto

            estado = "✅ válida" if valido else "❌ inválida"
            validados.append(f"{v} → {estado}")
        resultados[tipo] = validados

    return resultados