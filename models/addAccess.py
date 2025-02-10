from odoo import models, api, fields, exceptions

class AddAccessFromProject(models.Model):
    _inherit = "project.project"
    
    def view_analyitc_account(self):
        """ Abre una cuenta analitica """
        self.ensure_one()
        
        if self.account_id:
            return {
                "name": "Cuenta Analítica",
                "type": "ir.actions.act_window",
                "res_model": "account.analytic.account",
                "view_mode": "form",
                "res_id": self.account_id.id,
                "target": "current",
            }
        else:
            return {'type': 'ir.actions.act_window_close'}
        