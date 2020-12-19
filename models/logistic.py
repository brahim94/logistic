# -*- coding: utf-8 -*-

from odoo import models, fields, api


class logistic(models.Model):

    _name = 'logistic'

    booking = fields.Char('Booking N°')
    shipement = fields.Char('Shipment N°')
    vendor = fields.Many2one('res.partner', string='vendor')
    shipper = fields.Many2one('res.partner', string='Shipper')
    consignee = fields.Many2one('res.partner', string='Consignee')
    byer = fields.Many2one('res.partner', string='Byer')
    notify_one = fields.Many2one('res.partner', string='Notify1')
    notify_two = fields.Many2one('res.partner', string='Notify2')
    notify_three = fields.Many2one('res.partner', string='Notify3')
    export_freight_forwarder = fields.Many2one('res.partner', string='Export Freight forwarder')
    export_freight_broker = fields.Many2one('res.partner', string='Export Customs broker')
    shipping_line = fields.Many2one('res.partner', string='Shipping line')
    vessel_trailer_flight = fields.Many2one('vissel.trailer', 'Vessel /Trailer/ Flight')
    etd = fields.Date("ETD")
    eta = fields.Date("ETA")
    import_customs_broker = fields.Many2one('res.partner', string='Import Customs broker')
    import_freight_forwarder = fields.Many2one('res.partner', string='Import Freight forwarder')
    country_id = fields.Many2one('res.country', string='Country Origin')
    city_id = fields.Text(string='Pick up Adress')
    provenance_id = fields.Many2one('res.country', string='Country Provenance')
    pol_id = fields.Many2one("logistic.city", string='POL')
    tol = fields.Many2one("logistic.city",'TOL')
    pod_id = fields.Many2one("logistic.city", string='POD')
    tod_id = fields.Many2one("logistic.city",'TOD')
    delivery_id = fields.Text(string='Delivery Adress')
    marks = fields.Text('Marks')
    stc = fields.Text('STC')
    #stc = fields.Text('STC')
    cargo_release = fields.Selection([
            ('released', 'Released'),
            ('against_documents', 'Against Documents'),
            ], string='Cargo Release')
    cargo_release_conditions = fields.Text('Cargo Release Conditions')
    other_instrcutions = fields.Text('Other Instrcutions')
    m_h = fields.Selection([
            ('m', 'M'),
            ('m_h', 'M/H'),
            ], string='M/H')
    number_of_original_bl = fields.Integer('Number of Original BL')
    




class logistic_city(models.Model):

    _name = 'logistic.city'
    _order = 'code'

    country_id = fields.Many2one('res.country', string='Country')
    name  = fields.Char('name')
    code = fields.Char(string='city Code', help='The city code.')


class VisselFlight(models.Model):

    _name = 'vissel.trailer'

    name  = fields.Char('name: ')

    # @api.onchange('state_id')
    # def _onchange_state(self):
    #     if self.state_id.country_id:
    #         self.country_id = self.state_id.country_id



    