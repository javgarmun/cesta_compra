# -*- coding: utf-8 -*-
{
    'name': "Cesta de la Compra",

    'summary': """
        Gestiona cestas de la compra con productos, clientes y cálculos automáticos de totales en Odoo.
    """,

    'description': """
        Este módulo permite gestionar cestas de la compra asociadas a clientes dentro de Odoo. 
        Incluye funcionalidades para agregar productos o servicios a las cestas, calcular subtotales 
        automáticamente en las líneas de la cesta y gestionar el total global. 

        Características principales:
        - Asociación de cestas a clientes y productos.
        - Cálculo automático de subtotales y totales.
        - Vistas intuitivas para la gestión de clientes, cestas y productos.
    """,

    'author': "Javier García Muñoz",
    'website': "https://github.com/javgarmun/cesta_compra",

    'category': 'Sales',
    'version': '1.0',

    # Dependencias necesarias
    'depends': ['base'],

    # Archivos de datos cargados por el módulo
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # Archivos de demostración
    'demo': [
        'demo/demo.xml',
    ],
}
