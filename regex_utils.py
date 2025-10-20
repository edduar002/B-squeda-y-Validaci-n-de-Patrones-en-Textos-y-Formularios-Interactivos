"""
regex_utils.py

Módulo encargado de definir y aplicar las expresiones regulares utilizadas
en el proyecto “Validador de Patrones”.

Este archivo contiene:
- Un diccionario con patrones precompilados (`PATTERNS`) para distintos tipos de datos.
- Funciones que permiten buscar coincidencias en un texto dado.

Autor: Eduardo Cortes Pineda
Fecha: 20/10/2025
Versión: 1.0
"""

import re  # Módulo estándar de Python para trabajar con expresiones regulares

# ---------------------------------------------------------------------------------
# Diccionario de patrones precompilados
# ---------------------------------------------------------------------------------
# Cada entrada del diccionario asocia un tipo de dato con una expresión regular
# precompilada para optimizar la búsqueda de coincidencias.
PATTERNS = {
    # ----------------------------------------------------------
    # 1. Correos electrónicos
    # ----------------------------------------------------------
    # Explicación:
    # - (?i): bandera que hace la búsqueda insensible a mayúsculas/minúsculas.
    # - [a-z0-9._%+-]+ : nombre del usuario (caracteres válidos antes del @)
    # - @[a-z0-9.-]+ : dominio
    # - \.[a-z]{2,} : dominio de nivel superior (mínimo 2 letras, ej. .com, .org)
    'Correo electrónico': re.compile(
        r'(?i)\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b'
    ),

    # ----------------------------------------------------------
    # 2. Números de teléfono
    # ----------------------------------------------------------
    # Explicación:
    # - Permite códigos de país opcionales (+57, +1, etc.)
    # - Acepta espacios o guiones como separadores.
    # - Reconoce teléfonos con 6 a 8 dígitos al final.
    'Teléfono': re.compile(
        r'\b(?:\+\d{1,3}[ -]?)?(?:\(\d{2,3}\)[ -]?|\d{2,4}[ -]?)?\d{6,8}\b'
    ),

    # ----------------------------------------------------------
    # 3. Fechas
    # ----------------------------------------------------------
    # Explicación:
    # - Permite formatos DD/MM/AAAA, DD-MM-AAAA, o AAAA-MM-DD.
    # - Valida días (00–31), meses (00–12) y años de 4 dígitos.
    'Fecha': re.compile(
        r'\b(?:[0-3]?\d[\/\-][01]?\d[\/\-](?:\d{4}))|(?:\d{4}[\-][01]?\d[\-][0-3]?\d)\b'
    ),

    # ----------------------------------------------------------
    # 4. Cédula / ID
    # ----------------------------------------------------------
    # Explicación:
    # - Busca secuencias numéricas de 6 a 12 dígitos.
    # - No permite letras ni símbolos.
    'Cédula / ID': re.compile(
        r'\b\d{6,12}\b'
    ),

    # ----------------------------------------------------------
    # 5. Código Postal
    # ----------------------------------------------------------
    # Explicación:
    # - Reconoce códigos numéricos de exactamente 5 dígitos.
    # - Muy útil para sistemas postales como el colombiano.
    'Código Postal': re.compile(
        r'\b\d{5}\b'
    ),

    # ----------------------------------------------------------
    # 6. URL o enlace web
    # ----------------------------------------------------------
    # Explicación:
    # - Detecta direcciones web con o sin “http://” o “https://”.
    # - Permite dominios con múltiples niveles (.com, .co, .org, etc.).
    # - Incluye parámetros opcionales o rutas (/, ?, =, etc.).
    'URL': re.compile(
        r'\b(?:https?:\/\/)?(?:www\.)?[\w\-]+(?:\.[\w\-]+)+(?:[\w\-\._~:\/?#@!$&\'()*+,;=%]*)\b'
    ),

    # ----------------------------------------------------------
    # 7. Placa de vehículo
    # ----------------------------------------------------------
    # Explicación:
    # - Acepta formatos comunes:
    #     ABC-123  → autos
    #     CD456EF  → motos
    # - Solo letras mayúsculas (A-Z) y números (0-9).
    'Placa de vehículo': re.compile(
        r'\b(?:[A-Z]{3}\-?\d{3}|[A-Z]{2}\d{3}[A-Z]{2})\b'
    )
}


# ---------------------------------------------------------------------------------
# Funciones de búsqueda
# ---------------------------------------------------------------------------------
def find_all(text: str, kind: str):
    """
    Busca todas las coincidencias de un tipo específico dentro de un texto.

    Parámetros:
        text (str): Texto donde se realizará la búsqueda.
        kind (str): Tipo de patrón a buscar (debe estar en PATTERNS).

    Retorna:
        list[str]: Lista de todas las coincidencias encontradas.

    Excepciones:
        ValueError: Si el tipo especificado no existe en el diccionario de patrones.
    """
    pattern = PATTERNS.get(kind)
    if not pattern:
        raise ValueError(f"Tipo desconocido: {kind}")
    return pattern.findall(text)


def find_all_multiple(text: str, kinds=None):
    """
    Busca coincidencias de múltiples tipos de patrones en un mismo texto.

    Parámetros:
        text (str): Texto a analizar.
        kinds (list[str], opcional): Lista de claves específicas del diccionario PATTERNS.
                                     Si no se especifica, analiza todos los patrones.

    Retorna:
        dict[str, list[str]]: Un diccionario donde las claves son los tipos de patrones
                              y los valores son listas con las coincidencias encontradas.
    """
    kinds = kinds or PATTERNS.keys()
    return {k: find_all(text, k) for k in kinds}