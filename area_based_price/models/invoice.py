from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    height = fields.Float(
        default=0.0,
        digits='Product Unit of Measure'
    )
    width = fields.Float(
        default=0.0,
        digits='Product Unit of Measure'
    )
    area = fields.Float(
        compute='_compute_area',
        store=True
    )
    area_based = fields.Boolean(
        related='product_id.area_based_price'
    )

    @api.depends('height', 'width')
    def _compute_area(self):
        for line in self:
            if line.height < 0 or line.width < 0:
                raise ValidationError(_("Negative value is not possible!"))
            line.area = line.height * line.width

    @api.onchange('product_uom_id', 'area')
    def _onchange_uom_id(self):
        self.ensure_one()
        super(AccountMoveLine, self)._onchange_uom_id()
        self.price_unit = self.price_unit * ((self.height * self.width) or 1)
