# -*- coding: utf-8 -*-
{
    'name': "Cesta de la Compra",  # Nombre del módulo en Odoo

    'summary': """
        Gestiona cestas de la compra con productos, clientes y cálculos automáticos de totales en Odoo.
    """,  # Breve resumen de las funcionalidades del módulo

    'description': """
        Este módulo permite gestionar cestas de la compra asociadas a clientes dentro de Odoo. 
        Incluye funcionalidades para agregar productos o servicios a las cestas, calcular subtotales 
        automáticamente en las líneas de la cesta y gestionar el total global. 

        Características principales:
        - Asociación de cestas a clientes y productos.
        - Cálculo automático de subtotales y totales.
        - Vistas intuitivas para la gestión de clientes, cestas y productos.
    """,  # Descripción detallada del módulo y sus características

    'author': "Javier García Muñoz",
    'website': "https://github.com/javgarmun/cesta_compra",  # Enlace al repositorio del proyecto

    'category': 'Sales',  # Categoría dentro de Odoo (en este caso, relacionado con ventas)
    'version': '1.0',  # Versión del módulo

    # Dependencias necesarias para que el módulo funcione correctamente
    'depends': ['base'],

    # Archivos de datos cargados por el módulo
    'data': [
        'views/views.xml',  # Archivo de vistas principales
        'views/cliente_view.xml',  # Vistas relacionadas con clientes
        'views/producto_view.xml',  # Vistas relacionadas con productos
        'views/cesta_view.xml',  # Vistas relacionadas con las cestas
    ],
    # Archivos de demostración
    'demo': [
        'demo/cliente_demo.xml',  # Datos de ejemplo para los clientes
        'demo/producto_demo.xml',  # Datos de ejemplo para los productos
    ],
}
