# Sistema de Gestión para Servicios Legales — Justicia & Asociados

## Descripción

Sistema de gestión desarrollado en Python para administrar información relacionada con una firma de servicios legales.

El proyecto cuenta con una interfaz gráfica desarrollada con Tkinter y conexión a una base de datos MySQL.

## Tecnologías utilizadas

* Python
* Tkinter
* MySQL
* mysql.connector
* Pillow
* Tkcalendar
* OpenPyXL
* ReportLab

## Módulos

El proyecto está organizado en diferentes módulos:

* `main.py`
* `clientes.py`
* `abogados_casos.py`
* `procesal_documentos.py`
* `agenda_facturacion.py`
* `conexion.py`

## Funcionalidades

El sistema incluye:

* Gestión de clientes.
* Gestión de abogados y casos.
* Gestión procesal y documentos.
* Agenda y facturación.
* Operaciones CRUD.
* Conexión con MySQL.
* Procedimientos almacenados.
* Validación de datos.
* Selección de fechas mediante calendario.
* Gestión de imágenes.
* Exportación a Excel.
* Exportación a PDF.
* Filtros.
* Tema claro y oscuro.
* Favicon e iconografía.

## Base de datos

El sistema utiliza la base de datos MySQL:

`TextilPro`

La conexión se realiza mediante el archivo:

`conexion.py`

## Instalación

1. Instalar Python.
2. Instalar las dependencias necesarias.
3. Configurar MySQL.
4. Crear o restaurar la base de datos `TextilPro`.
5. Verificar los datos de conexión en `conexion.py`.
6. Ejecutar:

```bash
python main.py
```

## Dependencias

Las principales librerías utilizadas son:

```bash
pip install mysql-connector-python
pip install openpyxl
pip install reportlab
pip install tkcalendar
pip install Pillow
```

## Autores

Proyecto académico — Justicia & Asociados.
