# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductRequestLine(models.Model):
    _inherit = 'vit.product.request'
    
    product_id = fields.Many2many(comodel_name='project.project', string='Project')
    
    # @api.onchange('product_id')
    # def _onchange_product_id(self):
    #     if self.product_id:
    #         self.product_uom_id = self.product_id.uom_id.id
    #         self.unit_price = self.product_id.standard_price
    #         self.name = self.product_id.name
    #     else:
    #         self.product_uom_id = None
    #         self.unit_price = None
