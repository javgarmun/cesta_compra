# -*- coding: utf-8 -*-
from odoo import models, fields, api


# CLASE PRODUCTO: Representa los productos disponibles para la compra.
class Producto(models.Model):
    _name = 'cesta_compra.producto'
    _description = 'Producto'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio', required=True)


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
