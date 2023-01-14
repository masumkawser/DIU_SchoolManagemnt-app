from odoo import models, fields, api


class Course(models.Model):
    _name = 'school.course'
    _description = 'course'

    name = fields.Char('Course Name', required=True)
    code = fields.Char('Code')