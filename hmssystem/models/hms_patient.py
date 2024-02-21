from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError
import re

class HMSsystem(models.Model):
    _name = 'hms.system'
    _rec_name = 'FirstName'

    FirstName = fields.Char(required=True, string='First Name')

    LastName = fields.Char(required=True, string='Last Name')

    BirthDate = fields.Date(string='Birth Date')

    History = fields.Html()

    CRratio = fields.Float(string='CR Ratio')

    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    ], string='Blood Type')

    PCR = fields.Boolean(string='PCR')

    Image = fields.Binary()

    Address = fields.Text()

    Age = fields.Integer(compute='calculate_age')

    department_id = fields.Many2one('hms.department')

    doctor_ids = fields.Many2many('hms.doctors', readonly=True)

    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined', string='State')

    department_capacity = fields.Integer(related='department_id.capacity')

    state_log = fields.One2many('hms.patient.log', 'patient_id')

    Email = fields.Char()

    # _sql_constraints = [
    #   ('email_unique', 'UNIQUE(Email)', 'Email must be unique!'),
    #  ('email_format', 'CHECK (Email ~* \'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$\')', 'Invalid email format!')
    # ]

    

    @api.onchange('state')
    def log_state(self):
        for rec in self:
            rec.env['hms.patient.log'].create({
                'description': 'state changed to %s' % rec.state,
                'patient_id': rec.id
            })

    @api.onchange('Age')
    def _onchange_age(self):
        if self.Age < 30 and self.Age !=0:
            self.PCR = True
            return {
                'warning': {
                    'title': "PCR Checked",
                    'message': "PCR field has been automatically checked."
                }
            }

    @api.depends('BirthDate')
    def calculate_age(self):
        for rec in self:
            if rec.BirthDate:
             today = date.today()
             rec.Age = today.year - rec.BirthDate.year - ((today.month, today.day) < ( rec.BirthDate.month, rec.BirthDate.day))
            else:
               rec.Age = 0


    @api.constrains('Email')
    def _check_unique_email(self):
        for rec in self:
            if rec.Email:
                existing_patient = self.env['hms.system'].search([('Email', '=', rec.Email)])
                if len(existing_patient) > 1:
                    raise ValidationError('Email address must be unique.')


    @api.constrains('Email')
    def _check_valid_email(self):
        for rec in self:
            if rec.Email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", rec.Email):
                    raise ValidationError('Invalid email address.')
                


              