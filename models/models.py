# -*- coding: utf-8 -*-
from odoo import models, fields, api


# CLASE CLIENTE: Representa la información de los clientes que realizan pedidos.
class Cliente(models.Model):
    _name = 'cesta_compra.cliente'
    _description = 'Cliente'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos')
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Char(string='Dirección')
    numero_cestas = fields.Char(string='Número de Cestas',
                                compute='_compute_numero_cestas')  # Cálculo automático del número de cestas que ha realizado el cliente
    gasto_total = fields.Float(string='Gasto Total',
                               compute='_compute_gasto_total')  # Cálculo automático del gasto total del cliente
    activo = fields.Boolean(string='Activo', default=True)  # Campo booleano para indicar si el cliente está activo
    country_id = fields.Many2one('res.country', string='País', required=True)  # Relación con el país del cliente
    cesta_ids = fields.One2many('cesta_compra.cesta', 'cliente_id',
                                string='Cestas')  # Relación uno a muchos con las cestas de compra del cliente

    # Método para calcular el número de cestas del cliente
    @api.depends('cesta_ids')
    def _compute_numero_cestas(self):
        for cliente in self:
            cliente.numero_cestas = len(cliente.cesta_ids)

    # Método para calcular el gasto total del cliente
    @api.depends('cesta_ids.total_cesta')
    def _compute_gasto_total(self):
        for cliente in self:
            cliente.gasto_total = sum(cesta.total_cesta for cesta in cliente.cesta_ids)


# CLASE PRODUCTO: Representa los productos disponibles para la compra.
class Producto(models.Model):
    _name = 'cesta_compra.producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio', required=True)


# CLASE CESTA: Representa una cesta de compra, que agrupa los productos seleccionados por un cliente.
class Cesta(models.Model):
    _name = 'cesta_compra.cesta'
    _description = 'Cesta de la Compra'

    name = fields.Char(string='Referencia', readonly=True)  # Referencia única de la cesta, solo lectura
    fecha_pedido = fields.Datetime(string='Fecha de Pedido', default=fields.Datetime.now)
    estado = fields.Selection([
        ('en_proceso', 'En proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='en_proceso')  # El estado por defecto es 'en_proceso'
    cliente_id = fields.Many2one('cesta_compra.cliente', string='Cliente', required=True)
    linea_pedido_ids = fields.One2many('cesta_compra.linea_pedido', 'pedido_id',
                                       string='Líneas de Pedido')  # Relación uno a muchos con las líneas de pedido
    cantidad_productos = fields.Integer(string='Número de Productos', compute='_compute_cantidad_productos',
                                        store=True)

    descuento = fields.Float(string='Descuento (%)', default=0.0,
                             help="Descuento aplicable sobre el total de la cesta")  # Descuento en porcentaje sobre el total de la cesta
    total_cesta = fields.Float(string='Total', compute='_compute_total_cesta',
                               store=True)  # Total de la cesta, incluyendo el descuento

    # Método para calcular la cantidad total de productos en la cesta
    @api.depends('linea_pedido_ids.cantidad')
    def _compute_cantidad_productos(self):
        for cesta in self:
            cesta.cantidad_productos = sum(line.cantidad for line in cesta.linea_pedido_ids)

    # Método para calcular el total de la cesta, aplicando el descuento sobre el total sin descuento
    @api.depends('linea_pedido_ids.subtotal', 'descuento')
    def _compute_total_cesta(self):
        for cesta in self:
            total_sin_descuento = sum(line.subtotal for line in cesta.linea_pedido_ids)
            descuento = (cesta.descuento / 100) * total_sin_descuento  # Cálculo del descuento
            cesta.total_cesta = total_sin_descuento - descuento  # Total tras aplicar el descuento

    # Método para generar la referencia única de la cesta al crearla
    @api.model
    def create(self, vals):
        max_number = self.search([], order='name desc', limit=1).name  # Busca la última cesta creada
        if max_number:
            next_number = int(max_number.split('-')[1]) + 1  # Incrementa el número de la cesta
            vals['name'] = f'C-{next_number:03d}'
        else:
            vals['name'] = 'C-001'  # Si no hay cestas, comienza con la referencia C-001

        return super(Cesta, self).create(vals)


# CLASE LINEAPEDIDO: Representa cada producto agregado a una cesta de compra.
class LineaPedido(models.Model):
    _name = 'cesta_compra.linea_pedido'
    _description = 'Línea de Pedido'

    cantidad = fields.Integer(string='Cantidad', required=True, default=1)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)
    pedido_id = fields.Many2one('cesta_compra.cesta', string='Cesta', required=True)
    producto_id = fields.Many2one('cesta_compra.producto', string='Producto', required=True)

    # Método para calcular el subtotal de la línea de pedido (cantidad * precio del producto)
    @api.depends('cantidad', 'producto_id.precio')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.cantidad * line.producto_id.precio

    # Método para actualizar el subtotal cuando cambian la cantidad o el producto seleccionado
    @api.onchange('cantidad', 'producto_id')
    def _onchange_cantidad_precio(self):
        if self.producto_id:
            self.subtotal = self.cantidad * self.producto_id.precio  # Recalcula el subtotal
