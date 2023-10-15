from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    gst = fields.Char(
        string='GST'
    )
    pst = fields.Char(
        string='PST'
    )
