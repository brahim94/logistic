# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class PaymentPayment(models.Model):

    _name = 'payment.type'
    _rec_name = 'billing_section'

    billing_section = fields.Selection([
            ('all_services', 'All services'),
            ('services_except', 'All services Except'),
            ('only_services', 'Only theses services'),
            ], string='Billing section')
    service_except_id = fields.Many2many('service.type', 'service_payment_rel', 'payment_id', 'service_typ_id', string='Services')
    service_only_id = fields.Many2many('service.type', 'service_pay_rel', 'pay_id', 'service_t_id', string='Services')
    billing_party = fields.Many2one('res.partner', 'Billing party')
    payment_moment = fields.Many2many('payment.moment', 'moment_payment_rel', 'pay_id', 'moment_id', string='Moment of payment')
    payment_type = fields.Selection([
            ('cash', 'Cash'),
            ('cheque', 'Cheque'),
            ('ldc', 'LDC'),
            ('bank_tr', 'Bank transfer'),
            ('online', 'Online'),
            ], setting='Payment Type', default='cash')
    cheque_type = fields.Selection([
            ('certified', 'Certified'),
            ('not_certified', 'Not certified'),
            ], setting='Cheque', default='certified')
    ldc_type = fields.Selection([
            ('certified', 'Certified'),
            ('not_certified', 'Not certified'),
            ], setting='LDC', default='certified')
    total_payment_cap = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Total CPayment Cap', default='euro')
    total_spayment_cap = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Total SPayment Cap', default='euro')
    service_type_payment = fields.Many2many('service.type', 'service_payment_rel', 'pay_id', 'serv_t_id', string='Service type')
    payment_cap_payment = fields.Many2many('payment.cap', 'payment_payment_rel', 'py_id', 'paymnt_ty_id', string='payment cap')
    sector_type_payment = fields.Many2many('sector.type', 'sector_payment_rel', 'use_id', 'sector_t_id', string='Sector')
    discount_payment = fields.Many2many('service.type.discount', 'dscoun_paym_rel', 'paym_id', 'discoun_ty_id', string='Discount')
    

class PaymentMoment(models.Model):

    _name = 'payment.moment'

    number_of_days = fields.Integer('nombre de jours')
    before_starting = fields.Boolean('Before starting')
    before_str = fields.Char('Prc')
    after_starting = fields.Boolean('After starting')
    after_str = fields.Char('Prc')
    after_finishing = fields.Boolean('After finishing')
    after_finish = fields.Char('Prc')
    after_billing = fields.Boolean('After billing')
    after_bili = fields.Char('Prc')


class BankBank(models.Model):

     _name = 'bank.bank'
     _rec_name = 'account_number'

     account_number = fields.Char('Account N°')
     bank_detail = fields.Text('Bank details')
     iban = fields.Char('IBAN')
     code_swift = fields.Integer('Code swift')



#     name = fields.Char('Payment methode name')
#     payment_type = fields.Selection([
#             ('cash', 'Cash'),
#             ('cheque', 'Cheque'),
#             ('ldc', 'LDC'),
#             ('bank_tr', 'Bank transfer'),
#             ('online', 'Online'),
#             ], setting='Payment Type', default='cash')
#     cheque_type = fields.Selection([
#             ('certified', 'Certified'),
#             ('not_certified', 'Not certified'),
#             ], setting='Cheque', default='certified')
#     ldc_type = fields.Selection([
#             ('certified', 'Certified'),
#             ('not_certified', 'Not certified'),
#             ], setting='LDC', default='certified')