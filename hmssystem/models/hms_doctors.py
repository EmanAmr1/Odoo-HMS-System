from odoo import models, fields


class HMSdoctors(models.Model):
    _name = 'hms.doctors'
    _rec_name = 'FirstName'

    FirstName = fields.Char(string='First Name')
    LastName = fields.Char(string='Last Name')
    image = fields.Binary(string='Image')
