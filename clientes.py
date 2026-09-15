import tkinter as tk
from tkinter import ttk


def crear_clientes(pestaña):

    titulo = ttk.Label(
        pestaña,
        text="Registro de Clientes",
        font=("Arial", 16, "bold")
    )

    titulo.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )

    ttk.Label(
        pestaña,
        text="Código único:"
    ).grid(row=1, column=0, padx=10, pady=10)

    codigo = ttk.Entry(pestaña)
    codigo.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Tipo:"
    ).grid(row=2, column=0, padx=10, pady=10)

    tipo = ttk.Combobox(
        pestaña,
        values=["Persona natural", "Empresa"]
    )

    tipo.grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Nombres / Razón social:"
    ).grid(row=3, column=0, padx=10, pady=10)

    nombres = ttk.Entry(pestaña)
    nombres.grid(row=3, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Documento / RUC:"
    ).grid(row=4, column=0, padx=10, pady=10)

    documento = ttk.Entry(pestaña)
    documento.grid(row=4, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Dirección:"
    ).grid(row=5, column=0, padx=10, pady=10)

    direccion = ttk.Entry(pestaña)
    direccion.grid(row=5, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Teléfono:"
    ).grid(row=6, column=0, padx=10, pady=10)

    telefono = ttk.Entry(pestaña)
    telefono.grid(row=6, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Correo electrónico:"
    ).grid(row=7, column=0, padx=10, pady=10)

    correo = ttk.Entry(pestaña)
    correo.grid(row=7, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Fecha de primer contacto:"
    ).grid(row=8, column=0, padx=10, pady=10)

    fecha = ttk.Entry(pestaña)
    fecha.grid(row=8, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Referido por:"
    ).grid(row=9, column=0, padx=10, pady=10)

    referido = ttk.Entry(pestaña)
    referido.grid(row=9, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Sector de actividad:"
    ).grid(row=10, column=0, padx=10, pady=10)

    sector = ttk.Entry(pestaña)
    sector.grid(row=10, column=1, padx=10, pady=10)

    ttk.Label(
        pestaña,
        text="Clasificación interna:"
    ).grid(row=11, column=0, padx=10, pady=10)

    clasificacion = ttk.Entry(pestaña)
    clasificacion.grid(row=11, column=1, padx=10, pady=10)

    def limpiar_clientes():
        codigo.delete(0, tk.END)
    tipo.set("")
    nombres.delete(0, tk.END)
    documento.delete(0, tk.END)
    direccion.delete(0, tk.END)
    telefono.delete(0, tk.END)
    correo.delete(0, tk.END)
    fecha.delete(0, tk.END)
    referido.delete(0, tk.END)
    sector.delete(0, tk.END)
    clasificacion.delete(0, tk.END)


    boton = ttk.Button(
    pestaña,
    text="Limpiar",
    command=limpiar_clientes
)

    boton.grid(
    row=12,
    column=0,
    columnspan=2,
    pady=20
)