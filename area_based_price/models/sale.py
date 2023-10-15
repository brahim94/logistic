from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    height = fields.Float(
        default=0.0,
        digits='Product Unit of Measure'
    )
    width = fields.Float(
        default=0.0,
        digits='Product Unit of Measure'
    )
    area = fields.Float(
        compute='_compute_area'
    )
    area_based = fields.Boolean(
        related='product_id.area_based_price'
    )
    price_unit_pi = fields.Float(
        string='Price (PI²)',
    )
    price_unit_stored = fields.Float('Unit Price', related='price_unit', store=True, copy=True, required=False, digits='Product Price')

    @api.depends('height', 'width', 'product_uom')
    def _compute_area(self):
        for line in self:
            if line.height < 0 or line.width < 0:
                raise ValidationError(_("Negative value is not possible!"))
            if line.product_uom and line.product_uom.name in ['PI²', 'ft²']:
                line.area =  (line.height * line.width) / 144.0
            else:
                line.area = line.height * line.width



    @api.onchange('product_uom', 'product_uom_qty', 'area')
    def product_uom_change(self):
        self.ensure_one()
        super(SaleOrderLine, self).product_uom_change()
        self.price_unit = self.price_unit * ((self.area) or 1)
        self.price_unit_pi = self.product_id.list_price

    @api.onchange('price_unit_pi')
    def price_unit_pi_change(self):
        for line in self:
            if line.area_based:
               line.price_unit = line.price_unit_pi * (line.area or 1)



    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['width'] = self.width
        res['area'] = self.area
        res['height'] = self.height
        return res
