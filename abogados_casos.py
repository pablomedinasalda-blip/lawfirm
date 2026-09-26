import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from conexion import conectar
from openpyxl import Workbook
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import mm
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import re
import os
from datetime import datetime


def crear_abogados_casos(pestaña):

    # ==========================================================
    # VARIABLES DE IMAGEN DEL ABOGADO
    # ==========================================================

    imagen_original_abogado = None
    imagen_tk_abogado = None
    ruta_imagen_abogado = ""

    # ==========================================================
    # CONEXIÓN A LA BASE DE DATOS
    # ==========================================================

    conexion = conectar()

    maquinas = []
    productos = []

    if conexion:

        try:
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM maquinas")
            maquinas = cursor.fetchall()

            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()

            cursor.close()

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"No se pudieron cargar los datos:\n{e}"
            )

        finally:
            conexion.close()

    # ==========================================================
    # SUBPESTAÑAS
    # ==========================================================

    subpestañas = ttk.Notebook(pestaña)

    subpestañas.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    abogados = ttk.Frame(subpestañas)
    casos = ttk.Frame(subpestañas)

    subpestañas.add(
        abogados,
        text="Abogados"
    )

    subpestañas.add(
        casos,
        text="Casos"
    )

    # ==========================================================
    # ======================= ABOGADOS =========================
    # ==========================================================

    ttk.Label(
        abogados,
        text="GESTIÓN DE ABOGADOS",
        font=("Arial", 16, "bold")
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        pady=10
    )

    campos_abogados = [
        ("Número de colegiatura", "colegiatura"),
        ("Nombres", "nombres"),
        ("Apellidos", "apellidos"),
        ("Especialidad", "especialidad"),
        ("Años de experiencia", "experiencia"),
        ("Formación académica", "formacion"),
        ("Idiomas", "idiomas"),
        ("Tarifa por hora", "tarifa"),
        ("Disponibilidad", "disponibilidad")
    ]

    entradas_abogados = {}

    for fila, (texto, clave) in enumerate(
        campos_abogados,
        start=1
    ):

        ttk.Label(
            abogados,
            text=texto
        ).grid(
            row=fila,
            column=0,
            padx=10,
            pady=6,
            sticky="w"
        )

        entrada = ttk.Entry(
            abogados,
            width=35
        )

        entrada.grid(
            row=fila,
            column=1,
            padx=10,
            pady=6
        )

        entradas_abogados[clave] = entrada

    # ==========================================================
    # MÁQUINAS
    # ==========================================================

    ttk.Label(
        abogados,
        text="Máquina relacionada"
    ).grid(
        row=10,
        column=0,
        padx=10,
        pady=6,
        sticky="w"
    )

    combo_maquina = ttk.Combobox(
        abogados,
        width=32,
        state="readonly"
    )

    combo_maquina.grid(
        row=10,
        column=1,
        padx=10,
        pady=6
    )

    combo_maquina["values"] = [
        str(m[0]) for m in maquinas
    ]

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    ttk.Label(
        abogados,
        text="Producto relacionado"
    ).grid(
        row=11,
        column=0,
        padx=10,
        pady=6,
        sticky="w"
    )

    combo_producto = ttk.Combobox(
        abogados,
        width=32,
        state="readonly"
    )

    combo_producto.grid(
        row=11,
        column=1,
        padx=10,
        pady=6
    )

    combo_producto["values"] = [
        str(p[0]) for p in productos
    ]

    # ==========================================================
    # IMAGEN DEL ABOGADO
    # ==========================================================

    ttk.Label(
        abogados,
        text="Imagen del abogado",
        font=("Arial", 11, "bold")
    ).grid(
        row=1,
        column=2,
        padx=20,
        pady=5
    )

    marco_imagen_abogado = ttk.Frame(
        abogados,
        width=180,
        height=150
    )

    marco_imagen_abogado.grid(
        row=2,
        column=2,
        rowspan=6,
        padx=20,
        pady=5
    )

    marco_imagen_abogado.grid_propagate(False)

    etiqueta_imagen_abogado = ttk.Label(
        marco_imagen_abogado,
        text="Sin imagen",
        anchor="center"
    )

    etiqueta_imagen_abogado.pack(
        fill="both",
        expand=True
    )

    # ==========================================================
    # SELECCIONAR IMAGEN
    # ==========================================================

    def seleccionar_imagen_abogado():

        nonlocal imagen_original_abogado
        nonlocal imagen_tk_abogado
        nonlocal ruta_imagen_abogado

        archivo = filedialog.askopenfilename(
            title="Seleccionar imagen del abogado",
            filetypes=[
                (
                    "Imágenes",
                    "*.jpg *.jpeg *.png *.gif"
                )
            ]
        )

        if not archivo:
            return

        extension = os.path.splitext(
            archivo
        )[1].lower()

        extensiones_permitidas = [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif"
        ]

        if extension not in extensiones_permitidas:

            messagebox.showwarning(
                "Imagen",
                "Solo se permiten imágenes JPG, PNG o GIF."
            )

            return

        tamaño = os.path.getsize(
            archivo
        )

        tamaño_maximo = 2 * 1024 * 1024

        if tamaño > tamaño_maximo:

            messagebox.showwarning(
                "Imagen",
                "La imagen no puede superar los 2 MB."
            )

            return

        try:

            imagen_original_abogado = Image.open(
                archivo
            )

            imagen_original_abogado.thumbnail(
                (160, 130)
            )

            imagen_tk_abogado = ImageTk.PhotoImage(
                imagen_original_abogado
            )

            etiqueta_imagen_abogado.config(
                image=imagen_tk_abogado,
                text=""
            )

            ruta_imagen_abogado = archivo

            messagebox.showinfo(
                "Imagen",
                "Imagen seleccionada correctamente."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"No se pudo abrir la imagen:\n{e}"
            )

    ttk.Button(
        abogados,
        text="🖼️ Seleccionar imagen",
        command=seleccionar_imagen_abogado
    ).grid(
        row=8,
        column=2,
        padx=20,
        pady=5
    )

    # ==========================================================
    # VALIDAR ABOGADO
    # ==========================================================

    def validar_abogado():

        datos = {
            clave: entrada.get().strip()
            for clave, entrada
            in entradas_abogados.items()
        }

        for campo, valor in datos.items():

            if not valor:

                messagebox.showwarning(
                    "Validación",
                    "Todos los campos del abogado son obligatorios."
                )

                return False

        if not datos["colegiatura"].isdigit():

            messagebox.showwarning(
                "Validación",
                "La colegiatura debe contener solamente números."
            )

            return False

        if len(datos["colegiatura"]) > 15:

            messagebox.showwarning(
                "Validación",
                "La colegiatura no puede superar 15 dígitos."
            )

            return False

        if not re.fullmatch(
            r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]{2,100}",
            datos["nombres"]
        ):

            messagebox.showwarning(
                "Validación",
                "Los nombres solo deben contener letras."
            )

            return False

        if not re.fullmatch(
            r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]{2,100}",
            datos["apellidos"]
        ):

            messagebox.showwarning(
                "Validación",
                "Los apellidos solo deben contener letras."
            )

            return False

        if len(datos["especialidad"]) < 2 or \
           len(datos["especialidad"]) > 100:

            messagebox.showwarning(
                "Validación",
                "La especialidad debe tener entre 2 y 100 caracteres."
            )

            return False

        if not datos["experiencia"].isdigit():

            messagebox.showwarning(
                "Validación",
                "Los años de experiencia deben ser numéricos."
            )

            return False

        if int(datos["experiencia"]) > 70:

            messagebox.showwarning(
                "Validación",
                "Los años de experiencia no pueden superar 70."
            )

            return False

        if len(datos["formacion"]) < 2 or \
           len(datos["formacion"]) > 150:

            messagebox.showwarning(
                "Validación",
                "La formación académica debe tener entre 2 y 150 caracteres."
            )

            return False

        if len(datos["idiomas"]) < 2 or \
           len(datos["idiomas"]) > 100:

            messagebox.showwarning(
                "Validación",
                "Los idiomas deben tener entre 2 y 100 caracteres."
            )

            return False

        try:

            tarifa = float(
                datos["tarifa"]
            )

            if tarifa < 0:

                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validación",
                "La tarifa debe ser un número válido."
            )

            return False

        if len(datos["disponibilidad"]) < 2 or \
           len(datos["disponibilidad"]) > 100:

            messagebox.showwarning(
                "Validación",
                "La disponibilidad debe tener entre 2 y 100 caracteres."
            )

            return False

        if not combo_maquina.get():

            messagebox.showwarning(
                "Validación",
                "Seleccione una máquina."
            )

            return False

        if not combo_producto.get():

            messagebox.showwarning(
                "Validación",
                "Seleccione un producto."
            )

            return False

        return True

    # ==========================================================
    # LIMPIAR ABOGADO
    # ==========================================================

    def limpiar_abogado():

        nonlocal imagen_original_abogado
        nonlocal imagen_tk_abogado
        nonlocal ruta_imagen_abogado

        for entrada in entradas_abogados.values():

            entrada.delete(
                0,
                tk.END
            )

        combo_maquina.set("")
        combo_producto.set("")

        imagen_original_abogado = None
        imagen_tk_abogado = None
        ruta_imagen_abogado = ""

        etiqueta_imagen_abogado.config(
            image="",
            text="Sin imagen"
        )

    # ==========================================================
    # EXPORTAR ABOGADO A EXCEL
    # ==========================================================

    def exportar_abogado_excel():

        if not validar_abogado():
            return

        archivo = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[
                ("Excel", "*.xlsx")
            ],
            title="Guardar abogado"
        )

        if not archivo:
            return

        datos = [
            entradas_abogados[campo].get().strip()
            for campo in entradas_abogados
        ]

        wb = Workbook()
        ws = wb.active

        ws.title = "Abogado"

        encabezados = [
            "Colegiatura",
            "Nombres",
            "Apellidos",
            "Especialidad",
            "Experiencia",
            "Formación",
            "Idiomas",
            "Tarifa",
            "Disponibilidad",
            "Máquina",
            "Producto"
        ]

        ws.append(encabezados)

        datos.append(combo_maquina.get())
        datos.append(combo_producto.get())

        ws.append(datos)

        wb.save(archivo)

        messagebox.showinfo(
            "Excel",
            "Archivo Excel creado correctamente."
        )

    # ==========================================================
    # EXPORTAR ABOGADO A PDF
    # ==========================================================

    def exportar_abogado_pdf():

        if not validar_abogado():
            return

        archivo = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[
                ("PDF", "*.pdf")
            ],
            title="Guardar abogado"
        )

        if not archivo:
            return

        datos = [
            entradas_abogados[campo].get().strip()
            for campo in entradas_abogados
        ]

        datos.append(combo_maquina.get())
        datos.append(combo_producto.get())

        encabezados = [
            "Colegiatura",
            "Nombres",
            "Apellidos",
            "Especialidad",
            "Experiencia",
            "Formación",
            "Idiomas",
            "Tarifa",
            "Disponibilidad",
            "Máquina",
            "Producto"
        ]

        documento = SimpleDocTemplate(
            archivo,
            pagesize=landscape(A4),
            rightMargin=10 * mm,
            leftMargin=10 * mm,
            topMargin=10 * mm,
            bottomMargin=10 * mm
        )

        tabla = Table(
            [encabezados, datos],
            repeatRows=1
        )

        tabla.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.grey
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.black
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    7
                )
            ])
        )

        documento.build([tabla])

        messagebox.showinfo(
            "PDF",
            "Archivo PDF creado correctamente."
        )

    # ==========================================================
    # BOTONES ABOGADOS
    # ==========================================================

    ttk.Button(
        abogados,
        text="Limpiar",
        command=limpiar_abogado
    ).grid(
        row=13,
        column=0,
        padx=10,
        pady=15
    )

    ttk.Button(
        abogados,
        text="📊 Excel",
        command=exportar_abogado_excel
    ).grid(
        row=13,
        column=1,
        padx=10,
        pady=15
    )

    ttk.Button(
        abogados,
        text="📄 PDF",
        command=exportar_abogado_pdf
    ).grid(
        row=13,
        column=2,
        padx=10,
        pady=15
    )

    # ==========================================================
    # ========================== CASOS =========================
    # ==========================================================

    ttk.Label(
        casos,
        text="GESTIÓN DE CASOS LEGALES",
        font=("Arial", 16, "bold")
    ).grid(
        row=0,
        column=0,
        columnspan=3,
        pady=10
    )

    campos_casos = [
        ("Número de caso", "numero"),
        ("Título descriptivo", "titulo"),
        ("Tipo de caso", "tipo"),
        ("Rama del derecho", "rama"),
        ("Cliente", "cliente"),
        ("Contraparte", "contraparte"),
        ("Juzgado o entidad", "juzgado"),
        ("Número de expediente externo", "expediente"),
        ("Abogado principal", "abogado"),
        ("Abogados secundarios", "secundarios"),
        ("Estado actual", "estado")
    ]

    entradas_casos = {}

    for fila, (texto, clave) in enumerate(
        campos_casos,
        start=1
    ):

        ttk.Label(
            casos,
            text=texto
        ).grid(
            row=fila,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        entrada = ttk.Entry(
            casos,
            width=40
        )

        entrada.grid(
            row=fila,
            column=1,
            padx=10,
            pady=5
        )

        entradas_casos[clave] = entrada

    # ==========================================================
    # FECHA DE APERTURA
    # ==========================================================

    ttk.Label(
        casos,
        text="Fecha de apertura"
    ).grid(
        row=5,
        column=2,
        padx=10,
        pady=5,
        sticky="w"
    )

    fecha = DateEntry(
        casos,
        width=18,
        date_pattern="dd/mm/yyyy"
    )

    fecha.grid(
        row=6,
        column=2,
        padx=10,
        pady=5
    )

    # ==========================================================
    # FECHA ESTIMADA DE CONCLUSIÓN
    # ==========================================================

    ttk.Label(
        casos,
        text="Fecha estimada de conclusión"
    ).grid(
        row=8,
        column=2,
        padx=10,
        pady=5,
        sticky="w"
    )

    conclusion = DateEntry(
        casos,
        width=18,
        date_pattern="dd/mm/yyyy"
    )

    conclusion.grid(
        row=9,
        column=2,
        padx=10,
        pady=5
    )

    # ==========================================================
    # FILTRO DE CASOS
    # ==========================================================

    ttk.Label(
        casos,
        text="Filtrar por estado"
    ).grid(
        row=12,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    combo_filtro_estado = ttk.Combobox(
        casos,
        state="readonly",
        values=[
            "Todos",
            "Abierto",
            "En proceso",
            "Cerrado",
            "Pendiente"
        ],
        width=25
    )

    combo_filtro_estado.set("Todos")

    combo_filtro_estado.grid(
        row=12,
        column=1,
        padx=10,
        pady=10
    )

    # ==========================================================
    # VALIDAR CASO
    # ==========================================================

    def validar_caso():

        datos = {
            clave: entrada.get().strip()
            for clave, entrada
            in entradas_casos.items()
        }

        for campo, valor in datos.items():

            if not valor:

                messagebox.showwarning(
                    "Validación",
                    "Todos los campos del caso son obligatorios."
                )

                return False

        if not datos["numero"].isdigit():

            messagebox.showwarning(
                "Validación",
                "El número de caso debe ser numérico."
            )

            return False

        if len(datos["numero"]) > 20:

            messagebox.showwarning(
                "Validación",
                "El número de caso no puede superar 20 dígitos."
            )

            return False

        if len(datos["titulo"]) < 3 or \
           len(datos["titulo"]) > 150:

            messagebox.showwarning(
                "Validación",
                "El título debe tener entre 3 y 150 caracteres."
            )

            return False

        if len(datos["tipo"]) < 2 or \
           len(datos["tipo"]) > 100:

            messagebox.showwarning(
                "Validación",
                "El tipo de caso no es válido."
            )

            return False

        if len(datos["rama"]) < 2 or \
           len(datos["rama"]) > 100:

            messagebox.showwarning(
                "Validación",
                "La rama del derecho no es válida."
            )

            return False

        if len(datos["cliente"]) < 2 or \
           len(datos["cliente"]) > 100:

            messagebox.showwarning(
                "Validación",
                "El cliente no es válido."
            )

            return False

        if len(datos["contraparte"]) < 2 or \
           len(datos["contraparte"]) > 100:

            messagebox.showwarning(
                "Validación",
                "La contraparte no es válida."
            )

            return False

        if len(datos["juzgado"]) < 2 or \
           len(datos["juzgado"]) > 150:

            messagebox.showwarning(
                "Validación",
                "El juzgado o entidad no es válido."
            )

            return False

        if len(datos["expediente"]) < 2 or \
           len(datos["expediente"]) > 100:

            messagebox.showwarning(
                "Validación",
                "El expediente no es válido."
            )

            return False

        if len(datos["abogado"]) < 2 or \
           len(datos["abogado"]) > 100:

            messagebox.showwarning(
                "Validación",
                "El abogado principal no es válido."
            )

            return False

        if len(datos["secundarios"]) < 2 or \
           len(datos["secundarios"]) > 150:

            messagebox.showwarning(
                "Validación",
                "Los abogados secundarios no son válidos."
            )

            return False

        if len(datos["estado"]) < 2 or \
           len(datos["estado"]) > 100:

            messagebox.showwarning(
                "Validación",
                "El estado no es válido."
            )

            return False

        try:

            datetime.strptime(
                fecha.get(),
                "%d/%m/%Y"
            )

            datetime.strptime(
                conclusion.get(),
                "%d/%m/%Y"
            )

        except ValueError:

            messagebox.showwarning(
                "Validación",
                "Las fechas no son válidas."
            )

            return False

        return True

    # ==========================================================
    # LIMPIAR CASO
    # ==========================================================

    def limpiar_caso():

        for entrada in entradas_casos.values():

            entrada.delete(
                0,
                tk.END
            )

        fecha.set_date(
            datetime.now()
        )

        conclusion.set_date(
            datetime.now()
        )

        combo_filtro_estado.set(
            "Todos"
        )

    # ==========================================================
    # FILTRO
    # ==========================================================

    def aplicar_filtro():

        estado_filtro = combo_filtro_estado.get().strip()

        if estado_filtro == "Todos":
            return True

        estado_actual = entradas_casos[
            "estado"
        ].get().strip()

        if estado_actual != estado_filtro:

            messagebox.showinfo(
                "Filtro",
                "El estado actual del caso no coincide con el filtro."
            )

            return False

        return True

    # ==========================================================
    # EXPORTAR CASO A EXCEL
    # ==========================================================

    def exportar_caso_excel():

        if not validar_caso():
            return

        if not aplicar_filtro():
            return

        archivo = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[
                ("Excel", "*.xlsx")
            ],
            title="Guardar caso"
        )

        if not archivo:
            return

        datos = [
            entradas_casos[campo].get().strip()
            for campo in entradas_casos
        ]

        datos.insert(
            4,
            fecha.get()
        )

        datos.append(
            conclusion.get()
        )

        encabezados = [
            "Número",
            "Título",
            "Tipo",
            "Rama",
            "Fecha apertura",
            "Cliente",
            "Contraparte",
            "Juzgado",
            "Expediente",
            "Abogado",
            "Secundarios",
            "Estado",
            "Conclusión"
        ]

        wb = Workbook()

        ws = wb.active

        ws.title = "Caso"

        ws.append(encabezados)
        ws.append(datos)

        wb.save(archivo)

        messagebox.showinfo(
            "Excel",
            "Archivo Excel creado correctamente."
        )

    # ==========================================================
    # EXPORTAR CASO A PDF
    # ==========================================================

    def exportar_caso_pdf():

        if not validar_caso():
            return

        if not aplicar_filtro():
            return

        archivo = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[
                ("PDF", "*.pdf")
            ],
            title="Guardar caso"
        )

        if not archivo:
            return

        datos = [
            entradas_casos[campo].get().strip()
            for campo in entradas_casos
        ]

        datos.insert(
            4,
            fecha.get()
        )

        datos.append(
            conclusion.get()
        )

        encabezados = [
            "Número",
            "Título",
            "Tipo",
            "Rama",
            "Fecha apertura",
            "Cliente",
            "Contraparte",
            "Juzgado",
            "Expediente",
            "Abogado",
            "Secundarios",
            "Estado",
            "Conclusión"
        ]

        documento = SimpleDocTemplate(
            archivo,
            pagesize=landscape(A4),
            rightMargin=8 * mm,
            leftMargin=8 * mm,
            topMargin=10 * mm,
            bottomMargin=10 * mm
        )

        tabla = Table(
            [encabezados, datos],
            repeatRows=1
        )

        tabla.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.grey
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.black
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    6
                )
            ])
        )

        documento.build([tabla])

        messagebox.showinfo(
            "PDF",
            "Archivo PDF creado correctamente."
        )

    # ==========================================================
    # BOTONES DE CASOS
    # ==========================================================

    ttk.Button(
        casos,
        text="Limpiar",
        command=limpiar_caso
    ).grid(
        row=13,
        column=0,
        padx=10,
        pady=15
    )

    ttk.Button(
        casos,
        text="📊 Excel",
        command=exportar_caso_excel
    ).grid(
        row=13,
        column=1,
        padx=10,
        pady=15
    )

    ttk.Button(
        casos,
        text="📄 PDF",
        command=exportar_caso_pdf
    ).grid(
        row=13,
        column=2,
        padx=10,
        pady=15
    )