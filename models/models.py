# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__) 
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    rysunek = fields.Char('Rysunek', required = False)

#    mo_ids = fields.One2many('mrp.production',
#     _name = 'mrp_sale_worksheet.mrp_sale_worksheet'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
