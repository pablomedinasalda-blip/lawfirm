import tkinter as tk
from tkinter import ttk


def crear_agenda_facturacion(pestaña):

    # Crear subpestañas
    subpestañas = ttk.Notebook(pestaña)
    subpestañas.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    audiencias = ttk.Frame(subpestañas)
    facturacion = ttk.Frame(subpestañas)

    subpestañas.add(
        audiencias,
        text="Audiencias y citas"
    )

    subpestañas.add(
        facturacion,
        text="Facturación"
    )

    # ==========================================
    # AUDIENCIAS Y CITAS
    # ==========================================

    titulo_audiencias = ttk.Label(
        audiencias,
        text="Registro de Audiencias y Citas",
        font=("Arial", 16, "bold")
    )

    titulo_audiencias.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )

    ttk.Label(
        audiencias,
        text="Código:"
    ).grid(row=1, column=0, padx=10, pady=8)

    codigo = ttk.Entry(audiencias)
    codigo.grid(row=1, column=1, padx=10, pady=8)

    ttk.Label(
        audiencias,
        text="Tipo:"
    ).grid(row=2, column=0, padx=10, pady=8)

    tipo = ttk.Combobox(
        audiencias,
        values=[
            "Audiencia",
            "Cita"
        ],
        state="readonly"
    )

    tipo.grid(row=2, column=1, padx=10, pady=8)

    ttk.Label(
        audiencias,
        text="Caso relacionado:"
    ).grid(row=3, column=0, padx=10, pady=8)

    caso = ttk.Entry(audiencias)
    caso.grid(row=3, column=1, padx=10, pady=8)

    ttk.Label(
        audiencias,
        text="Fecha y hora:"
    ).grid(row=4, column=0, padx=10, pady=8)

    fecha_hora = ttk.Entry(audiencias)
    fecha_hora.grid(row=4, column=1, padx=10, pady=8)

    ttk.Label(
        audiencias,
        text="Duración:"
    ).grid(row=5, column=0, padx=10, pady=8)

    duracion = ttk.Entry(audiencias)
    duracion.grid(row=5, column=1, padx=10, pady=8)

    ttk.Label(
        audiencias,
        text="Lugar:"
    ).grid(row=6, column=0, padx=10, pady=8)

    lugar = ttk.Entry(audiencias)
    lugar.grid(row=6, column=1, padx=10, pady=8)

    ttk.Label(
        audiencias,
        text="Participantes internos:"
    ).grid(row=7, column=0, padx=10, pady=8)

    participantes_internos = ttk.Entry(audiencias)
    participantes_internos.grid(
        row=7,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        audiencias,
        text="Participantes externos:"
    ).grid(row=8, column=0, padx=10, pady=8)

    participantes_externos = ttk.Entry(audiencias)
    participantes_externos.grid(
        row=8,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        audiencias,
        text="Propósito:"
    ).grid(row=9, column=0, padx=10, pady=8)

    proposito = ttk.Entry(audiencias)
    proposito.grid(row=9, column=1, padx=10, pady=8)

    ttk.Label(
        audiencias,
        text="Materiales:"
    ).grid(row=10, column=0, padx=10, pady=8)

    materiales = ttk.Entry(audiencias)
    materiales.grid(row=10, column=1, padx=10, pady=8)

    ttk.Label(
        audiencias,
        text="Resultado esperado / real:"
    ).grid(row=11, column=0, padx=10, pady=8)

    resultado = ttk.Entry(audiencias)
    resultado.grid(row=11, column=1, padx=10, pady=8)

    boton_audiencias = ttk.Button(
        audiencias,
        text="Limpiar"
    )

    boton_audiencias.grid(
        row=12,
        column=0,
        columnspan=2,
        pady=20
    )

    # ==========================================
    # FACTURACIÓN
    # ==========================================

    titulo_facturacion = ttk.Label(
        facturacion,
        text="Registro de Facturación",
        font=("Arial", 16, "bold")
    )

    titulo_facturacion.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )

    ttk.Label(
        facturacion,
        text="Número de factura:"
    ).grid(row=1, column=0, padx=10, pady=8)

    numero_factura = ttk.Entry(facturacion)
    numero_factura.grid(
        row=1,
        column=1,
        padx=10,
        pady=8
    )

    ttk.Label(
        facturacion,
        text="Fecha:"
    ).grid(row=2, column=0, padx=10, pady=8)

    fecha = ttk.Entry(facturacion)
    fecha.grid(row=2, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Cliente:"
    ).grid(row=3, column=0, padx=10, pady=8)

    cliente = ttk.Entry(facturacion)
    cliente.grid(row=3, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Periodo:"
    ).grid(row=4, column=0, padx=10, pady=8)

    periodo = ttk.Entry(facturacion)
    periodo.grid(row=4, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Casos:"
    ).grid(row=5, column=0, padx=10, pady=8)

    casos = ttk.Entry(facturacion)
    casos.grid(row=5, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Detalle de servicios:"
    ).grid(row=6, column=0, padx=10, pady=8)

    detalle = ttk.Entry(facturacion)
    detalle.grid(row=6, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Horas por abogado:"
    ).grid(row=7, column=0, padx=10, pady=8)

    horas = ttk.Entry(facturacion)
    horas.grid(row=7, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Tarifa:"
    ).grid(row=8, column=0, padx=10, pady=8)

    tarifa = ttk.Entry(facturacion)
    tarifa.grid(row=8, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Gastos:"
    ).grid(row=9, column=0, padx=10, pady=8)

    gastos = ttk.Entry(facturacion)
    gastos.grid(row=9, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Subtotal:"
    ).grid(row=10, column=0, padx=10, pady=8)

    subtotal = ttk.Entry(facturacion)
    subtotal.grid(row=10, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Impuestos:"
    ).grid(row=11, column=0, padx=10, pady=8)

    impuestos = ttk.Entry(facturacion)
    impuestos.grid(row=11, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Total:"
    ).grid(row=12, column=0, padx=10, pady=8)

    total = ttk.Entry(facturacion)
    total.grid(row=12, column=1, padx=10, pady=8)

    ttk.Label(
        facturacion,
        text="Estado de pago:"
    ).grid(row=13, column=0, padx=10, pady=8)

    estado_pago = ttk.Combobox(
        facturacion,
        values=[
            "Pendiente",
            "Pagada",
            "Vencida"
        ],
        state="readonly"
    )

    estado_pago.grid(
        row=13,
        column=1,
        padx=10,
        pady=8
    )

    boton_facturacion = ttk.Button(
        facturacion,
        text="Limpiar"
    )

    boton_facturacion.grid(
        row=14,
        column=0,
        columnspan=2,
        pady=20
    )