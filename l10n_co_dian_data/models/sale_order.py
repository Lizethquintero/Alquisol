# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    number_contract = fields.Char(string='Contract N°')
    date_contract = fields.Date(string='Contract Date')
    
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res['number_contract'] = self.number_contract or ''
        res['date_contract'] = self.date_contract or ''
        return res
    
    def _create_invoices(self, grouped=False, final=False):
        res = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final)
        for move in res:
            move._onchange_invoice_dates()
        return res
