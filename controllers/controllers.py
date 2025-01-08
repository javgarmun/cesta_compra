# -*- coding: utf-8 -*-
# from odoo import http


# class CestaCompra(http.Controller):
#     @http.route('/cesta_compra/cesta_compra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cesta_compra/cesta_compra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cesta_compra.listing', {
#             'root': '/cesta_compra/cesta_compra',
#             'objects': http.request.env['cesta_compra.cesta_compra'].search([]),
#         })

#     @http.route('/cesta_compra/cesta_compra/objects/<model("cesta_compra.cesta_compra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cesta_compra.object', {
#             'object': obj
#         })
