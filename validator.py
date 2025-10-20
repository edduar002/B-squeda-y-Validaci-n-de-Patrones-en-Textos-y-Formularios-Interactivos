"""
validator.py

Módulo encargado de analizar textos y validar los patrones encontrados
mediante expresiones regulares, especialmente las fechas.

Este archivo actúa como un puente entre el motor de detección (regex_utils.py)
y la interfaz de usuario (main_gui.py), añadiendo una capa de validación
lógica sobre los datos encontrados.

Autor: Eduardo Cortes Pineda
Fecha: 20/10/2025
Versión: 1.0
"""

from datetime import datetime
from regex_utils import find_all_multiple


# ---------------------------------------------------------------------------------
# Función: validar_fecha_str
# ---------------------------------------------------------------------------------
def validar_fecha_str(fecha_str):
    """
    Intenta validar una fecha en formato de texto utilizando distintos formatos.

    Parámetros:
        fecha_str (str): Cadena de texto que representa una fecha (por ejemplo, '29/02/2024').

    Retorna:
        tuple[bool, datetime | None]:
            - bool: True si la fecha es válida, False si no lo es.
            - datetime | None: Objeto datetime resultante si la fecha es válida,
              de lo contrario, None.

    Detalles:
        - La función intenta convertir la cadena a un objeto datetime utilizando
          diferentes formatos comunes:
              '%d/%m/%Y' → Ejemplo: 29/02/2024
              '%Y-%m-%d' → Ejemplo: 2024-02-29
              '%d-%m-%Y' → Ejemplo: 29-02-2024
              '%d/%m/%y' → Ejemplo: 29/02/24
        - Si la conversión falla en todos los formatos, se considera una fecha inválida.
    """
    for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y', '%d/%m/%y'):
        try:
            # Intentar parsear la fecha según el formato actual
            dt = datetime.strptime(fecha_str, fmt)
            return True, dt  # Fecha válida
        except ValueError:
            # Si no coincide el formato, continuar con el siguiente
            continue
    # Si ninguno de los formatos fue válido
    return False, None


# ---------------------------------------------------------------------------------
# Función: analizar_texto
# ---------------------------------------------------------------------------------
def analizar_texto(texto):
    """
    Analiza el texto y devuelve un diccionario con los resultados de coincidencias
    y validaciones correspondientes.

    Parámetros:
        texto (str): Texto a analizar, ingresado por el usuario o cargado desde ejemplo.

    Retorna:
        dict[str, list[str]]:
            Un diccionario donde las claves representan el tipo de patrón
            (por ejemplo, 'Correo electrónico', 'Fecha', etc.)
            y los valores son listas con las coincidencias encontradas.

    Funcionamiento:
        1. Se utiliza la función `find_all_multiple` del módulo regex_utils
           para encontrar todas las coincidencias posibles de los patrones definidos.
        2. Si el tipo de patrón es 'Fecha', cada coincidencia se valida con
           `validar_fecha_str()` para determinar si la fecha realmente existe.
        3. Las fechas válidas se marcan con "válida" y las inválidas con "inválida".
        4. Se devuelve el diccionario final, listo para ser mostrado en la interfaz gráfica.
    """
    # Buscar coincidencias de todos los patrones en el texto
    resultados = find_all_multiple(texto)

    # Procesar y validar las fechas encontradas
    for tipo, valores in resultados.items():
        if tipo == 'Fecha':
            resultados[tipo] = [
                f"{f} válida" if validar_fecha_str(f)[0] else f"{f} inválida"
                for f in valores
            ]

    # Devolver resultados con todas las coincidencias clasificadas
    return resultados