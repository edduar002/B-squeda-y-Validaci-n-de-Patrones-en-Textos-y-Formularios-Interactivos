"""
main_gui.py

Módulo principal que implementa la interfaz gráfica del proyecto:
“Búsqueda y Validación de Patrones en Textos y Formularios Interactivos”.

Este archivo define la estructura visual y la lógica de interacción entre el
usuario y el sistema. Permite cargar un texto, analizarlo en busca de patrones
(correos, teléfonos, URLs, fechas, etc.) y mostrar los resultados de manera clara
y ordenada.

Autor: Eduardo Cortes Pineda, Luis Manuel Osorio Medina y Andres Felipe Ruiz Escarraga
Fecha: 20/10/2025
Versión: 1.0
"""

# ---------------------------------------------------------------------------------
# Importación de librerías y módulos del proyecto
# ---------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from validator import analizar_texto  # Función principal de análisis léxico-sintáctico
from examples import EJEMPLO_COMPLETO  # Texto de ejemplo con múltiples patrones

# ---------------------------------------------------------------------------------
# Funciones de la Interfaz Gráfica
# ---------------------------------------------------------------------------------
def ejecutar_analisis():
    """
    Ejecuta el proceso de análisis del texto ingresado en la interfaz.

    1. Obtiene el texto desde el cuadro de entrada.
    2. Valida que no esté vacío.
    3. Llama a la función `analizar_texto` para procesar el contenido.
    4. Muestra los resultados en el área de salida.
    """
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor ingresa o carga un texto.")
        return

    # Procesamiento del texto mediante expresiones regulares
    resultados = analizar_texto(texto)

    # Limpieza y habilitación del área de salida
    salida_texto.configure(state='normal')
    salida_texto.delete("1.0", tk.END)
    total = 0

    # Iteración por tipo de patrón encontrado
    for tipo, valores in resultados.items():
        if valores:
            # Título del tipo de patrón (ej: "Correos (2 encontrados):")
            salida_texto.insert(tk.END, f"🔹 {tipo} ({len(valores)} encontrados):\n", 'titulo')

            # Imprime cada coincidencia hallada
            for v in valores:
                salida_texto.insert(tk.END, f"   - {v}\n")
            salida_texto.insert(tk.END, "\n")
            total += len(valores)

    # Si no se detectaron coincidencias
    if total == 0:
        salida_texto.insert(tk.END, "No se encontraron coincidencias.")

    # Deshabilita la edición del área de salida
    salida_texto.configure(state='disabled')


def limpiar_campos():
    """
    Limpia el área de texto de entrada y el área de resultados.
    """
    entrada_texto.delete("1.0", tk.END)
    salida_texto.configure(state='normal')
    salida_texto.delete("1.0", tk.END)
    salida_texto.configure(state='disabled')


def cargar_ejemplo():
    """
    Carga automáticamente un texto de ejemplo (definido en examples.py)
    en el área de entrada para facilitar la demostración del programa.
    """
    entrada_texto.delete("1.0", tk.END)
    entrada_texto.insert(tk.END, EJEMPLO_COMPLETO)


# ---------------------------------------------------------------------------------
# Configuración de la ventana principal (Interfaz Gráfica)
# ---------------------------------------------------------------------------------
root = tk.Tk()
root.title("Validador de Patrones - Proyecto Python")
root.geometry("900x600")
root.resizable(False, False)

# ---------------------------------------------------------------------------------
# Encabezado principal
# ---------------------------------------------------------------------------------
ttk.Label(root, text="🔍 Proyecto: Validador de Patrones",
          font=("Arial", 14, "bold")).pack(pady=10)

# ---------------------------------------------------------------------------------
# Área de entrada de texto
# ---------------------------------------------------------------------------------
ttk.Label(root, text="Texto para analizar:", font=("Arial", 11, "bold")).pack(anchor='w', padx=20)
entrada_texto = scrolledtext.ScrolledText(root, width=100, height=12, wrap=tk.WORD)
entrada_texto.pack(padx=20, pady=5)

# ---------------------------------------------------------------------------------
# Botones de acción
# ---------------------------------------------------------------------------------
frame_btn = ttk.Frame(root)
frame_btn.pack(pady=10)

# Cada botón ejecuta una de las funciones definidas arriba
ttk.Button(frame_btn, text="Analizar", command=ejecutar_analisis).grid(row=0, column=0, padx=10)
ttk.Button(frame_btn, text="Limpiar", command=limpiar_campos).grid(row=0, column=1, padx=10)
ttk.Button(frame_btn, text="Cargar ejemplo", command=cargar_ejemplo).grid(row=0, column=2, padx=10)
ttk.Button(frame_btn, text="Salir", command=root.destroy).grid(row=0, column=3, padx=10)

# ---------------------------------------------------------------------------------
# Área de salida (resultados del análisis)
# ---------------------------------------------------------------------------------
ttk.Label(root, text="Resultados del análisis:", font=("Arial", 11, "bold")).pack(anchor='w', padx=20)
salida_texto = scrolledtext.ScrolledText(root, width=100, height=14, wrap=tk.WORD, state='disabled')
salida_texto.pack(padx=20, pady=5)

# Configuración del estilo para los títulos de secciones
salida_texto.tag_config('titulo', font=('Arial', 10, 'bold'), foreground='blue')

# ---------------------------------------------------------------------------------
# Ciclo principal de ejecución
# ---------------------------------------------------------------------------------
root.mainloop()