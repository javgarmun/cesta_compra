# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'cesta_compra.cliente'
    _description = 'Cliente'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Char(string='Dirección')
    country_id = fields.Many2one('res.country', string='País', required=True)
    cesta_ids = fields.One2many('cesta_compra.cesta', 'cliente_id', string='Cestas')

class Cesta(models.Model):
    _name = 'cesta_compra.cesta'
    _description = 'Cesta de la Compra'

    name = fields.Char(string='Referencia', required=True, readonly=True)
    fecha_pedido = fields.Datetime(string='Fecha de Pedido', default=fields.Datetime.now)
    estado = fields.Selection([
        ('en_proceso', 'En proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ], string='Estado', default='en_proceso')
    cliente_id = fields.Many2one('cesta_compra.cliente', string='Cliente', required=True)
    detalle_pedido_ids = fields.One2many('cesta_compra.detalle_pedido', 'pedido_id', string='Detalles de Pedido')
    total_cesta = fields.Float(string='Total de la Cesta', compute='_compute_total_cesta', store=True)

    @api.depends('detalle_pedido_ids.subtotal')
    def _compute_total_cesta(self):
        for cesta in self:
            cesta.total_cesta = sum(line.subtotal for line in cesta.detalle_pedido_ids)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cesta_compra.sequence') or _('New')
        return super(Cesta, self).create(vals)


class DetallePedido(models.Model):
    _name = 'cesta_compra.detalle_pedido'
    _description = 'Detalle de Pedido'

    cantidad = fields.Float(string='Cantidad', required=True, default=1.0)
    precio_unidad = fields.Float(string='Precio Unitario', required=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)
    pedido_id = fields.Many2one('cesta_compra.cesta', string='Cesta', required=True)
    producto_id = fields.Many2one('cesta_compra.producto', string='Producto', required=True)

    @api.depends('cantidad', 'precio_unidad')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.cantidad * line.precio_unidad

    @api.onchange('cantidad', 'precio_unidad')
    def _onchange_cantidad_precio(self):
        self.subtotal = self.cantidad * self.precio_unidad


class Producto(models.Model):
    _name = 'cesta_compra.producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio', required=True)