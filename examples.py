"""
examples.py

Este módulo contiene ejemplos de texto utilizados para probar el funcionamiento del
proyecto "Búsqueda y Validación de Patrones en Textos y Formularios Interactivos".

El texto de ejemplo incluye diferentes tipos de datos estructurados
(como correos electrónicos, números telefónicos, fechas, cédulas, códigos postales,
URLs y placas de vehículos), los cuales sirven para validar las expresiones
regulares implementadas en el sistema.

Autor: Eduardo Cortes Pineda
Fecha: 20/10/2025
Versión: 1.0
"""

# ---------------------------------------------------------------------------------
# Variable global de ejemplo
# ---------------------------------------------------------------------------------

EJEMPLO_COMPLETO = """
Hola, mi correo es juan.perez@example.com y mi número de teléfono es +57 300 4567890.
También puedes escribirme a contacto@empresa.co.
Nací el 29/02/2024 y mi cédula es 1029384756.
Mi código postal es 110111.
Visita nuestro sitio web: https://www.tecnored.com o http://blog.tecnored.com.
La placa de mi carro es ABC-123 y la de mi moto es CD456EF.
"""

# ---------------------------------------------------------------------------------
# Descripción:
# Este texto contiene múltiples patrones reconocibles:
#   - Correos electrónicos: "juan.perez@example.com", "contacto@empresa.co"
#   - Número telefónico: "+57 300 4567890"
#   - Fecha: "29/02/2024"
#   - Cédula: "1029384756"
#   - Código postal: "110111"
#   - URLs: "https://www.tecnored.com", "http://blog.tecnored.com"
#   - Placas: "ABC-123", "CD456EF"
#
# Este ejemplo se utiliza principalmente en la interfaz gráfica (main_gui.py)
# para probar la detección y validación de los patrones definidos en el módulo
# regex_utils.py.
# ---------------------------------------------------------------------------------