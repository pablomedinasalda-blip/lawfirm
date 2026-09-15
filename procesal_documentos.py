import tkinter as tk
from tkinter import ttk


def crear_procesal_documentos(pestaña):

    # Crear subpestañas
    subpestañas = ttk.Notebook(pestaña)
    subpestañas.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    actuaciones = ttk.Frame(subpestañas)
    documentos = ttk.Frame(subpestañas)

    subpestañas.add(
        actuaciones,
        text="Actuaciones procesales"
    )

    subpestañas.add(
        documentos,
        text="Documentos legales"
    )

    # ==========================================
    # ACTUACIONES PROCESALES
    # ==========================================

    titulo_actuaciones = ttk.Label(
        actuaciones,
        text="Actuaciones Procesales",
        font=("Arial", 16, "bold")
    )

    titulo_actuaciones.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )

    ttk.Label(
        actuaciones,
        text="Código:"
    ).grid(row=1, column=0, padx=10, pady=8)

    codigo = ttk.Entry(actuaciones)
    codigo.grid(row=1, column=1, padx=10, pady=8)

    ttk.Label(
        actuaciones,
        text="Caso relacionado:"
    ).grid(row=2, column=0, padx=10, pady=8)

    caso = ttk.Entry(actuaciones)
    caso.grid(row=2, column=1, padx=10, pady=8)

    ttk.Label(
        actuaciones,
        text="Tipo de actuación:"
    ).grid(row=3, column=0, padx=10, pady=8)

    tipo = ttk.Combobox(
        actuaciones,
        values=[
            "Demanda",
            "Contestación",
            "Recurso",
            "Audiencia"
        ],
        state="readonly"
    )

    tipo.grid(row=3, column=1, padx=10, pady=8)

    ttk.Label(
        actuaciones,
        text="Fecha y hora:"
    ).grid(row=4, column=0, padx=10, pady=8)

    fecha_hora = ttk.Entry(actuaciones)
    fecha_hora.grid(row=4, column=1, padx=10, pady=8)

    ttk.Label(
        actuaciones,
        text="Lugar:"
    ).grid(row=5, column=0, padx=10, pady=8)

    lugar = ttk.Entry(actuaciones)
    lugar.grid(row=5, column=1, padx=10, pady=8)

    ttk.Label(
        actuaciones,
        text="Descripción:"
    ).grid(row=6, column=0, padx=10, pady=8)

    descripcion = ttk.Entry(actuaciones)
    descripcion.grid(row=6, column=1, padx=10, pady=8)

    ttk.Label(
        actuaciones,
        text="Documentos presentados:"
    ).grid(row=7, column=0, padx=10, pady=8)

    documentos_presentados = ttk.Entry(actuaciones)
    documentos_presentados.grid(
        row=7,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        actuaciones,
        text="Resultado obtenido:"
    ).grid(row=8, column=0, padx=10, pady=8)

    resultado = ttk.Entry(actuaciones)
    resultado.grid(row=8, column=1, padx=10, pady=8)

    ttk.Label(
        actuaciones,
        text="Siguiente paso recomendado:"
    ).grid(row=9, column=0, padx=10, pady=8)

    siguiente_paso = ttk.Entry(actuaciones)
    siguiente_paso.grid(
        row=9,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        actuaciones,
        text="Fecha límite:"
    ).grid(row=10, column=0, padx=10, pady=8)

    fecha_limite = ttk.Entry(actuaciones)
    fecha_limite.grid(
        row=10,
        column=1,
        padx=10,
        pady=8
    )

    def limpiar_actuaciones():
        codigo.delete(0, tk.END)
        caso.delete(0, tk.END)
        tipo.set("")
        fecha_hora.delete(0, tk.END)
        lugar.delete(0, tk.END)
        descripcion.delete(0, tk.END)
        documentos_presentados.delete(0, tk.END)
        resultado.delete(0, tk.END)
        siguiente_paso.delete(0, tk.END)
        fecha_limite.delete(0, tk.END)


    boton_actuaciones = ttk.Button(
    actuaciones,
    text="Limpiar",
    command=limpiar_actuaciones
)

    boton_actuaciones.grid(
    row=11,
    column=0,
    columnspan=2,
    pady=20
)

    # ==========================================
    # DOCUMENTOS LEGALES
    # ==========================================

    titulo_documentos = ttk.Label(
        documentos,
        text="Documentos Legales",
        font=("Arial", 16, "bold")
    )

    titulo_documentos.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )

    ttk.Label(
        documentos,
        text="Código único:"
    ).grid(row=1, column=0, padx=10, pady=8)

    codigo_documento = ttk.Entry(documentos)
    codigo_documento.grid(
        row=1,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Tipo:"
    ).grid(row=2, column=0, padx=10, pady=8)

    tipo_documento = ttk.Combobox(
        documentos,
        values=[
            "Contrato",
            "Demanda",
            "Informe",
            "Dictamen"
        ],
        state="readonly"
    )

    tipo_documento.grid(
        row=2,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Título:"
    ).grid(row=3, column=0, padx=10, pady=8)

    titulo = ttk.Entry(documentos)
    titulo.grid(
        row=3,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Autor:"
    ).grid(row=4, column=0, padx=10, pady=8)

    autor = ttk.Entry(documentos)
    autor.grid(
        row=4,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Destinatario:"
    ).grid(row=5, column=0, padx=10, pady=8)

    destinatario = ttk.Entry(documentos)
    destinatario.grid(
        row=5,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Fecha de creación:"
    ).grid(row=6, column=0, padx=10, pady=8)

    fecha_creacion = ttk.Entry(documentos)
    fecha_creacion.grid(
        row=6,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Versión:"
    ).grid(row=7, column=0, padx=10, pady=8)

    version = ttk.Entry(documentos)
    version.grid(
        row=7,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Estado:"
    ).grid(row=8, column=0, padx=10, pady=8)

    estado = ttk.Combobox(
        documentos,
        values=[
            "Borrador",
            "Revisión",
            "Final"
        ],
        state="readonly"
    )

    estado.grid(
        row=8,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Contenido / archivo asociado:"
    ).grid(row=9, column=0, padx=10, pady=8)

    contenido = ttk.Entry(documentos)
    contenido.grid(
        row=9,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        documentos,
        text="Nivel de confidencialidad:"
    ).grid(row=10, column=0, padx=10, pady=8)

    confidencialidad = ttk.Combobox(
        documentos,
        values=[
            "Bajo",
            "Medio",
            "Alto",
            "Restringido"
        ],
        state="readonly"
    )

    confidencialidad.grid(
        row=10,
        column=1,
        padx=10,
        pady=8
    )

    def limpiar_documentos():
        codigo_documento.delete(0, tk.END)
        tipo_documento.set("")
        titulo.delete(0, tk.END)
        autor.delete(0, tk.END)
        destinatario.delete(0, tk.END)
        fecha_creacion.delete(0, tk.END)
        version.delete(0, tk.END)
        estado.set("")
        contenido.delete(0, tk.END)
        confidencialidad.set("")


    boton_documentos = ttk.Button(
    documentos,
    text="Limpiar",
    command=limpiar_documentos
)

    boton_documentos.grid(
    row=11,
    column=0,
    columnspan=2,
    pady=20
)