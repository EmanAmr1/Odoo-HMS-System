from odoo import models, fields,api
from odoo.exceptions import ValidationError

class HMSInherit(models.Model):
    _inherit = 'res.partner'

    
    vat = fields.Char(string='Tax ID', required=True, readonly=False)
    related_patient_id = fields.Many2one('hms.system', string='Related Patient')


    @api.constrains('email', 'related_patient_id')
    def _check_unique_email_per_patient(self):
        for record in self:
            if record.email and record.related_patient_id:
                existing_customer = self.env['res.partner'].search([
                    ('email', '=', record.email),
                    ('related_patient_id', '!=', record.related_patient_id.id)
                ])
                if existing_customer:
                    raise ValidationError('Email address must be unique per patient.')
                


   