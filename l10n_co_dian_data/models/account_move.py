# -*- coding: utf-8 -*-

from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    number_contract = fields.Char(string='Contract N°')
    date_contract = fields.Date(string='Contract Date')
    
