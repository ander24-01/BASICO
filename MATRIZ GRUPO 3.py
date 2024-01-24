import numpy as np
import tkinter as tk
import pandas as pd

# Definir las propiedades de los materiales
materiales = {
    "Fibra de carbono": {
        "vf": 0.6,  # Fracción volumétrica de las fibras
        "vm": 0.4,  # Fracción volumétrica de la matriz
        "Ef": 230e9,  # Módulo de elasticidad de las fibras (Pa)
        "Em": 3.5e9,  # Módulo de elasticidad de la matriz (Pa)
        "nuf": 0.2,  # Coeficiente de Poisson de las fibras
        "num": 0.35,  # Coeficiente de Poisson de la matriz
    },
    "Fibra de vidrio": {
        "vf": 0.5,  # Fracción volumétrica de las fibras
        "vm": 0.5,  # Fracción volumétrica de la matriz
        "Ef": 72e9,  # Módulo de elasticidad de las fibras (Pa)
        "Em": 3.5e9,  # Módulo de elasticidad de la matriz (Pa)
        "nuf": 0.28,  # Coeficiente de Poisson de las fibras
        "num": 0.35,  # Coeficiente de Poisson de la matriz
    },
    "Fibra de sílice": {
        "vf": 0.4,  # Fracción volumétrica de las fibras
        "vm": 0.6,  # Fracción volumétrica de la matriz
        "Ef": 80e9,  # Módulo de elasticidad de las fibras (Pa)
        "Em": 3.5e9,  # Módulo de elasticidad de la matriz (Pa)
        "nuf": 0.17,  # Coeficiente de Poisson de las fibras
        "num": 0.35,  # Coeficiente de Poisson de la matriz
    },
    "Fibra de cuarzo": {
        "vf": 0.6,  # Fracción volumétrica de las fibras
        "vm": 0.4,  # Fracción volumétrica de la matriz
        "Ef": 85e9,  # Módulo de elasticidad de las fibras (Pa)
        "Em": 3.5e9,  # Módulo de elasticidad de la matriz (Pa)
        "nuf": 0.14,  # Coeficiente de Poisson de las fibras
        "num": 0.35,  # Coeficiente de Poisson de la matriz
    },
    "Fibra de kevlar": {
        "vf": 0.5,  # Fracción volumétrica de las fibras
        "vm": 0.5,  # Fracción volumétrica de la matriz
        "Ef": 131e9,  # Módulo de elasticidad de las fibras (Pa)
        "Em": 3.5e9,  # Módulo de elasticidad de la matriz (Pa)
        "nuf": 0.34,  # Coeficiente de Poisson de las fibras
        "num": 0.35,  # Coeficiente de Poisson de la matriz
    },
}

# Definir la función que calcula la matriz D de un material compuesto
def calcular_matriz_D(nombre_material):
    # Obtener el material correspondiente
    material = materiales[nombre_material]

    # Calcular el módulo de elasticidad longitudinal del material compuesto
    El = material["vf"] * material["Ef"] + material["vm"] * material["Em"]

    # Calcular el módulo de elasticidad transversal del material compuesto
    Et = 1 / (material["vf"] / material["Ef"] + material["vm"] / material["Em"])

    # Calcular el coeficiente de Poisson del material compuesto
    nu = material["vf"] * material["nuf"] + material["vm"] * material["num"]

    # Calcular el módulo de corte del material compuesto
    G = 1 / (1 / (material["vf"] * material["Ef"]) + 1 / (material["vm"] * material["Em"]))

    # Construir la matriz D del material compuesto
    D = np.array([
        [El / (1 - nu ** 2), nu * El / (1 - nu ** 2), 0],
        [nu * El / (1 - nu ** 2), El / (1 - nu ** 2), 0],
        [0, 0, G]
    ])

    # Devolver la matriz D
    return D

# Definir la función que se ejecuta al pulsar el botón
def mostrar_propiedades():
    # Obtener el nombre del material seleccionado
    nombre_material = opcion.get()

    # Calcular la matriz D del material seleccionado
    D = calcular_matriz_D(nombre_material)

    # Obtener el material correspondiente
    material = materiales[nombre_material]

    # Mostrar las propiedades y la matriz D del material en la etiqueta
    etiqueta.config(text=f"Las propiedades de {nombre_material} son:\n"
                         f"vf = {material['vf']}\n"
                         f"vm = {material['vm']}\n"
                         f"Ef = {material['Ef']}\n"
                         f"Em = {material['Em']}\n"
                         f"nuf = {material['nuf']}\n"
                         f"num = {material['num']}\n"
                         f"La matriz D es:\n{D}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Elegir material")

# Crear el marco para los elementos
marco = tk.Frame(ventana)
marco.pack()

# Crear la variable para almacenar la opción elegida
opcion = tk.StringVar()

# Crear los botones de radio para elegir el tipo de material
radio1 = tk.Radiobutton(marco, text="Fibra de carbono", variable=opcion, value="Fibra de carbono")
radio1.grid(row=0, column=0)
radio2 = tk.Radiobutton(marco, text="Fibra de vidrio", variable=opcion, value="Fibra de vidrio")
radio2.grid(row=0, column=1)
radio3 = tk.Radiobutton(marco, text="Fibra de sílice", variable=opcion, value="Fibra de sílice")
radio3.grid(row=0, column=2)
radio4 = tk.Radiobutton(marco, text="Fibra de cuarzo", variable=opcion, value="Fibra de cuarzo")
radio4.grid(row=1, column=0)
radio5 = tk.Radiobutton(marco, text="Fibra de kevlar", variable=opcion, value="Fibra de kevlar")
radio5.grid(row=1, column=1)

# Crear el botón para mostrar las propiedades
boton = tk.Button(marco, text="Mostrar", command=mostrar_propiedades)
boton.grid(row=2, column=0, columnspan=3)

# Crear la etiqueta para mostrar las propiedades
etiqueta = tk.Label(marco, text="")
etiqueta.grid(row=3, column=0, columnspan=3)

# Iniciar el bucle principal de la ventana
ventana.mainloop()

