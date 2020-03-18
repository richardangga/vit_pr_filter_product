# -*- coding: utf-8 -*-
from odoo import http

# class VitPrFilterProduct(http.Controller):
#     @http.route('/vit_pr_filter_product/vit_pr_filter_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_pr_filter_product/vit_pr_filter_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_pr_filter_product.listing', {
#             'root': '/vit_pr_filter_product/vit_pr_filter_product',
#             'objects': http.request.env['vit_pr_filter_product.vit_pr_filter_product'].search([]),
#         })

#     @http.route('/vit_pr_filter_product/vit_pr_filter_product/objects/<model("vit_pr_filter_product.vit_pr_filter_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_pr_filter_product.object', {
#             'object': obj
#         })