from odoo import models, fields


class HMSPatientLog(models.Model):
    _name = 'hms.patient.log'

    patient_id = fields.Many2one('hms.system')
    description = fields.Text(string='Description')
