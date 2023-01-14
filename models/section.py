from odoo import models, fields, api


class Section(models.Model):
    _name = 'school.section'
    _description = 'section'

    name = fields.Char('Section Name', required=True)
    code = fields.Char('Code')