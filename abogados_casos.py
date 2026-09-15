import tkinter as tk
from tkinter import ttk


def crear_abogados_casos(pestaña):

    # Crear subpestañas
    subpestañas = ttk.Notebook(pestaña)
    subpestañas.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    abogados = ttk.Frame(subpestañas)
    casos = ttk.Frame(subpestañas)

    subpestañas.add(abogados, text="Abogados")
    subpestañas.add(casos, text="Casos")

    # ==========================================
    # FORMULARIO DE ABOGADOS
    # ==========================================

    titulo_abogados = ttk.Label(
        abogados,
        text="Registro de Abogados",
        font=("Arial", 16, "bold")
    )

    titulo_abogados.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )

    ttk.Label(
        abogados,
        text="N.º de colegiatura:"
    ).grid(row=1, column=0, padx=10, pady=8)

    colegiatura = ttk.Entry(abogados)
    colegiatura.grid(row=1, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Nombres:"
    ).grid(row=2, column=0, padx=10, pady=8)

    nombres = ttk.Entry(abogados)
    nombres.grid(row=2, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Apellidos:"
    ).grid(row=3, column=0, padx=10, pady=8)

    apellidos = ttk.Entry(abogados)
    apellidos.grid(row=3, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Especialidad:"
    ).grid(row=4, column=0, padx=10, pady=8)

    especialidad = ttk.Combobox(
        abogados,
        values=[
            "Civil",
            "Penal",
            "Laboral",
            "Tributario",
            "Mercantil"
        ],
        state="readonly"
    )

    especialidad.grid(row=4, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Años de experiencia:"
    ).grid(row=5, column=0, padx=10, pady=8)

    experiencia = ttk.Entry(abogados)
    experiencia.grid(row=5, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Formación académica:"
    ).grid(row=6, column=0, padx=10, pady=8)

    formacion = ttk.Entry(abogados)
    formacion.grid(row=6, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Idiomas que domina:"
    ).grid(row=7, column=0, padx=10, pady=8)

    idiomas = ttk.Entry(abogados)
    idiomas.grid(row=7, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Tarifa por hora:"
    ).grid(row=8, column=0, padx=10, pady=8)

    tarifa = ttk.Entry(abogados)
    tarifa.grid(row=8, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Casos asignados:"
    ).grid(row=9, column=0, padx=10, pady=8)

    casos_asignados = ttk.Entry(abogados)
    casos_asignados.grid(row=9, column=1, padx=10, pady=8)

    ttk.Label(
        abogados,
        text="Disponibilidad:"
    ).grid(row=10, column=0, padx=10, pady=8)

    disponibilidad = ttk.Combobox(
        abogados,
        values=[
            "Disponible",
            "Ocupado",
            "No disponible"
        ],
        state="readonly"
    )

    disponibilidad.grid(row=10, column=1, padx=10, pady=8)

    def limpiar_abogados():
        colegiatura.delete(0, tk.END)
        nombres.delete(0, tk.END)
        apellidos.delete(0, tk.END)
        especialidad.set("")
        experiencia.delete(0, tk.END)
        formacion.delete(0, tk.END)
        idiomas.delete(0, tk.END)
        tarifa.delete(0, tk.END)
        casos_asignados.delete(0, tk.END)
        disponibilidad.set("")


    boton_abogados = ttk.Button(
    abogados,
    text="Limpiar",
    command=limpiar_abogados
)

    boton_abogados.grid(
    row=11,
    column=0,
    columnspan=2,
    pady=20
)

    # ==========================================
    # FORMULARIO DE CASOS
    # ==========================================

    titulo_casos = ttk.Label(
        casos,
        text="Registro de Casos Legales",
        font=("Arial", 16, "bold")
    )

    titulo_casos.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )

    ttk.Label(
        casos,
        text="Número único:"
    ).grid(row=1, column=0, padx=10, pady=8)

    numero = ttk.Entry(casos)
    numero.grid(row=1, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Título descriptivo:"
    ).grid(row=2, column=0, padx=10, pady=8)

    titulo = ttk.Entry(casos)
    titulo.grid(row=2, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Tipo de caso:"
    ).grid(row=3, column=0, padx=10, pady=8)

    tipo_caso = ttk.Entry(casos)
    tipo_caso.grid(row=3, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Rama del derecho:"
    ).grid(row=4, column=0, padx=10, pady=8)

    rama = ttk.Combobox(
        casos,
        values=[
            "Civil",
            "Penal",
            "Laboral",
            "Tributario",
            "Mercantil"
        ],
        state="readonly"
    )

    rama.grid(row=4, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Fecha de apertura:"
    ).grid(row=5, column=0, padx=10, pady=8)

    fecha_apertura = ttk.Entry(casos)
    fecha_apertura.grid(row=5, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Cliente:"
    ).grid(row=6, column=0, padx=10, pady=8)

    cliente = ttk.Entry(casos)
    cliente.grid(row=6, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Contraparte:"
    ).grid(row=7, column=0, padx=10, pady=8)

    contraparte = ttk.Entry(casos)
    contraparte.grid(row=7, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Juzgado o entidad:"
    ).grid(row=8, column=0, padx=10, pady=8)

    juzgado = ttk.Entry(casos)
    juzgado.grid(row=8, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="N.º expediente externo:"
    ).grid(row=9, column=0, padx=10, pady=8)

    expediente = ttk.Entry(casos)
    expediente.grid(row=9, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Abogado principal:"
    ).grid(row=10, column=0, padx=10, pady=8)

    abogado_principal = ttk.Entry(casos)
    abogado_principal.grid(row=10, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Abogados secundarios:"
    ).grid(row=11, column=0, padx=10, pady=8)

    abogados_secundarios = ttk.Entry(casos)
    abogados_secundarios.grid(row=11, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Estado actual:"
    ).grid(row=12, column=0, padx=10, pady=8)

    estado = ttk.Combobox(
        casos,
        values=[
            "Abierto",
            "En trámite",
            "Suspendido",
            "Cerrado"
        ],
        state="readonly"
    )

    estado.grid(row=12, column=1, padx=10, pady=8)

    ttk.Label(
        casos,
        text="Fecha estimada de conclusión:"
    ).grid(row=13, column=0, padx=10, pady=8)

    fecha_conclusion = ttk.Entry(casos)
    fecha_conclusion.grid(row=13, column=1, padx=10, pady=8)

    def limpiar_casos():
        numero.delete(0, tk.END)
        titulo.delete(0, tk.END)
        tipo_caso.delete(0, tk.END)
        rama.set("")
        fecha_apertura.delete(0, tk.END)
        cliente.delete(0, tk.END)
        contraparte.delete(0, tk.END)
        juzgado.delete(0, tk.END)
        expediente.delete(0, tk.END)
        abogado_principal.delete(0, tk.END)
        abogados_secundarios.delete(0, tk.END)
        estado.set("")
        fecha_conclusion.delete(0, tk.END)


    boton_casos = ttk.Button(
    casos,
    text="Limpiar",
    command=limpiar_casos
)

    boton_casos.grid(
    row=14,
    column=0,
    columnspan=2,
    pady=20
)