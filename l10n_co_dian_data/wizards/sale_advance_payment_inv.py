from odoo import api, fields, models

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    journal_id = fields.Many2one('account.journal', string='Journal', domain=lambda self: [('type','=','sale'), ('company_id', '=', self.env.company.id)])

    def create_invoices(self):
        if self.journal_id:
            self = self.with_context(default_journal_id=self.journal_id.id)
        return super(SaleAdvancePaymentInv, self).create_invoices()
    
