# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class directoryorde(models.Model):

    _name = 'directory.type'

    name = fields.Char(string='Draft N°')
    name_id = fields.Char(string='PCF N°')
    account_number = fields.Char('Account Number', readonly="1")
    type_file = fields.Selection([
            ('draft', 'Draft'),
            ('definitive', 'Definitive'),
            ], setting='Type File', required=True)
    how = fields.Selection([
            ('blank_form', 'Formulaire vièrge'),
            ('other_file', 'From another file'),
            ], setting='HOW', default='blank_form')
    blank_form = fields.Text('Formulaire vierge')
    pcf_number = fields.Many2one('directory.type', string='PCF Number?')
    m_s = fields.Selection([
            ('master', 'Master file (M)'),
            ('subfile', 'Subfile (S)'),
            ], setting='M/S', default='master')
    pcf_n = fields.Char('PCF N°?')
    link = fields.Selection([
            ('yes', 'Yes'),
            ('no', 'No'),
            ], setting='Link', default='no')
    at_glance = fields.Text('At a glance')    
    name_principal = fields.Char(string='Principal')
    company_detail = fields.Many2one('res.partner', string='Principal')
    rc = fields.Char(string='RC')
    ice = fields.Char(string='ICE')
    pic = fields.Char(string='PIC')
    pic_detail = fields.Char(string='PIC details')
    sector_id = fields.Many2one('sector.type', string='Sector')
    reference_id = fields.Many2one('reference.type', string='Reference')
    year_frequency = fields.Selection([
            ('dk', 'DK'),
            ('one', 'VIII: 1'),
            ('three', 'VII: 1<....=<3'),
            ('teen', 'VI: 3<....=<10'),
            ('twenty', 'V: 10<.....=<20'),
            ('therten', 'IV: 20<.......=<50'),
            ('hundred', 'III: 50<........=<100'),
            ('twohundred', 'II: 100<......=<200'),
            ('more', 'I: >200'),
            ], setting='Frequency per year', default='dk')
    customer_ref = fields.Char(string="Customer's Ref")
    purchase_order = fields.Char(string="Purchase Order (PO)")
    sales_order = fields.Char(string='Sales Order (SO)')
    shipment_reference = fields.Char(string='Shipment Ref')
    vendor_reference = fields.Char(string='Vendor Ref')
    consign_reference = fields.Char(string='Consignee Ref')
    ticket_n = fields.Char(string='Ticket N°')
    rma_n = fields.Char(string='RMA N°')
    beyer_ref = fields.Char(string='Byer Ref')
    ref_two = fields.Char(string='Ref2')
    ref_thre = fields.Char(string='Ref3')
    ref_four = fields.Char(string='Ref4')
    ref_five = fields.Char(string='Ref5')
    ref_six = fields.Char(string='Ref6')
    ref_id = fields.Many2one('directory.type', string="Ref ID")
    direction = fields.Selection([
            ('export', 'Export (E)'),
            ('import', 'Import (I)'),
            ('local', 'Local (L)'),
            ('off', 'OffShore (Off)'),
            ('offon', 'OffOnShore (OffOn)'),
            ('offoncl', 'OffOnShore Cleared (OffOnCl)'),
            ], setting='Direction', default='export')
    transport_mode = fields.Selection([
            ('as', 'AS'),
            ('pessenger_luggage', 'Passenger luggage'),
            ('postal_parcel', 'Postal Parcel'),
            ('ltl', 'LTL'),
            ('lcl', 'LCL'),
            ('fcl', 'FCL'),
            ('reefer', 'Reefer'),
            ('ftl', 'FTL'),
            ('bb_lolo', 'BB (Lolo)'),
            ('bb_roro', 'BB (Roro)'),
            ('bulk', 'Bulk'),
            ('bulk_liquid', 'Bulk liquid'),
            ('vessel', 'Chartered vessel'),
            ('aircraft', 'Chartered Aircraft'),
            ], setting='Mode of Transport', default='as')


    packaging = fields.Boolean(string='Packaging')
    stuffing = fields.Boolean(string='Stuffing')
    lsd = fields.Boolean(string='LSD')
    loading_on_track = fields.Boolean(string='Loading On Truck')
    export_formalities = fields.Boolean(string='Export Formalities')
    pre_carriage = fields.Boolean(string='Pre-Carriage')
    export_customs = fields.Boolean(string='Export Customs')
    entry_formalities = fields.Boolean(string='Terminal Entry Formalities')
    on_terminal = fields.Boolean(string='Unloading On Terminal')
    export_agency = fields.Boolean(string='Export Agency')
    loading_main_transport = fields.Boolean(string='Loading on Main Transport')
    main_transport = fields.Boolean(string='Main Transport')
    from_main_transport = fields.Boolean(string='Unloading From Main Transport')
    import_agency = fields.Boolean(string='Import Agency')
    import_formalities = fields.Boolean(string='Import Formalities')
    import_customs = fields.Boolean(string='Import Customs')
    loading_from_term = fields.Boolean(string='Loading From Terminal')
    terminal_exit = fields.Boolean(string='Terminal Exit Formalities')
    delivery = fields.Boolean(string='Delivery')
    ulonading_site = fields.Boolean(string='Unloading on site')
    unlashing = fields.Boolean(string='Unlashing')
    stripping = fields.Boolean(string='Stripping')
    unpackaging = fields.Boolean(string='Unpackaging')
    other = fields.Boolean(string='Other Customs Formalities')
    other_requests = fields.Boolean(string='Other Requests')
    insurance_int = fields.Boolean(string='Insurance Int')
    insurance_dom = fields.Boolean(string='Insurance Dom')
    domestic_customs = fields.Boolean(string='Domestic Customs')
    trailer_traction = fields.Boolean(string='Trailer Traction')
    storage = fields.Boolean(string='Storage')
    lifting = fields.Boolean(string='Lifting')
    domestic = fields.Boolean(string='Domestic Haulage')
    renting = fields.Boolean(string='Renting')
    consulting = fields.Boolean(string='Consulting')
    road_surevy = fields.Boolean(string='Road survey')
    studies = fields.Boolean(string='Studies')
    survey_report = fields.Boolean(string='Survey Report')
    escort = fields.Boolean(string='Escort')
    civil_work = fields.Boolean(string='Civil Work')
    documents = fields.Boolean(string='Documents')
    
    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New') and vals.get('name_id', ('New')) == ('New'):
                if vals.get('type_file') == 'draft':
                        vals['name'] = self.env['ir.sequence'].next_by_code('draft.order') or ('New')
                        vals['name_id'] = self.env['ir.sequence'].next_by_code('definitive.order') or ('New')
        if vals.get('name', ('New')) == ('New') and vals.get('type_file') == 'definitive':
                vals['name_id'] = self.env['ir.sequence'].next_by_code('definitive.order') or ('New')
        return super(directoryorde, self).create(vals)


class sector(models.Model):

    _name = 'sector.type'

    name = fields.Char(string='Name')

class RubriquesRubriques(models.Model):

    _name = 'rubriques.type'

    name = fields.Char(string='Rubriques')


class MomentOfPayment(models.Model):

    _name = 'moment.payment'

    before_starting = fields.Boolean('Before Starting')
    before_str_prc = fields.Integer('Prc')
    before_finishing = fields.Boolean('Before Finishing')
    before_fin_prc = fields.Integer('Prc')
    after_finishing = fields.Boolean('After finishing')
    after_fini_prc = fields.Integer('Prc')
    after_billing = fields.Boolean('After Billing')
    after_billing_prc = fields.Integer('Prc')

class MethodeOfPayment(models.Model):

    _name = 'payment.methode'

    name = fields.Char('Payment Methode')
    code = fields.Char('Payment Methode Code')
    risk_level = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Risk level', default='one')


class CapPayment(models.Model):
        _name = 'cap.cap'

        payment_c = fields.Float('Payment Cap: ')
        cap_currency = fields.Many2one('res.currency', string='Currency')


class CustomerPayment(models.Model):
        _name = 'customer.payment'
        
        section_id = fields.Many2one('rubriques.type', string='Section')
        terms = fields.Integer('Term')
        moment_payment_id = fields.Many2one('moment.payment', string='Moment Of Payment')
        methode_payment_id = fields.Many2one('payment.methode', string='Payment method')
        payment_cap_id = fields.Many2one('cap.cap', string='Payment Cap')


class Customerdiscount(models.Model):
        
        _name = 'customer.discount'

        name = fields.Many2one('rubriques.type', string='Section')
        discount = fields.Integer('Discount %')


class BankDetails(models.Model):
        
        _name = 'bank.details'

        bank_details_line = fields.One2many('bank.bank','bank_details_id', string="Bank Details")                    
        

        
class references(models.Model):

    _name = 'reference.type'
    _rec_name = 'customer_ref'

    name = fields.Char(string='Ref name')
    customer_ref = fields.Char(string="Customer's Ref", required=True)
    purchase_order = fields.Char(string="Purchase Order (PO)")
    sales_order = fields.Char(string='Sales Order (SO)')
    shipment_reference = fields.Char(string='Shipment Ref')
    vendor_reference = fields.Char(string='Vendor Ref')
    consign_reference = fields.Char(string='Consignee Ref')
    ticket_n = fields.Char(string='Ticket N°')
    rma_n = fields.Char(string='RMA N°')
    beyer_ref = fields.Char(string='Byer Ref')
    ref_two = fields.Char(string='Ref2')
    ref_thre = fields.Char(string='Ref3')
    ref_four = fields.Char(string='Ref4')
    ref_five = fields.Char(string='Ref5')
    ref_six = fields.Char(string='Ref6')
    ref_id = fields.Many2one('directory.type', string="Ref ID")

class GroupGroup(models.Model):

    _name = 'group.type'

    name = fields.Char(string='Group name')

class NetworkNetwork(models.Model):

    _name = 'network.type'

    name = fields.Char(string='name')


class ResPartner(models.Model):

    _inherit = 'res.partner'

    rc = fields.Char(string='RC')
    ice = fields.Char(string='ICE')
    pic = fields.Char(string='PIC')
    pic_detail = fields.Char(string='PIC details')
    #sector = fields.Char(string='Sector')
    activity_description = fields.Text('Activity Description')
    currency_unit = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Currency', default='euro')
    capital = fields.Float(string="Capital")
    group = fields.Char('Group')
    date_creation = fields.Date('Date of creation')
    form = fields.Selection([
            ('sa', 'SA'),
            ('sarl', 'SARL'),
            ('sas', 'SAS'),
            ('sarl_au', 'SARL AU'),
            ('gie', 'GIE'),
            ('snc', 'SNC'),
            ('scs', 'SCS'),
            ('sca', 'SCA'),
            ('ae', 'AE'),
            ('others', 'Others'),
            ('dk', 'DK'),
            ], setting='Form', default='dk')
    legal_number = fields.Char(string='Legal number')
    company_size = fields.Selection([
            ('les_than_five', 'Less than 5 employee'),
            ('five_twee', '5-20 Employees'),
            ('twen_fif', '20-50 Employees'),
            ('fif_hund', '50-100 Employees'),
            ('hud_twh', '100-200 Employees'),
            ('twh_fihd', '200-500 Employees'),
            ('above', 'Above 500 Employees'),
            ], setting='Company Size', default='les_than_five')
    type_s = fields.Selection([
            ('natural', 'Natural'),
            ('legal', 'Legal'),
            ], setting='Type', default='natural')
    location = fields.Selection([
            ('local', 'Local'),
            ('foreign', 'Foreign'),
            ], setting='Location', default='local')
    number = fields.Char('Number')
    adress_compleme = fields.Text('Adress complement')
    pref_phone_one = fields.Char('Prefix')
    phone_one = fields.Char('Phone')
    pref_phone_two = fields.Char('Prefix')
    phone_two = fields.Char('Phone 1')
    pref_phone_three = fields.Char('Prefix')
    phone_three = fields.Char('Phone 2')
    pref_phone_four = fields.Char('Prefix')
    phone_four = fields.Char('Phone 3')
    fixe_prefix_ad = fields.Char('Prefix')
    fixe = fields.Char('Fixe')
    extention = fields.Char('Extension')
    extention_suf = fields.Char('Suffix')
    delivrey_add = fields.Text('Delivery Adress')
    invoicing_add = fields.Text('Invoicing Adress')
    other_add = fields.Text('Other Adress')
    sex = fields.Selection([
            ('mr', 'Mr'),
            ('mme', 'Mme'),
            ('mrs', 'Mrs'),
            ], setting='Sex', default='mr')
    mobile_prefix = fields.Char('Prefix')
    mobile_contact = fields.Char('Mobile')
    direct_prefix = fields.Char('Prefix')
    direct_contact = fields.Char('Direct')
    fixe_prefix = fields.Char('Prefix')
    fixe_contact = fields.Char('Fixe')
    depar_tment_id = fields.Many2one('hr.department', 'Department')
    title = fields.Selection([
            ('ceo', 'CEO'),
            ('g_dir', 'General Director'),
            ('mng_dir', 'Managing Director'),
            ('direc', 'Director'),
            ('head', 'Head of Department'),
            ('key', 'Key Account'),
            ('mng', 'Manager'),
            ('tech', 'Technicien'),
            ('agen', 'Agent'),
            ('assis', 'Assistant'),
            ], setting='Title', default='ceo')
    internal_note = fields.Text('Internal note')
     #service_type = fields.Many2many
    terms = fields.Integer('Term')
    before_starting = fields.Boolean('Before Starting')
    before_str_prc = fields.Char('Prc')
    before_finishing = fields.Boolean('Before Finishing')
    before_fin_prc = fields.Char('Prc')
    after_finishing = fields.Boolean('After finishing')
    after_fini_prc = fields.Char('Prc')
    after_billing = fields.Boolean('After Billing')
    after_billing_prc = fields.Char('Prc')
    billing_section_id_sup = fields.Many2one('billing.section', 'Billing Section')
    terms_su = fields.Integer('Term')
#     before_starting_sup = fields.Boolean('Before Starting')
#     before_str_prc_sup = fields.Char('Prc')
#     before_finishing_sup = fields.Boolean('Before Finishing')
#     before_fin_prc_sup = fields.Char('Prc')
#     after_finishing_sup = fields.Boolean('After finishing')
#     after_fini_prc_sup = fields.Char('Prc')
#     after_billing_sup = fields.Boolean('After Billing')
#     after_billing_prc_sup = fields.Char('Prc')
     #payment_type = fields.Many2many
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
    payment_cap = fields.Float('Payment Cap')
    payment_cap_sel = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='CPayment Cap', default='euro')
    total_paycap = fields.Float('Total payement cap')
    total_payment_cap = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Total CPayment Cap', default='euro')
    payment_cap_sup = fields.Float('Payment Cap')
    payment_cap_sel_sup = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='CPayment Cap', default='euro')
    total_paycap_sup = fields.Float('Total payement cap')
    total_spayment_cap = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Total Payment Cap', default='euro')
      #service_type_disc_cus = fields.Many2many('Service Type')
      #service_type_disc_sup = fields.Many2many('Service Type')
    rc_insurance = fields.Selection([
            ('no', 'No'),
            ('yes', 'Yes'),
            ], setting='RC Insurance', default='no')
    amount_rc = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Amount', default='euro')
    cargo_insurance = fields.Selection([
            ('no', 'No'),
            ('yes', 'Yes'),
            ], setting='Cargo Insurance', default='no')
    amount_cargo = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Amount', default='euro')
    exploitation_insurance = fields.Selection([
            ('no', 'No'),
            ('yes', 'Yes'),
            ], setting='Exploitation Insurance', default='no')
    amount_exploitation = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Amount', default='euro')
    other_insurance = fields.Selection([
            ('no', 'No'),
            ('yes', 'Yes'),
            ], setting='Other Insurance', default='no')
    amount_amount = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='Amount', default='euro')
    Communication_level = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Communication level', default='one')
    price_level = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Price level', default='one')
    service_level = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Service level', default='one')
    Risk = fields.Selection([
            ('one', 'Creditworthy'),
            ('two', 'Under control'),
            ('three', 'Frozen'),
            ], setting='Risk', default='one')
    equipment_availability = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Equipment availability', default='one')
    incidents = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Incidents', default='one')
    Communication_level_sup = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Communication level', default='one')
    price_level_sup = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Price level', default='one')
    service_level_sup = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Service level', default='one')
    Risk_sup = fields.Selection([
            ('one', 'Creditworthy'),
            ('two', 'Under control'),
            ('three', 'Frozen'),
            ], setting='Risk', default='one')
    equipment_availability_sup = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Equipment availability', default='one')
    incidents_sup = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Incidents', default='one')
    complexity_cons = fields.Selection([
            ('one', '1'),
            ('two', '2'),
            ('three', '3'),
            ('four', '4'),
            ('five', '5'),
            ('six', '6'),
            ('seven', '7'),
            ('eight', '8'),
            ('nine', '9'),
            ('teen', '10'),
            ], setting='Complexity', default='one')
    total_turnover = fields.Selection([
            ('one', '1 (<100k) mad'),
            ('two', '2 (100k-300k) mad'),
            ('three', '3 (300-500k) mad'),
            ('four', '4 ( 500-1000k) mad'),
            ('five', '5 (1000-2000k) mad'),
            ('six', '6 (2000-3000k) mad'),
            ('seven', '7 (3000-5000k) mad'),
            ('eight', '8 (5000-7500k) mad'),
            ('nine', '9 (7500-10000k) mad'),
            ('teen', '10 (>10M)'),
            ], setting='Total Turnover', default='one')
    total_at_cost = fields.Selection([
            ('one', '1 (<20k) mad'),
            ('two', '2 (20-50k) mad'),
            ('three', '3 (50-100k) mad'),
            ('four', '4 (100-200k) mad'),
            ('five', '5 ( 200-300k) mad'),
            ('six', '6 (300-400k) mad'),
            ('seven', '7 (400-500k) mad'),
            ('eight', '8 (500-1000k) mad'),
            ('nine', '9 (1000-2000k) mad'),
            ('teen', '10 (>2000k) mad'),
            ], setting='Total At Cost', default='one')
    profitability = fields.Selection([
            ('one', '1 (<5%)'),
            ('two', '2 (5-10%)'),
            ('three', '3 (10-15%)'),
            ('four', '4 (15-20%)'),
            ('five', '5 (20-25%)'),
            ('six', '6 (25-30%)'),
            ('seven', '7 (30-35%)'),
            ('eight', '8 (35-40%)'),
            ('nine', '9 (40-50%)'),
            ('teen', '10 (>50%)'),
            ], setting='Total At Cost', default='one')
    internal_notes_sup = fields.Text('Internal notes')
    file_upload = fields.Binary('Download Legal Documents' )
    service_type_ids = fields.Many2many('service.type', 'service_user_rel', 'user_id', 'service_ty_id', string='Service type')
    payment_cap_ids = fields.Many2many('payment.cap', 'payment_user_rel', 'usr_id', 'payment_ty_id', string='payment cap')
    sector_type_ids = fields.Many2many('sector.type', 'sector_user_rel', 'us_id', 'sector_ty_id', string='Sector')
    language_type_ids = fields.Many2many('language.type', 'language_user_rel', 'usrr_id', 'language_ty_id', string='Language')
    discount_ids = fields.Many2many('service.type.discount', 'dscount_user_rel', 'usre_id', 'discount_ty_id', string='Discount')
    discount_sup_ids = fields.Many2many('service.type.discount', 'dscount_sup_rel_rel', 'usr_su_id', 'discount_ty_sup_id', string='Discount')
    bank_bank_id = fields.Many2many('bank.bank', 'bank_user_rel', 'uer_id', 'bank_ty_id', string='Bank Account')
    bank_bank_sup_id = fields.Many2many('bank.bank', 'bank__sup_user_rel', 'uer_sup_id', 'bank_sup_ty_id', string='Bank Account')
    partnership_ids = fields.One2many('partner.ship.customer','partner_id', string="Partnership Customer")
    quantities_ids = fields.One2many('partner.ship.customer','quantity_id', string="Quantity Customer")
    quantities_two_ids = fields.One2many('partner.ship.customer','quantity_two_id', string="Quantity Customer two")
    partnership_sup_ids = fields.One2many('partner.ship.supplier', 'partnersup_id', string="Partnership Supplier")
    air_shipment_ids = fields.One2many('air.shipment', 'air_shipment_id', string="Air shipment")
    custom_formalities_ids = fields.One2many('custom.formalities', 'custom_formalities_id', string="Custom Formalities")
    services_fcl_ids = fields.One2many('services.fcl', 'services_fcl_id', string="Services FCL")    
    services_lcl_ids = fields.One2many('services.lcl', 'services_lcl_id', string="Services LCL")        
    services_ftl_ids = fields.One2many('services.ftl', 'services_ftl_id', string="Services FTL")            
    services_ltl_ids = fields.One2many('services.ltl', 'services_ltl_id', string="Services LTL")                
    services_reefer_ids = fields.One2many('services.reefer', 'services_reefer_id', string="Services REEFER")                    
    services_cargo_ids = fields.One2many('services.cargo', 'services_cargo_id', string="Services CARGO")                    
    services_bulk_ids = fields.One2many('services.bulk', 'services_bulk_id', string="Services BULK")                        
    services_liquid_ids = fields.One2many('services.liquid', 'services_liquid_id', string="Services LIQUID")                        
    services_mead_ids = fields.One2many('services.mead', 'services_mead_id', string="Services MEAD")                        
    services_storage_ids = fields.One2many('services.storage', 'services_storage_id', string="Services STORAGE")                        
    services_port_ids = fields.One2many('services.port', 'services_port_id', string="Services PORT")                            
    quantities_sup_ids = fields.One2many('partner.ship.supplier', 'quantity_sup_id', string="Quantity Supplier")
    quantities_sup_two_ids = fields.One2many('partner.ship.supplier', 'quantity_sup_two_id', string="Quantity Supplier two")
    directory_id = fields.Many2one('directory.type', 'Directory_ID')
    group_id = fields.Many2one('group.type', 'Group')
    network_id = fields.Many2one('network.type', 'Network')
    #account_number_id = fields.Char(related='directory_id.account_number', string="Account Number")
    #account_number_is = fields.Char(string="Account Number")
    commercial = fields.Many2one('hr.employee', 'commercial')
    csd = fields.Many2one('hr.employee', 'CSD')

    packaging = fields.Boolean(string='Packaging')
    ship_chandler = fields.Boolean(string="Ship Chandler")
    shipping_expert = fields.Boolean(string="Shipping expert")
    studies = fields.Boolean(string='Studies')
    quality_control = fields.Boolean(string='Quality Control')
    insurance = fields.Boolean(string='Insurance')
    it = fields.Boolean(string='IT')
    customs_administration = fields.Boolean(string='Customs AdministrationF')
    administrations = fields.Boolean(string='Administrations')
    bank_c = fields.Boolean(string='Bank')
    civil_work = fields.Boolean(string='Civil Work')
    equipment_fourniture = fields.Boolean(string='Equipment & fourniture')
#     di_r = fields.Selection([
#             ('e', 'E'),
#             ('i', 'I'),
#             ], setting='DIR', default='e')
#     customs_type_ids = fields.Many2many('customs.type', 'custom_user_rel', 'us_id', 'custom_ty_id', string='Customs type')
    payment_methode_id = fields.Many2many('payment.type', 'paymentmet_us_rel', 'u_id', 'payment_meth_id', string='Payment Methode')
    payment_methode_sup_id = fields.Many2many('payment.type', 'paymentmet_sup_us_rel', 'su_id', 'payment_meth_sup_id', string='Payment Methode')      
    type = fields.Selection(
            [('contact', 'Contact'),
            ('invoice', 'Billing Address'),
            ('delivery', 'Shipping Address'),
            ('other', 'Other Address'),
            ("private", "Personal Address"),
            ("main", "Main Address"),
            ("head", "Headquarter Address"),
            ], string='Address Type',
            default='contact',
            help="Invoice & Delivery addresses are used in sales orders. Private addresses are only visible by authorized users.")
    fax = fields.Char(string='Fax')

    billing_section_id = fields.Many2one('billing.section', 'Billing Section')
    bank_details = fields.Text('Bank details')
    iban = fields.Char('IBAN')
    code_swift = fields.Char('Code swift')
    visit_card = fields.Binary('Visit card')
    type_insurance = fields.Selection([
            ('liability', 'Liability'),
            ('cargo', 'Cargo'),
            ('exploitation', 'Exploitation'),
            ('other', 'Other'),
            ], string='Type')
    other_bool = fields.Boolean('Other')
    other_type = fields.Char('Other')
    liability_bo = fields.Boolean('Liability')
    cargo_bo = fields.Boolean('Cargo')
    Exploitation_bo = fields.Boolean('Exploitation')
    currency_id_liab = fields.Many2one('res.currency', string='Currency')
    currency_id_car = fields.Many2one('res.currency', string='Currency')
    currency_id_expl = fields.Many2one('res.currency', string='Currency')
    currency_id_oth = fields.Many2one('res.currency', string='Currency')
    amount_li = fields.Float('lib')
    amount_car = fields.Float('car')
    amount_exp = fields.Float('exp')
    amount_oth = fields.Float('oth')
    amount_insurance_currency = fields.Selection([
            ('mad', 'MAD'),
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ], setting='Amount')
    amount = fields.Float('Amount')
    van = fields.Boolean('VAN', default=False)
    qty_van = fields.Char('Qty')
    pickup = fields.Boolean(string='Pickup', default=False)
    qty_pick = fields.Char('Qty')
    fourgon = fields.Boolean(string='Fourgon', default=False)
    qty_forg = fields.Char('Qty')
    camionnette = fields.Boolean('Camionnette', default=False)
    qty_cami = fields.Char('Qty')
    camion_sixm = fields.Boolean(string='Camion 6m', default=False)
    qty_six = fields.Char('Qty')
    trailertweelvm = fields.Boolean(string='Trailer12m', default=False)
    qty_tra = fields.Char('Qty')
    trailer_six_eigh = fields.Boolean('trailer 16-18m', default=False)
    qty_tr_six = fields.Char('Qty')
    trailer_eight_twe  = fields.Boolean(string='Trailer 18-22m', default=False)
    qty_eight = fields.Char('Qty')
    trailer_therte = fields.Boolean(string='Trailer 22-30m', default=False)
    qty_there = fields.Char('Qty')
    tralier_grat_ther = fields.Boolean(string='Tralier > 30m', default=False)
    qty_grat = fields.Char('Qty')
    lowbed_smal_the = fields.Boolean(string='Lowbed <40t', default=False)
    qty_low = fields.Char('Qty')
    lowbed_fort = fields.Boolean(string='Lowbed 40-70t', default=False)
    qty_for = fields.Char('Qty')
    lowbed_smal_sev = fields.Boolean(string='Lowbed >70t', default=False)
    qty_smal = fields.Char('Qty')
    hydraulic_trailers_axles = fields.Boolean(string='Hydraulic trailers axles', default=False)
    qty_hyd = fields.Char('Qty')
    spmt_axles = fields.Boolean(string='Spmt axles', default=False)
    qty_axl = fields.Char('Qty')
    gantry = fields.Boolean(string='Gantry', default=False)
    qty_gant = fields.Char('Qty')
    hydraulic_jacks = fields.Boolean(string='Hydraulic jacks', default=False)
    qty_jack = fields.Char('Qty')
    cranes_smal_ther = fields.Boolean(string='Cranes <30t', default=False)
    qty_sma = fields.Char('Qty')
    carnes_small_thre = fields.Boolean(string='Cranes 30-100t', default=False)
    qty_sma_th = fields.Char('Qty')
    cranes_hundredt = fields.Boolean(string='Cranes 100-200t', default=False)
    qty_cra = fields.Char('Qty')
    cranes_two_h = fields.Boolean(string='Cranes 200-300t', default=False)
    qty_two = fields.Char('Qty')
    cranes_three = fields.Boolean(string='Cranes >300t', default=False)
    qty_cra_thr = fields.Char('Qty')
    forklift_small_than_four = fields.Boolean(string='Forklift <4t', default=False)
    qty_fork_sm = fields.Char('Qty')
    forklift_between = fields.Boolean(string='Forklift 4-15t', default=False)
    qty_fork_bet = fields.Char('Qty')
    forklift_fift_twen = fields.Boolean(string="Forklift 15-25t", default=False)
    qty_fif = fields.Char('Qty')
    forklift_biger_than = fields.Boolean(string='Forklift >25t', default=False)
    qty_big = fields.Char('Qty')
    nacelles = fields.Boolean(string='Nacelles', default=False)
    qty_nac = fields.Char('Qty')

    fcl_sup = fields.Boolean(string='FCL')
    lcl_sup = fields.Boolean(string="LCL")
    project_cargo_sup = fields.Boolean(string="Project cargo")
    ftl_sup = fields.Boolean(string='FTL')
    ltl_sup = fields.Boolean(string='LTL')
    bulk_sup = fields.Boolean(string='Bulk')
    bulk_liquid_sup = fields.Boolean(string='Bulk liquid')
    med_sup = fields.Boolean(string='Mead (m²)')
    qty_med_sup = fields.Char(string="Qty")
    storage_sup = fields.Boolean(string='Storage (m²)')
    qty_storage_sup = fields.Char(string='Qty')
    airline_ff_sup = fields.Boolean(string='Airline FF')
    shipping_line_sup = fields.Boolean(string='Shipping line')
    airline_sup = fields.Boolean(string='Airline')
    port_operations_sup = fields.Boolean(string='Port operations')
    customs_formalities_sup = fields.Boolean(string='Customs Formalities')
    van_sup = fields.Boolean('VAN', default=False)
    qty_van_sup = fields.Char('Qty')
    pickup_sup = fields.Boolean(string='Pickup', default=False)
    qty_pick_sup = fields.Char('Qty')
    fourgon_sup = fields.Boolean(string='Fourgon', default=False)
    qty_forg_sup = fields.Char('Qty')
    camionnette_sup = fields.Boolean('Camionnette', default=False)
    qty_cami_sup = fields.Char('Qty')
    camion_sixm_sup = fields.Boolean(string='Camion 6m', default=False)
    qty_six_sup = fields.Char('Qty')
    trailertweelvm_sup = fields.Boolean(string='Trailer12m', default=False)
    qty_tra_sup = fields.Char('Qty')
    trailer_six_eigh_sup = fields.Boolean('trailer 16-18m', default=False)
    qty_tr_six_sup = fields.Char('Qty')
    trailer_eight_twe_sup  = fields.Boolean(string='Trailer 18-22m', default=False)
    qty_eight_sup = fields.Char('Qty')
    trailer_therte_sup = fields.Boolean(string='Trailer 22-30m', default=False)
    qty_there_sup = fields.Char('Qty')
    tralier_grat_ther_sup = fields.Boolean(string='Tralier > 30m', default=False)
    qty_grat_sup = fields.Char('Qty')
    lowbed_smal_the_sup = fields.Boolean(string='Lowbed <40t', default=False)
    qty_low_sup = fields.Char('Qty')
    lowbed_fort_sup = fields.Boolean(string='Lowbed 40-70t', default=False)
    qty_for_sup = fields.Char('Qty')
    lowbed_smal_sev_sup = fields.Boolean(string='Lowbed >70t', default=False)
    qty_smal_sup = fields.Char('Qty')
    hydraulic_trailers_axles_sup = fields.Boolean(string='Hydraulic trailers axles', default=False)
    qty_hyd_sup = fields.Char('Qty')
    spmt_axles_sup = fields.Boolean(string='Spmt axles', default=False)
    qty_axl_sup = fields.Char('Qty')
    gantry_sup = fields.Boolean(string='Gantry', default=False)
    qty_gant_sup = fields.Char('Qty')
    hydraulic_jacks_sup = fields.Boolean(string='Hydraulic jacks', default=False)
    qty_jack_sup = fields.Char('Qty')
    cranes_smal_ther_sup = fields.Boolean(string='Cranes <30t', default=False)
    qty_sma_sup = fields.Char('Qty')
    carnes_small_thre_sup = fields.Boolean(string='Cranes 30-100t', default=False)
    qty_sma_th_sup = fields.Char('Qty')
    cranes_hundredt_sup = fields.Boolean(string='Cranes 100-200t', default=False)
    qty_cra_sup = fields.Char('Qty')
    cranes_two_h_sup = fields.Boolean(string='Cranes 200-300t', default=False)
    qty_two_sup = fields.Char('Qty')
    cranes_three_sup = fields.Boolean(string='Cranes >300t', default=False)
    qty_cra_thr_sup = fields.Char('Qty')
    forklift_small_than_four_sup = fields.Boolean(string='Forklift <4t', default=False)
    qty_fork_sm_sup = fields.Char('Qty')
    forklift_between_sup = fields.Boolean(string='Forklift 4-15t', default=False)
    qty_fork_bet_sup = fields.Char('Qty')
    forklift_fift_twen_sup = fields.Boolean(string="Forklift 15-25t", default=False)
    qty_fif_sup = fields.Char('Qty')
    forklift_biger_than_sup = fields.Boolean(string='Forklift >25t', default=False)
    qty_big_sup = fields.Char('Qty')
    nacelles_sup = fields.Boolean(string='Nacelles', default=False)
    qty_nac_sup = fields.Char('Qty')
    packaging_sup = fields.Boolean(string='Packaging')
    ship_chandler_sup = fields.Boolean(string="Ship Chandler")
    shipping_expert_sup = fields.Boolean(string="Shipping expert")
    studies_sup = fields.Boolean(string='Studies')
    quality_control_sup = fields.Boolean(string='Quality Control')
    insurance_sup = fields.Boolean(string='Insurance')
    it_sup = fields.Boolean(string='IT')
    customs_administration_sup = fields.Boolean(string='Customs AdministrationF')
    administrations_sup = fields.Boolean(string='Administrations')
    bank_c_sup = fields.Boolean(string='Bank')
    civil_work_sup = fields.Boolean(string='Civil Work')
    equipment_fourniture_sup = fields.Boolean(string='Equipment & fourniture')
    currency_cap = fields.Many2one('res.currency', string='Currency')
    customer_payment_id = fields.Many2one('customer.payment', string='Customer Payment term')
    customer_discount_id = fields.Many2one('customer.discount', string='Customer Discount')
    total_paym_cap = fields.Float('Total payement cap')
    bank_bank_id = fields.Many2one('bank.details', string='Bank Details')
    supliers_payment_id = fields.Many2one('customer.payment', string='Supliers Payment term')
    supliers_discount_id = fields.Many2one('customer.discount', string='Supliers Discount')
    total_paym_cap_sup = fields.Float('Total payement cap')
    bank_bank_sup_id = fields.Many2one('bank.details', string='Bank Details')
    currency_cap_sup = fields.Many2one('res.currency', string='Currency')

#     total_cap_currency = fields.Many2one('res.currency', string='Currency')
        


    @api.constrains('hs_code')
    def _check_my_field(self):
            hs_code = self.hs_code
            if hs_code and len(str(abs(hs_code))) > 4:
                    raise ValidationError('le nombre de chiffre composant le HS code ne doit pas dépassé 4 chiffres')
    #indication_ids = fields.One2many('cargo.indication','indication_id', string='Cargo indication')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('res.partner') or '/'
        return super(ResPartner, self).create(vals)
        
    
    
#     @api.onchange('directory_id')
#     def onchange_employee_id(self):
#         self.account_number_is = self.directory_id.account_number
class AirShipment(models.Model):
        
        _name = 'air.shipment'

        di_r_air = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        shipment_y = fields.Integer('Shipment /Y')
        incoterm_id_air = fields.Many2one('incoterm.type', 'Incoterm')
        destination_air = fields.Many2one('destination.provenance', 'Destination')
        provenance_air = fields.Many2one('destination.provenance', 'Provenance')
        air_shipment_id = fields.Many2one('res.partner', string="Airshipment IDs")

class ServicesFcl(models.Model):

        _name = 'services.fcl'

        di_r_fcl = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        teus_y = fields.Integer('TEUs /Y')
        incoterm_id_fcl = fields.Many2one('incoterm.type', 'Incoterm')
        destination_fcl = fields.Many2one('destination.provenance', 'Destination')
        provenance_fcl = fields.Many2one('destination.provenance', 'Provenance')
        services_fcl_id = fields.Many2one('res.partner', string='Services FCL ID')

class ServicesCargo(models.Model):
        _name = "services.cargo"

        di_r_cargo = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        wm_y_cargo = fields.Integer('wm /Y')
        incoterm_id_cargo = fields.Many2one('incoterm.type', 'Incoterm')
        destination_cargo = fields.Many2one('destination.provenance', 'Destination')
        provenance_cargo = fields.Many2one('destination.provenance', 'Provenance')
        services_cargo_id = fields.Many2one('res.partner', string='Services CARGO ID')

class ServicesStorage(models.Model):
        _name = "services.storage"

        di_r_storage = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        wm_y_storage = fields.Integer('wm /Y')
        incoterm_id_storage = fields.Many2one('incoterm.type', 'Incoterm')
        destination_storage = fields.Many2one('destination.provenance', 'Destination')
        provenance_storage = fields.Many2one('destination.provenance', 'Provenance')
        services_storage_id = fields.Many2one('res.partner', string='Services CARGO ID')

class ServicesPort(models.Model):
        _name = "services.port"

        di_r_port = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        wm_y_port = fields.Integer('wm /Y')
        incoterm_id_port = fields.Many2one('incoterm.type', 'Incoterm')
        destination_port = fields.Many2one('destination.provenance', 'Destination')
        provenance_port = fields.Many2one('destination.provenance', 'Provenance')
        services_port_id = fields.Many2one('res.partner', string='Services PORT ID')

class ServicesBulk(models.Model):
        _name = "services.bulk"

        di_r_bulk = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        wm_y_bulk = fields.Integer('wm /Y')
        incoterm_id_bulk = fields.Many2one('incoterm.type', 'Incoterm')
        destination_bulk = fields.Many2one('destination.provenance', 'Destination')
        provenance_bulk = fields.Many2one('destination.provenance', 'Provenance')
        services_bulk_id = fields.Many2one('res.partner', string='Services BULK ID')

class ServicesLiquid(models.Model):
        _name = "services.liquid"

        di_r_liquid = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        wm_y_liquid = fields.Integer('wm /Y')
        incoterm_id_liquid = fields.Many2one('incoterm.type', 'Incoterm')
        destination_liquid = fields.Many2one('destination.provenance', 'Destination')
        provenance_liquid = fields.Many2one('destination.provenance', 'Provenance')
        services_liquid_id = fields.Many2one('res.partner', string='Services LIQUID ID')

class CustomFormalities(models.Model):

        _name = 'custom.formalities'

        di_r = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        customs_type_ids = fields.Many2many('customs.type', 'custom_user_rel', 'us_id', 'custom_ty_id', string='Customs type')
        item_description_id = fields.Many2one('items.type', 'Item Description')
        hs_code = fields.Integer('HS code')
        files_y = fields.Integer('Files /Y')
        incoterm_id = fields.Many2one('incoterm.type', 'Incoterm')
        destination = fields.Many2one('destination.provenance', 'Destination')
        provenance = fields.Many2one('destination.provenance', 'Provenance')
        custom_formalities_id = fields.Many2one('res.partner', string='custom formalities ID')

class ServicesLCL(models.Model):
        _name = 'services.lcl'

        di_r_lcl = fields.Selection([
                ('e', 'E'),
                ('i', 'I'),
                ], setting='DIR', default='e')
        wm_y = fields.Integer('wm /Y')
        incoterm_id_lcl = fields.Many2one('incoterm.type', 'Incoterm')
        destination_lcl = fields.Many2one('destination.provenance', 'Destination')
        provenance_lcl = fields.Many2one('destination.provenance', 'Provenance')
        services_lcl_id = fields.Many2one('res.partner', string='Services LCL ID')

class ServicesReefer(models.Model):
        _name = "services.reefer"

        di_r_refer = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        teus_y_refer = fields.Integer('TEUs /Y')
        incoterm_id_refer = fields.Many2one('incoterm.type', 'Incoterm')
        destination_refer = fields.Many2one('destination.provenance', 'Destination')
        provenance_refer = fields.Many2one('destination.provenance', 'Provenance')
        services_reefer_id = fields.Many2one('res.partner', string='Services Reefer ID')

class ServicesFTL(models.Model):
        _name = 'services.ftl'

        di_r_ftl = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        trailer_y = fields.Integer('wm /Y')
        incoterm_id_ftl = fields.Many2one('incoterm.type', 'Incoterm')
        destination_ftl = fields.Many2one('destination.provenance', 'Destination')
        provenance_ftl = fields.Many2one('destination.provenance', 'Provenance')
        services_ftl_id = fields.Many2one('res.partner', string='Services FTL ID')

class ServicesMead(models.Model):
        _name = 'services.mead'

        di_r_mead = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        wm_y_mead = fields.Integer('wm /Y')
        incoterm_id_mead = fields.Many2one('incoterm.type', 'Incoterm')
        destination_mead = fields.Many2one('destination.provenance', 'Destination')
        provenance_mead = fields.Many2one('destination.provenance', 'Provenance')
        services_mead_id = fields.Many2one('res.partner', string='Services MEAD ID')

class ServicesLTL(models.Model):
        _name = 'services.ltl'

        di_r_ltl = fields.Selection([
            ('e', 'E'),
            ('i', 'I'),
            ], setting='DIR', default='e')
        wm_y_ltl = fields.Integer('wm /Y')
        incoterm_id_ltl = fields.Many2one('incoterm.type', 'Incoterm')
        destination_ltl = fields.Many2one('destination.provenance', 'Destination')
        provenance_ltl = fields.Many2one('destination.provenance', 'Provenance')
        services_ltl_id = fields.Many2one('res.partner', string='Services LTL ID')

class BillingSection(models.Model):

    _name = 'billing.section'

    name  = fields.Char('B.Section: ')

class DestinationProvenance(models.Model):

    _name = 'destination.provenance'
    _order = 'code'

    country_id = fields.Many2one('res.country', string='Country')
    name  = fields.Char('name')
    code = fields.Char(string='city Code', help='The city code.')

class incotermtype(models.Model):
        _name = 'incoterm.type'

        name = fields.Char('Incoterm') 

class customtype(models.Model):
        _name = 'customs.type'

        name = fields.Char('Customs Type: ') 

class ItemsDescription(models.Model):
        _name = 'items.type'

        name = fields.Char('Item Description: ') 

class servicetype(models.Model):
        _name = 'service.type'

        name = fields.Char('Service Type: ') 

class paymentcap(models.Model):
        _name = 'payment.cap'

        name = fields.Char('Payment Cap: ')

class servicetypediscount(models.Model):
        
        _name = 'service.type.discount'

        name = fields.Many2one('billing.section', 'Billing Section')
        discount = fields.Integer('Discount %')

class partnershipcustomer(models.Model):

    _name = 'partner.ship.customer'

    fcl = fields.Char(string='FCL')
    lcl = fields.Char(string="LCL")
    project_cargo = fields.Char(string="Project cargo")
    ftl = fields.Char(string='FTL')
    ltl = fields.Char(string='LTL')
    med = fields.Char(string='Mead')
    storage = fields.Char(string='Storage')
    airline_ff = fields.Char(string='Airline FF')
    shipping_line = fields.Char(string='Shipping line')
    airline = fields.Char(string='Airline')
    port_operations = fields.Char(string='Port operations')
    customs_formalities = fields.Char(string='Customs Formalities')
    van = fields.Boolean('VAN', default=False)
    qty_van = fields.Char('Qty')
    pickup = fields.Boolean(string='Pickup', default=False)
    qty_pick = fields.Char('Qty')
    fourgon = fields.Boolean(string='Fourgon', default=False)
    qty_forg = fields.Char('Qty')
    camionnette = fields.Boolean('Camionnette', default=False)
    qty_cami = fields.Char('Qty')
    camion_sixm = fields.Boolean(string='Camion 6m', default=False)
    qty_six = fields.Char('Qty')
    trailertweelvm = fields.Boolean(string='Trailer12m', default=False)
    qty_tra = fields.Char('Qty')
    trailer_six_eigh = fields.Boolean('trailer 16-18m', default=False)
    qty_tr_six = fields.Char('Qty')
    trailer_eight_twe  = fields.Boolean(string='Trailer 18-22m', default=False)
    qty_eight = fields.Char('Qty')
    trailer_therte = fields.Boolean(string='Trailer 22-30m', default=False)
    qty_there = fields.Char('Qty')
    tralier_grat_ther = fields.Boolean(string='Tralier > 30m', default=False)
    qty_grat = fields.Char('Qty')
    lowbed_smal_the = fields.Boolean(string='Lowbed <40t', default=False)
    qty_low = fields.Char('Qty')
    lowbed_fort = fields.Boolean(string='Lowbed 40-70t', default=False)
    qty_for = fields.Char('Qty')
    lowbed_smal_sev = fields.Boolean(string='Lowbed >70t', default=False)
    qty_smal = fields.Char('Qty')
    hydraulic_trailers_axles = fields.Boolean(string='Hydraulic trailers axles', default=False)
    qty_hyd = fields.Char('Qty')
    spmt_axles = fields.Boolean(string='Spmt axles', default=False)
    qty_axl = fields.Char('Qty')
    gantry = fields.Boolean(string='Gantry', default=False)
    qty_gant = fields.Char('Qty')
    hydraulic_jacks = fields.Boolean(string='Hydraulic jacks', default=False)
    qty_jack = fields.Char('Qty')
    cranes_smal_ther = fields.Boolean(string='Cranes <30t', default=False)
    qty_sma = fields.Char('Qty')
    carnes_small_thre = fields.Boolean(string='Cranes 30-100t', default=False)
    qty_sma_th = fields.Char('Qty')
    cranes_hundredt = fields.Boolean(string='Cranes 100-200t', default=False)
    qty_cra = fields.Char('Qty')
    cranes_two_h = fields.Boolean(string='Cranes 200-300t', default=False)
    qty_two = fields.Char('Qty')
    cranes_three = fields.Boolean(string='Cranes >300t', default=False)
    qty_cra_thr = fields.Char('Qty')
    forklift_small_than_four = fields.Boolean(string='Forklift <4t', default=False)
    qty_fork_sm = fields.Char('Qty')
    forklift_between = fields.Boolean(string='Forklift 4-15t', default=False)
    qty_fork_bet = fields.Char('Qty')
    forklift_fift_twen = fields.Boolean(string="Forklift 15-25t", default=False)
    qty_fif = fields.Char('Qty')
    forklift_biger_than = fields.Boolean(string='Forklift >25t', default=False)
    qty_big = fields.Char('Qty')
    nacelles = fields.Boolean(string='Nacelles', default=False)
    qty_nac = fields.Char('Qty')
    packaging = fields.Boolean(string='Packaging')
    ship_chandler = fields.Boolean(string="Ship Chandler")
    shipping_expert = fields.Boolean(string="Shipping expert")
    studies = fields.Boolean(string='Studies')
    quality_control = fields.Boolean(string='Quality Control')
    insurance = fields.Boolean(string='Insurance')
    it = fields.Boolean(string='IT')
    customs_administration = fields.Boolean(string='Customs AdministrationF')
    administrations = fields.Boolean(string='Administrations')
    bank_c = fields.Boolean(string='Bank')
    civil_work = fields.Boolean(string='Civil Work')
    equipment_fourniture = fields.Boolean(string='Equipment & fourniture')
    partner_id = fields.Many2one('res.partner', string="Partner ID")  
    quantity_id = fields.Many2one('res.partner', string="Quantity ID")
    quantity_two_id = fields.Many2one('res.partner', string="Quantity IDs")
    


class partnershipsupplier(models.Model):

    _name = 'partner.ship.supplier'

    fcl_sup = fields.Boolean(string='FCL')
    lcl_sup = fields.Boolean(string="LCL")
    project_cargo_sup = fields.Boolean(string="Project cargo")
    ftl_sup = fields.Boolean(string='FTL')
    ltl_sup = fields.Boolean(string='LTL')
    bulk_sup = fields.Boolean(string='Bulk')
    bulk_liquid_sup = fields.Boolean(string='Bulk liquid')
    med_sup = fields.Boolean(string='Mead (m²)')
    qty_med_sup = fields.Char(string="Qty")
    storage_sup = fields.Boolean(string='Storage (m²)')
    qty_storage_sup = fields.Char(string='Qty')
    airline_ff_sup = fields.Boolean(string='Airline FF')
    shipping_line_sup = fields.Boolean(string='Shipping line')
    airline_sup = fields.Boolean(string='Airline')
    port_operations_sup = fields.Boolean(string='Port operations')
    customs_formalities_sup = fields.Boolean(string='Customs Formalities')
    van_sup = fields.Boolean('VAN', default=False)
    qty_van_sup = fields.Char('Qty')
    pickup_sup = fields.Boolean(string='Pickup', default=False)
    qty_pick_sup = fields.Char('Qty')
    fourgon_sup = fields.Boolean(string='Fourgon', default=False)
    qty_forg_sup = fields.Char('Qty')
    camionnette_sup = fields.Boolean('Camionnette', default=False)
    qty_cami_sup = fields.Char('Qty')
    camion_sixm_sup = fields.Boolean(string='Camion 6m', default=False)
    qty_six_sup = fields.Char('Qty')
    trailertweelvm_sup = fields.Boolean(string='Trailer12m', default=False)
    qty_tra_sup = fields.Char('Qty')
    trailer_six_eigh_sup = fields.Boolean('trailer 16-18m', default=False)
    qty_tr_six_sup = fields.Char('Qty')
    trailer_eight_twe_sup  = fields.Boolean(string='Trailer 18-22m', default=False)
    qty_eight_sup = fields.Char('Qty')
    trailer_therte_sup = fields.Boolean(string='Trailer 22-30m', default=False)
    qty_there_sup = fields.Char('Qty')
    tralier_grat_ther_sup = fields.Boolean(string='Tralier > 30m', default=False)
    qty_grat_sup = fields.Char('Qty')
    lowbed_smal_the_sup = fields.Boolean(string='Lowbed <40t', default=False)
    qty_low_sup = fields.Char('Qty')
    lowbed_fort_sup = fields.Boolean(string='Lowbed 40-70t', default=False)
    qty_for_sup = fields.Char('Qty')
    lowbed_smal_sev_sup = fields.Boolean(string='Lowbed >70t', default=False)
    qty_smal_sup = fields.Char('Qty')
    hydraulic_trailers_axles_sup = fields.Boolean(string='Hydraulic trailers axles', default=False)
    qty_hyd_sup = fields.Char('Qty')
    spmt_axles_sup = fields.Boolean(string='Spmt axles', default=False)
    qty_axl_sup = fields.Char('Qty')
    gantry_sup = fields.Boolean(string='Gantry', default=False)
    qty_gant_sup = fields.Char('Qty')
    hydraulic_jacks_sup = fields.Boolean(string='Hydraulic jacks', default=False)
    qty_jack_sup = fields.Char('Qty')
    cranes_smal_ther_sup = fields.Boolean(string='Cranes <30t', default=False)
    qty_sma_sup = fields.Char('Qty')
    carnes_small_thre_sup = fields.Boolean(string='Cranes 30-100t', default=False)
    qty_sma_th_sup = fields.Char('Qty')
    cranes_hundredt_sup = fields.Boolean(string='Cranes 100-200t', default=False)
    qty_cra_sup = fields.Char('Qty')
    cranes_two_h_sup = fields.Boolean(string='Cranes 200-300t', default=False)
    qty_two_sup = fields.Char('Qty')
    cranes_three_sup = fields.Boolean(string='Cranes >300t', default=False)
    qty_cra_thr_sup = fields.Char('Qty')
    forklift_small_than_four_sup = fields.Boolean(string='Forklift <4t', default=False)
    qty_fork_sm_sup = fields.Char('Qty')
    forklift_between_sup = fields.Boolean(string='Forklift 4-15t', default=False)
    qty_fork_bet_sup = fields.Char('Qty')
    forklift_fift_twen_sup = fields.Boolean(string="Forklift 15-25t", default=False)
    qty_fif_sup = fields.Char('Qty')
    forklift_biger_than_sup = fields.Boolean(string='Forklift >25t', default=False)
    qty_big_sup = fields.Char('Qty')
    nacelles_sup = fields.Boolean(string='Nacelles', default=False)
    qty_nac_sup = fields.Char('Qty')
    packaging_sup = fields.Boolean(string='Packaging')
    ship_chandler_sup = fields.Boolean(string="Ship Chandler")
    shipping_expert_sup = fields.Boolean(string="Shipping expert")
    studies_sup = fields.Boolean(string='Studies')
    quality_control_sup = fields.Char(string='Quality Control')
    insurance_sup = fields.Boolean(string='Insurance')
    it_sup = fields.Boolean(string='IT')
    customs_administration_sup = fields.Boolean(string='Customs AdministrationF')
    administrations_sup = fields.Boolean(string='Administrations')
    bank_c_sup = fields.Boolean(string='Bank')
    civil_work_sup = fields.Boolean(string='Civil Work')
    equipment_fourniture_sup = fields.Boolean(string='Equipment & fourniture')
    partnersup_id = fields.Many2one('res.partner', string="Partner ID")  
    quantity_sup_id = fields.Many2one('res.partner', string="Quantity ID")
    quantity_sup_two_id = fields.Many2one('res.partner', string="Quantity IDs")

class SectorType(models.Model):

    _name = 'sector.type'

    name = fields.Char("sector name")

class LanguageType(models.Model):

    _name = 'language.type'

    name = fields.Char("Language")




      




#      partner_ship = fields.Many2many('')
#      sector = fields.Selection([
#             ('sa', 'Agriculture, Forestry, Fishery'),
#             ('sas', 'Arts, entertainment and recreation'),
#             ('sarl_au', 'Hospitality and Tourism'),
#             ('gie', 'Human health and social services activities'),
#             ('snc', 'ICT service activities'),
#             ('scs', 'Manufacturing of food, beverages and tobacco'),
#             ('sca', 'Manufacturing of Textile, Apparel, Leather, Footwear and related products'),
#             ('sas', 'Mining and heavy industry'),
#             ('sarl_au', 'Transportation and storage'),
#             ('gie', 'Veterinary activities'),
#             ('snc', 'Wholesale and retail trade, renting and leasing'),
#             ('scs', 'Business administration'),
#             ('sca', 'Chemical industry'),
#             ('sa', 'Construction'),
#             ('sas', 'Education'),
#             ('sarl_au', 'Energy and water supply, sewerage and waste management'),
#             ('gie', 'Finance, insurance and real estate'),
#             ('snc', 'Manufacturing of consumer goods except food, beverages, tobacco, textile, apparel, leather'),
#             ('scs', 'Manufacturing of electrical equipment, computer, electronic and optical products'),
#             ('sca', 'Manufacturing of fabricated metal products, except machinery and equipment'),
#             ('sas', 'Manufacturing of machinery and equipment, except electrical equipment'),
#             ('sarl_au', 'Manufacturing of transport equipment'),
#             ('gie', 'Media'),
#             ('snc', 'Personal service -, administrative support service- and security and investigation activities'),
#             ('scs', 'Public administration and defence and membership organisations'),
#             ('sca', 'Scientific and technical activities'),
#             ('sca', 'Wood processing, paper and printing'),
#             ], setting='Company Size', default='sa')
     

# class partnership(models.Model):

#     _name = 'partnership'

#     type_partner = fields.Char('Type Partnership')



