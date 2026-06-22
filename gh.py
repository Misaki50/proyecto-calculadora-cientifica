try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Error: El módulo tkinter no está instalado.")
from math import *

# Función para agregar números y operadores
def agregar(valor):
    pantalla.insert(tk.END, valor)

# Función para calcular el resultado
def calcular():
    try:
        expresion = pantalla.get()
        # Diccionario de traducción: Símbolo visual -> Código Python
        reemplazos = {'×': '*', '÷': '/', '^': '**', 'π': 'pi', '√': 'sqrt'}
        for simbolo, valor_python in reemplazos.items():
            expresion = expresion.replace(simbolo, valor_python)
            
        if not expresion:
            return
        resultado = eval(expresion)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

# Función para limpiar pantalla
def limpiar():
    pantalla.delete(0, tk.END)

# Función para borrar el último carácter (Backspace)
def borrar_uno():
    texto_actual = pantalla.get()
    if texto_actual:
        # Lista de funciones que queremos borrar de un solo golpe
        # Incluimos el "(" porque así es como las insertas en tu programa
        funciones = ["sin", "cos", "tan", "log"]
        
        for f in funciones:
            if texto_actual.endswith(f):
                # Si termina en una función, borramos todos sus caracteres a la vez
                pantalla.delete(len(texto_actual) - len(f), tk.END)
                return

        pantalla.delete(len(texto_actual) - 1, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")
ventana.geometry("385x510")
ventana.configure(bg="#1c1c1c")  # Fondo oscuro

# Configuración de fuentes (Cámbialas aquí y se aplicarán a todo)
FUENTE_PANTALLA = ("Segoe UI", 24)
FUENTE_BOTONES = ("Segoe UI", 11, "bold")

# Paleta de colores modernos
COLOR_FONDO = "#1c1c1c"
COLOR_BOTON_NUM = "#333333"
COLOR_BOTON_FUNC = "#505050"
COLOR_BOTON_OP = "#ff9500"  # Naranja estilo iOS
COLOR_TEXTO = "#ffffff"

# Pantalla
pantalla = tk.Entry(ventana, font=FUENTE_PANTALLA, justify="right", fg=COLOR_TEXTO, 
                   bg=COLOR_FONDO, borderwidth=1, insertbackground="white")
pantalla.grid(row=0, column=0, columnspan=5, padx=20, pady=30, sticky="nsew")

# Botones
botones = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('×',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('+',3,3),
    ('0',4,0), ('0',4,1), ('.',4,2), ('÷',4,3),
]

# Botones con funciones (los que tienen paréntesis)
botones_funciones = [
    ('sin',2,4), ('cos',3,4), ('tan',4,4), ('log',5,4),
]

def crear_boton(texto, fila, columna, comando, color=COLOR_BOTON_NUM, cspan=1):
    return tk.Button(
        ventana, text=texto, width=5, height=2, font=FUENTE_BOTONES,
        bg=color, fg=COLOR_TEXTO, 
        borderwidth=0,              # Aumentamos el borde para dar volumen
        relief="flat",            # Efecto 3D de "botón hacia afuera"
        highlightthickness=2,       # Crea un borde extra que simula brillo
        highlightbackground="#ade8f4", # Color celeste brillante (muy Frutiger Aero)
        highlightcolor="#ffffff",    # Brillo blanco al enfocar
        activebackground="#ffffff", # El botón se ilumina al tocarlo
        command=comando
    ).grid(row=fila, column=columna, columnspan=cspan, padx=3, pady=3, sticky="nsew")

# Botones de control superiores
crear_boton("(", 1, 0, lambda: agregar("("), COLOR_BOTON_FUNC)
crear_boton(")", 1, 1, lambda: agregar(")"), COLOR_BOTON_FUNC)
crear_boton("C", 1, 2, limpiar, "#ff3b30")  # Rojo para borrar
crear_boton("⌫", 1, 3, borrar_uno, COLOR_BOTON_FUNC)
crear_boton("√", 1, 4, lambda: agregar("√("), COLOR_BOTON_OP)

# Dibujar botones numéricos y básicos
for texto, fila, columna in botones:
    # Si el botón es un operador, usamos el color naranja, si no, el gris
    if texto in ['×', '-', '+', '÷']:
        color = COLOR_BOTON_OP
    else:
        color = COLOR_BOTON_NUM
    crear_boton(texto, fila+1, columna, lambda t=texto: agregar(t), color)

for texto, fila, columna in botones_funciones:
    crear_boton(texto, fila, columna, lambda t=texto+'(': agregar(t), COLOR_BOTON_OP)

# Botones especiales
int_a = 6
crear_boton("^", int_a, 0, lambda: agregar("^"), COLOR_BOTON_FUNC)
crear_boton("π", int_a, 1, lambda: agregar("π"), COLOR_BOTON_FUNC)
crear_boton(".", int_a, 2, lambda: agregar("."), COLOR_BOTON_NUM)
crear_boton("=", int_a, 3, calcular, COLOR_BOTON_OP, cspan=2)


if __name__ == "__main__":
    ventana.mainloop()