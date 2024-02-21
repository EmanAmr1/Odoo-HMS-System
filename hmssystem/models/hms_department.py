from odoo import models, fields


class HMSdepartmnt(models.Model):
    _name = 'hms.department'
   # _rec_name = 'name'

    
    name = fields.Char(string='Department Name')
    capacity = fields.Integer(string='Capacity')
    is_opened = fields.Boolean(default=True)
    patients = fields.One2many('hms.system', 'department_id')

