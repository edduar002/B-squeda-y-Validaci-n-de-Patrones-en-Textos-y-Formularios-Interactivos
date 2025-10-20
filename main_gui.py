# main_gui.py
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from validator import analizar_texto
from examples import EJEMPLO_COMPLETO

# Funciones GUI
def ejecutar_analisis():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor ingresa o carga un texto.")
        return
    resultados = analizar_texto(texto)

    salida_texto.configure(state='normal')
    salida_texto.delete("1.0", tk.END)
    total = 0
    for tipo, valores in resultados.items():
        if valores:
            salida_texto.insert(tk.END, f"🔹 {tipo} ({len(valores)} encontrados):\n", 'titulo')
            for v in valores:
                salida_texto.insert(tk.END, f"   - {v}\n")
            salida_texto.insert(tk.END, "\n")
            total += len(valores)
    if total == 0:
        salida_texto.insert(tk.END, "No se encontraron coincidencias.")
    salida_texto.configure(state='disabled')

def limpiar_campos():
    entrada_texto.delete("1.0", tk.END)
    salida_texto.configure(state='normal')
    salida_texto.delete("1.0", tk.END)
    salida_texto.configure(state='disabled')

def cargar_ejemplo():
    entrada_texto.delete("1.0", tk.END)
    entrada_texto.insert(tk.END, EJEMPLO_COMPLETO)

# Interfaz principal
root = tk.Tk()
root.title("Validador de Patrones - Proyecto Python")
root.geometry("900x600")
root.resizable(False, False)

ttk.Label(root, text="🔍 Proyecto: Validador de Patrones", font=("Arial", 14, "bold")).pack(pady=10)

ttk.Label(root, text="Texto para analizar:", font=("Arial", 11, "bold")).pack(anchor='w', padx=20)
entrada_texto = scrolledtext.ScrolledText(root, width=100, height=12, wrap=tk.WORD)
entrada_texto.pack(padx=20, pady=5)

# Botones
frame_btn = ttk.Frame(root)
frame_btn.pack(pady=10)
ttk.Button(frame_btn, text="Analizar", command=ejecutar_analisis).grid(row=0, column=0, padx=10)
ttk.Button(frame_btn, text="Limpiar", command=limpiar_campos).grid(row=0, column=1, padx=10)
ttk.Button(frame_btn, text="Cargar ejemplo", command=cargar_ejemplo).grid(row=0, column=2, padx=10)
ttk.Button(frame_btn, text="Salir", command=root.destroy).grid(row=0, column=3, padx=10)

# Resultados
ttk.Label(root, text="Resultados del análisis:", font=("Arial", 11, "bold")).pack(anchor='w', padx=20)
salida_texto = scrolledtext.ScrolledText(root, width=100, height=14, wrap=tk.WORD, state='disabled')
salida_texto.pack(padx=20, pady=5)
salida_texto.tag_config('titulo', font=('Arial', 10, 'bold'), foreground='blue')

root.mainloop()