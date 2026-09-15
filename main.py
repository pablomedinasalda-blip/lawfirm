import tkinter as tk
from tkinter import ttk
from clientes import crear_clientes
from abogados_casos import crear_abogados_casos
from procesal_documentos import crear_procesal_documentos
from agenda_facturacion import crear_agenda_facturacion

class LawFirmApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Justicia & Asociados")
        self.geometry("1000x700")

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = ttk.Label(
            self,
            text="JUSTICIA & ASOCIADOS",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=20)

        subtitulo = ttk.Label(
            self,
            text="Sistema de Gestión para Servicios Legales"
        )

        subtitulo.pack(pady=5)

        pestañas = ttk.Notebook(self)

        pestañas.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        clientes = ttk.Frame(pestañas)
        abogados = ttk.Frame(pestañas)
        procesal = ttk.Frame(pestañas)
        agenda = ttk.Frame(pestañas)

        pestañas.add(clientes, text="Clientes")
        pestañas.add(abogados, text="Abogados y Casos")
        pestañas.add(procesal, text="Procesal y Documentos")
        pestañas.add(agenda, text="Agenda y Facturación")

        crear_clientes(clientes)
        crear_abogados_casos(abogados)
        crear_procesal_documentos(procesal)
        crear_agenda_facturacion(agenda)

if __name__ == "__main__":
    app = LawFirmApp()
    app.mainloop()