import tkinter as tk
from tkinter import ttk
import os

from clientes import crear_clientes
from abogados_casos import crear_abogados_casos
from procesal_documentos import crear_procesal_documentos
from agenda_facturacion import crear_agenda_facturacion


class LawFirmApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # ======================================================
        # CONFIGURACIÓN
        # ======================================================

        self.title("Justicia & Asociados")
        self.geometry("1000x700")

        # Tema inicial
        self.tema_actual = "claro"

        # ======================================================
        # FAVICON
        # ======================================================

        ruta_icono = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "imagenes",
            "favicon.ico"
        )

        print("========================================")
        print("COMPROBACIÓN DEL FAVICON")
        print("Ruta del icono:", ruta_icono)
        print("¿Existe el archivo?:", os.path.exists(ruta_icono))
        print("========================================")

        try:
            self.iconbitmap(ruta_icono)
            print("✅ Favicon cargado correctamente.")
        except Exception as e:
            print("❌ No se pudo cargar el favicon.")
            print("Error:", e)

        # ======================================================
        # ESTILOS
        # ======================================================

        self.estilo = ttk.Style()

        self.crear_estilos()

        # ======================================================
        # INTERFAZ
        # ======================================================

        self.crear_interfaz()

    # ==========================================================
    # CREAR ESTILOS
    # ==========================================================

    def crear_estilos(self):

        if self.tema_actual == "claro":

            fondo = "#F4F6F7"
            texto = "#1F2937"
            boton = "#E5E7EB"
            pestaña = "#FFFFFF"

        else:

            fondo = "#1F2937"
            texto = "#F9FAFB"
            boton = "#374151"
            pestaña = "#111827"

        self.configure(
            background=fondo
        )

        self.estilo.configure(
            "TFrame",
            background=fondo
        )

        self.estilo.configure(
            "TLabel",
            background=fondo,
            foreground=texto
        )

        self.estilo.configure(
            "TButton",
            background=boton,
            foreground=texto,
            padding=6
        )

        self.estilo.configure(
            "TNotebook",
            background=fondo
        )

        self.estilo.configure(
            "TNotebook.Tab",
            background=pestaña,
            foreground=texto,
            padding=(12, 6)
        )

    # ==========================================================
    # CAMBIAR TEMA
    # ==========================================================

    def cambiar_tema(self):

        if self.tema_actual == "claro":

            self.tema_actual = "oscuro"

            self.boton_tema.config(
                text="☀️ Tema claro"
            )

        else:

            self.tema_actual = "claro"

            self.boton_tema.config(
                text="🌙 Tema oscuro"
            )

        self.crear_estilos()

    # ==========================================================
    # INTERFAZ
    # ==========================================================

    def crear_interfaz(self):

        # ======================================================
        # ENCABEZADO
        # ======================================================

        encabezado = ttk.Frame(
            self
        )

        encabezado.pack(
            fill="x",
            padx=20,
            pady=10
        )

        titulo = ttk.Label(
            encabezado,
            text="JUSTICIA & ASOCIADOS",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            side="left",
            pady=10
        )

        # ======================================================
        # BOTÓN TEMA
        # ======================================================

        self.boton_tema = ttk.Button(
            encabezado,
            text="🌙 Tema oscuro",
            command=self.cambiar_tema
        )

        self.boton_tema.pack(
            side="right",
            padx=10
        )

        # ======================================================
        # SUBTÍTULO
        # ======================================================

        subtitulo = ttk.Label(
            self,
            text="Sistema de Gestión para Servicios Legales"
        )

        subtitulo.pack(
            pady=5
        )

        # ======================================================
        # PESTAÑAS
        # ======================================================

        pestañas = ttk.Notebook(
            self
        )

        pestañas.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ======================================================
        # CREAR PESTAÑAS
        # ======================================================

        clientes = ttk.Frame(
            pestañas
        )

        abogados = ttk.Frame(
            pestañas
        )

        procesal = ttk.Frame(
            pestañas
        )

        agenda = ttk.Frame(
            pestañas
        )

        # ======================================================
        # AGREGAR PESTAÑAS
        # ======================================================

        pestañas.add(
            clientes,
            text="👤 Clientes"
        )

        pestañas.add(
            abogados,
            text="⚖️ Abogados y Casos"
        )

        pestañas.add(
            procesal,
            text="📁 Procesal y Documentos"
        )

        pestañas.add(
            agenda,
            text="📅 Agenda y Facturación"
        )

        # ======================================================
        # CARGAR MÓDULOS
        # ======================================================

        crear_clientes(
            clientes
        )

        crear_abogados_casos(
            abogados
        )

        crear_procesal_documentos(
            procesal
        )

        crear_agenda_facturacion(
            agenda
        )


# ==========================================================
# EJECUTAR PROGRAMA
# ==========================================================

if __name__ == "__main__":

    app = LawFirmApp()

    app.mainloop()