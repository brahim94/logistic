from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Purchaseorder(models.Model):
    _inherit = 'purchase.order'

    amount_by_group = fields.Binary(string="Tax amount by group", compute='_amount_by_group', help="type: [(name, amount, base, formated amount, formated base)]")

    def _amount_by_group(self):
        for order in self:
            currency = order.currency_id or order.company_id.currency_id
            fmt = partial(formatLang, self.with_context(lang=order.partner_id.lang).env, currency_obj=currency)
            res = {}
            for line in order.order_line:
                price_reduce = line.price_unit * (1.0 - line.discount / 100.0)
                taxes = line.tax_id.compute_all(price_reduce, quantity=line.product_uom_qty, product=line.product_id, partner=order.partner_shipping_id)['taxes']
                for tax in line.tax_id:
                    group = tax.tax_group_id
                    res.setdefault(group, {'amount': 0.0, 'base': 0.0})
                    for t in taxes:
                        if t['id'] == tax.id or t['id'] in tax.children_tax_ids.ids:
                            res[group]['amount'] += t['amount']
                            res[group]['base'] += t['base']
            res = sorted(res.items(), key=lambda l: l[0].sequence)
            order.amount_by_group = [(
                l[0].name, l[1]['amount'], l[1]['base'],
                fmt(l[1]['amount']), fmt(l[1]['base']),
                len(res),
            ) for l in res]

class PurchaseorderLine(models.Model):
    _inherit = 'purchase.order.line'

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
    price_unit_stored = fields.Float('Unit Price', related='price_unit', store=True, copy=True, required=False, digits='Product Price', default=0.0)


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
    def _onchange_quantity(self):
        self.ensure_one()
        super(PurchaseorderLine, self)._onchange_quantity()
        self.price_unit_pi = self.price_unit
        self.price_unit = self.price_unit * ((self.area) or 1)

        
    @api.onchange('price_unit_pi')
    def price_unit_pi_change(self):
        for line in self:
            if line.area_based:
               line.price_unit = line.price_unit_pi * (line.area or 1)
        

    def _prepare_account_move_line(self, move):
        res = super(PurchaseorderLine, self)._prepare_account_move_line(move)
        res['width'] = self.width
        res['area'] = self.area
        res['height'] = self.height
        return res
