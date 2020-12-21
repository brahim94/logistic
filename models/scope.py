# -*- coding: utf-8 -*-

from odoo import models, fields, api


class scope(models.Model):

    _name = 'scope.type'
    _rec_name = 'direction'

    # packagin_division_id = fields.Many2many('packagin.division', 'division_user_rel', 'scope_id', 'division_id', string='Division')
    packagin_division_id = fields.Many2one('packagin.division', string='Service')    
    direction = fields.Selection([
            ('export', 'Export (E)'),
            ('import', 'Import (I)'),
            ('local', 'Local (L)'),
            ('off', 'OffShore (Off)'),
            ('offon', 'OffOnShore (OffOn)'),
            ('offoncl', 'OffOnShore Cleared (OffOnCl)'),
            ], string='Direction', default='export')
    packagin_mode_transport_id = fields.Many2one('transport.mode', string='Mode of Transport')
    scope = fields.Selection([
            ('packaging', 'Packaging'),
            ('stuffing', 'Stuffing'),
            ('lsd', 'LSD'),
            ('loading_on_truck', 'Loading On Truck'),
            ('export_formalities', 'Export Formalities'),
            ('pre_carriage', 'Pre-Carriage'),
            ('export_customs', 'Export Customs'),
            ('terminal', 'Terminal Entry Formalities'),
            ('unloading', 'Unloading On Terminal'),
            ('export', 'Export Agency'),
            ('loading', 'Loading on Main Transport'),
            ('main_transport', 'Main Transport'),   
            ('unloading_from', 'Unloading From Main Transport'),
            ('import_agency', 'Import Agency'),
            ('import_formalities', 'Import Formalities'),
            ('import_customs', 'Import Customs'),
            ('loading_from_terminal', 'Loading From Terminal'),
            ('terminal_exit_formalities', 'Terminal Exit Formalities'),   
            ('delivery', 'Delivery'),
            ('unloading_on_site', 'Unloading on site'),
            ('local', 'Local (L)'),
            ('unlashing', 'Unlashing'),
            ('stripping', 'Stripping'),
            ('unpackaging', 'Unpackaging'),
            ('other_customs_formalities', 'Other Customs Formalities'),
            ('other_requests', 'Other Requests'),
            ('insurance_int', 'Insurance Int'),
            ('insurance_dom', 'Insurance Dom'),
            ('domestic_customs', 'Domestic Customs'),
            ('trailer_traction', 'Trailer Traction'),
            ('storage', 'Storage'),
            ('lifting', 'Lifting'),
            ('domestic_haulage', 'Domestic Haulage'),
            ('renting', 'Renting'),
            ('consulting', 'Consulting'),
            ('road_survey', 'Road survey'),
            ('studies', 'Studies'),
            ('survey_report', 'Survey Report'),
            ('escort', 'Escort'),
            ('civil_work', 'Civil Work'),
            ], string='Scope', default='packaging')

    service  = fields.Text('Service')
    service_n = fields.Char('Service N°')
    service_detail = fields.Text('Detail')
    packagin_criteria_id = fields.Many2one('packagin.criteria', string='Criteria')
    packagin_section_id = fields.Many2one('packaging.section', string='Section')
    atc = fields.Selection([
            ('yes', 'Yes'),
            ('no', 'No'),
            ], string='ATC', default='yes')
    cost_rate_ht_currency = fields.Many2one('res.currency', string='Currency')
    cost_rate_ht_monet = fields.Float('Cost Rate HT')
    suppliers = fields.Many2one('res.partner', string='Suppliers')
    packaging_amount_id_line = fields.One2many('packaging.amount','packaging_amount_id', string="Packaging Amount")                    

    total_cost_ht = fields.Float(string='Tot Cost HT', compute='_total_packaging_all')
    total_sales_ht = fields.Float(string='Tot Sales HT', compute='_total_packaging_all')
    total_net_sales_ht = fields.Float(string='Tot Net Sales HT', compute='_total_packaging_all')
    total_profit_ht = fields.Float(string='Tot Profit HT', compute='_total_packaging_all')
    profit = fields.Float(string='%Profit', compute='_total_packaging_all')

    def _total_packaging_all(self):
        for pack in self:
            total_cost_ht = total_sales_ht = total_net_sales_ht = total_profit_ht = profit  = 0.0
            for line in pack.packaging_amount_id_line:
                total_cost_ht += line.s_tot_cost_ht
                total_sales_ht += line.s_tot_sales_ht
                total_net_sales_ht += line.s_tot_net_sale_ht
                total_profit_ht += line.s_profit_ht
                if self.total_net_sales_ht != 0 and self.total_profit_ht != 0:
                    self.profit = self.total_profit_ht / self.total_net_sales_ht
                else:
                    self.profit = 0
            pack.update({
                'total_cost_ht': total_cost_ht,
                'total_sales_ht': total_sales_ht,
                'total_net_sales_ht': total_net_sales_ht,
                'total_profit_ht': total_profit_ht,
                'profit': pack.profit, 

            })

    # qty = fields.Float('Qty')
    # qty_unit = fields.Many2one('packaging.unit')
    # sale_rate_ht_currency = fields.Many2one('res.currency', string='Currency')
    # sale_rate_ht = fields.Float('Sale Rate HT')
    # discount = fields.Float('Discount ')
    # net_sale_rate = fields.Float('Net Sale Rate', compute='_net_sale')
    # net_sale_rate_ht_currency = fields.Many2one('res.currency', string='Currency')
    # profit_ht = fields.Float('Profit HT', compute='_prft_ht')
    # profit_ht_currency = fields.Many2one('res.currency', string='Currency')
    # s_tot_sales_ht = fields.Float('S/Tot Sales HT', compute='_tot_sales_ht')
    # s_tot_sales_currency = fields.Many2one('res.currency', string='Currency')
    # s_tot_cost_ht = fields.Float('S/Tot Cost HT', compute='_tot_cost_ht')
    # s_tot_cost_currency = fields.Many2one('res.currency', string='Currency')
    # s_tot_net_sale_ht = fields.Float('S/Tot Net Sale HT', compute='_tot_net_sale_ht')
    # s_tot_net_sale_currency = fields.Many2one('res.currency', string='Currency')
    # s_profit_ht = fields.Float('S/Tot Profit HT', compute='_tot_profit_ht')
    # s_tot_profit_currency = fields.Many2one('res.currency', string='Currency')
    

    # def _net_sale(self):
    #     self.net_sale_rate = self.sale_rate_ht - (self.sale_rate_ht * self.discount)
    #     return True
   
    # def _prft_ht(self):
    #     self.profit_ht = self.net_sale_rate - self.cost_rate_ht_monet  
    #     return True

    # def _tot_sales_ht(self):
    #     self.s_tot_sales_ht = self.qty * self.sale_rate_ht  
    #     return True    
    
    # def _tot_cost_ht(self):
    #     self.s_tot_cost_ht = self.qty * self.cost_rate_ht_monet  
    #     return True

    # def _tot_net_sale_ht(self):
    #     self.s_tot_net_sale_ht = self.qty * self.net_sale_rate  
    #     return True
 
    # def _tot_profit_ht(self):
    #     self.s_profit_ht = self.qty * self.profit_ht  
    #     return True

    # @api.onchange('sale_rate_ht_currency')
    # def onchange_currency_id(self):
    #     self.net_sale_rate_ht_currency = self.sale_rate_ht_currency
    #     self.profit_ht_currency = self.sale_rate_ht_currency
    #     self.s_tot_sales_currency = self.sale_rate_ht_currency
    #     self.s_tot_cost_currency = self.sale_rate_ht_currency
    #     self.s_tot_net_sale_currency = self.sale_rate_ht_currency
    #     self.s_tot_profit_currency = self.sale_rate_ht_currency
    

class PackagingDivision(models.Model):

    _name = 'packagin.division'
    _rec_name = 'division'

    division  = fields.Text('Division')
    division_n = fields.Char('Division N°')
    division_tag = fields.Text('Division Tag')
    # packagin_department_id = fields.Many2many('packagin.department', 'department_user_rel', 'div_id', 'depart_id', string='Department')
    packagin_department_id = fields.Many2one('packagin.department', string='Department')

class PackagingDepartment(models.Model):

    _name = 'packagin.department'
    _rec_name = 'department'

    department  = fields.Text('Depatment')
    department_n = fields.Char('Department N°')
    department_tag = fields.Text('Department Tag')
    pcl_office = fields.Many2one('res.partner', string="PCL Office")


class PackagingCriteria(models.Model):

    _name = 'packagin.criteria'

    packagin_value_class_id = fields.Many2one('packagin.vclass', string='Value Class')
    packagin_weight_class_id = fields.Many2one('packagin.weghitclass', string='Gross Weight Class')
    packagin_incoterm_id = fields.Many2one('packagin.incoterm', string='Incoterm')
    packagin_volume_class_id = fields.Many2one('packagin.volume', string='Volume Class')
    packagin_cargo_indication_id = fields.Many2one('packagin.cargo.indication', string='Cargo Indication')
    packagin_cargo_specification_id = fields.Many2one('packagin.cargo.specification', string='Cargo Specification')
    packagin_shipping_id = fields.Many2one('packagin.shipping', string='Shipping Packaging')
    packagin_cargo_payment_id = fields.Many2one('cargo.payment', string='Cargo Payment')
    packagin_pod_id = fields.Many2one('packagin.pod', string='POD')
    packagin_pol_id = fields.Many2one('packagin.pol', string='POL')
    packagin_regime_id = fields.Many2one('packagin.regime', string='Regime Type')
    packagin_regime_number_id = fields.Many2one('regime.number', string='Regime Number')
    packagin_added_proceders_id = fields.Many2one('added.proceders', string='Added Proceders')
    packagin_customs_desk_id = fields.Many2one('customs.desk', string='Customs Desk')
    packagin_packaging_processes_id = fields.Many2one('packaging.processes', string='Processes')


class PackagingValueClass(models.Model):

    _name = 'packagin.vclass'
    _rec_name = 'value_class'

    class_numero  = fields.Char('Class N°')
    value_class = fields.Text('Value Class')

class PackagingWeightClass(models.Model):

    _name = 'packagin.weghitclass'
    _rec_name = 'g_weight_class'

    class_numero  = fields.Char('Class N°')
    g_weight_class = fields.Text('Gross Weight Class')

class PackagingIncoterm(models.Model):

    _name = 'packagin.incoterm'
    _rec_name = 'incoterm'

    incoterm_numero  = fields.Char('Incoterm N°')
    incoterm = fields.Text('Incoterm')

class PackagingVolumClass(models.Model):

    _name = 'packagin.volume'
    _rec_name = 'volum_class'

    volum_class_n  = fields.Char('Volume Class N°')
    volum_class = fields.Text('Volume Class')

class PackagingCargoIndication(models.Model):

    _name = 'packagin.cargo.indication'
    _rec_name = 'cargo_indication'

    cargo_indication_n  = fields.Char('Cargo Indication N°')
    cargo_indication = fields.Text('Cargo Indication')

class PackagingCargoSpecification(models.Model):
 
    _name = 'packagin.cargo.specification'
    _rec_name = 'cargo_specification'

    cargo_specification_n  = fields.Char('Cargo Specification N°')
    cargo_specification = fields.Text('Cargo Specification')

class PackagingShipping(models.Model):
 
    _name = 'packagin.shipping'
    _rec_name = 'shipping'

    shippiing_n  = fields.Char('Shipping Packiging N°')
    shipping = fields.Text('Shipping Packiging')

class PackagingCargoPayment(models.Model):
 
    _name = 'cargo.payment'
    _rec_name = 'cargo_payment'

    cargo_payment_n  = fields.Char('Cargo Payment N°')
    cargo_payment = fields.Text('Cargo Payment')

class PackagingPOD(models.Model):
 
    _name = 'packagin.pod'
    _rec_name = 'port'

    port_n  = fields.Char('Port N°')
    port = fields.Text('Port Name')
    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.country.state', string='City')

class PackagingPOL(models.Model):
 
    _name = 'packagin.pol'
    _rec_name = 'port'

    port_n  = fields.Char('Port N°')
    port = fields.Text('Port Name')
    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.country.state', string='City')

class PackagingRegimeCategory(models.Model):
 
    _name = 'regime.category'
    _rec_name = 'regime_category_n'
    
    reg_category  = fields.Char('Régime Category')
    regime_category_n = fields.Text('Régime Category N°')


class PackagingRegimeType(models.Model):
 
    _name = 'packagin.regime'
    _rec_name = 'regime'

    packagin_regime_category_id = fields.Many2one('regime.category', string='Regime Category')
    regime_n  = fields.Char('Regime Type N°')
    regime = fields.Text('Regime Type Name')

class PackagingRegimeNumber(models.Model):
 
    _name = 'regime.number'
    _rec_name = 'regime_description'

    reg_number  = fields.Integer('Régime N°')
    regime_description = fields.Text('Régime Description')

class PackagingAddedProceders(models.Model):
 
    _name = 'added.proceders'
    _rec_name = 'added_proceders'

    added_proceders = fields.Text('Added Proceders')
    added_proceders_n = fields.Char('Added Proceders N°')

class PackagingCustomsDesk(models.Model):
 
    _name = 'customs.desk'
    _rec_name = 'customs_desk'

    customs_desk = fields.Text('Custom Desk')
    customs_desk_n = fields.Char('Custom Desk N°')
    city_id = fields.Many2one('res.country.state', string='City')
    country_id = fields.Many2one('res.country', string='Country')

class ProcessesProcesses(models.Model):
 
    _name = 'processes.processes'
    _rec_name = 'processes_name'

    processes_name = fields.Text('Processes Name')
    processes_n = fields.Char('Processes N°')
    review_n = fields.Integer('Review')
    date = fields.Date('Date')
    processes = fields.Binary('Processes')
    pcl_office = fields.Many2one('res.partner', string="PCL Office")
    department = fields.Selection([
            ('managment', 'Managment'),
            ('commercial', 'Commercial'),
            ('operations', 'Operations'),
            ('logistics', 'Logistics'),
            ('transit', 'Transit'),
            ('support', 'Support'),
            ('accounting', 'Accounting'),
            ('bank', 'Bank'),
            ('rh', 'RH'),
            ('marketing', 'Marketing'),
            ('it', 'IT'),
            ('legal', 'Legal'),   
            ('insurance', 'Insurance'),
            ('infrastructure', 'Infrastructure'),
            ('tools', 'Tools'),
            ], string='Department', default='managment')
    

class PackagingProcesses(models.Model):
 
    _name = 'packaging.processes'
    _rec_name = 'procedure_name'

    packagin_processes_id = fields.Many2one('processes.processes', string='Processes')
    procedure_name = fields.Text('Procedure Name')
    procedure_n = fields.Char('Procedure N°')
    review = fields.Integer('Review')
    date = fields.Date('Date')
    processes = fields.Binary('Processes')
    pcl_office = fields.Many2one('res.partner', string="PCL Office")
    department = fields.Selection([
            ('managment', 'Managment'),
            ('commercial', 'Commercial'),
            ('operations', 'Operations'),
            ('logistics', 'Logistics'),
            ('transit', 'Transit'),
            ('support', 'Support'),
            ('accounting', 'Accounting'),
            ('bank', 'Bank'),
            ('rh', 'RH'),
            ('marketing', 'Marketing'),
            ('it', 'IT'),
            ('legal', 'Legal'),   
            ('insurance', 'Insurance'),
            ('infrastructure', 'Infrastructure'),
            ('tools', 'Tools'),
            ], string='Department', default='managment')
    instruction_name = fields.Text('Instruction Name')
    instruction_n = fields.Char('Instruction N°')
    date = fields.Date('Date')
    instruction = fields.Binary('Instructions Internes')
    
class PackagingUnit(models.Model):
 
    _name = 'packaging.unit'

    name = fields.Char('Unit')

class PackagingVat(models.Model):
 
    _name = 'pack.vat'
    _rec_name = 'vat'

    vat = fields.Float('VAT')
    country_vat_id = fields.Many2one('res.country', string='Country')
    city_vat_id = fields.Many2one('res.country.state', string='City')
    code_auto = fields.Char('Code')

    @api.model
    def create(self, vals):
        vals['code_auto'] = self.env['ir.sequence'].next_by_code('code.auto') or '/'
        return super(PackagingVat, self).create(vals)

class PackagingSection(models.Model):
 
    _name = 'packaging.section'
    _rec_name = 'section_name'

    service_id = fields.Many2one('scope.type', string='Service')
    section_name = fields.Text('Section Name')
    section_translation = fields.Text('Translation')
    section_code = fields.Char('Section Code')
    section_abreviation = fields.Text('Abreviation')

    @api.model
    def create(self, vals):
        vals['section_code'] = self.env['ir.sequence'].next_by_code('section.code') or '/'
        return super(PackagingSection, self).create(vals)

    accounting_number = fields.Char('Accounting N°')
    note_section = fields.Text('Note')
    at_cost = fields.Selection([
            ('yes', 'Yes'),
            ('no', 'No'),
            ('depends', 'Depends'),
            ], string='At Cost', default='yes')
    taxable = fields.Selection([
            ('yes', 'Yes'),
            ('no', 'No'),
            ], string='Taxable', default='yes')
    rt = fields.Selection([
            ('yes', 'Yes'),
            ('no', 'No'),
            ], string='RT', default='yes')
    adf_min = fields.Float('MIN')
    currency_id_adf_min = fields.Many2one('res.currency', string='Currency')
    adf_max = fields.Float('MAX')
    currency_id_adf_max = fields.Many2one('res.currency', string='Currency')
    tarrif_id = fields.Many2one('packaging.tariff', string='Tarrif')
    vat_id = fields.Many2one('pack.vat', string='VAT')
    maximum_discount = fields.Float('Maximum Discount')
    validity_time = fields.Integer('Validity Time')

class PackagingTariff(models.Model):
 
    _name = 'packaging.tariff'
    _rec_name = 'per_name'

    amount_tariff = fields.Float('Amount Tarif')
    currency_id_tariff = fields.Many2one('res.currency', string='Currency tarrif')
    per_name = fields.Text('Per')
    unite_id_tariff = fields.Many2one('packaging.unit', string='Currency')    
    tariff_name = fields.Text('Concern')
    tarrif_from = fields.Char('From')
    currency_id_tariff_from = fields.Many2one('packaging.unit', string='Currency')    
    tarrif_to = fields.Char('To')
    currency_id_tariff_to = fields.Many2one('packaging.unit', string='Currency')        
    min_billing = fields.Float('Minimum Billing')    
    currency_id_min_billing = fields.Many2one('res.currency', string='Currency')
    max_billing = fields.Float('Maximum Billing')    
    currency_id_max_billing = fields.Many2one('res.currency', string='Currency')
    plus_fix = fields.Float('+Fix')    
    currency_id_plus_fix = fields.Many2one('res.currency', string='Currency')
    comments_tarrif = fields.Text('Comments')
    

class PackagingAmount(models.Model):

    _name = 'packaging.amount'

    cost_rate_ht_currency = fields.Many2one('res.currency', string='Currency')
    cost_rate_ht_monet = fields.Float('Cost Rate HT')
    qty = fields.Float('Qty')
    qty_unit = fields.Many2one('packaging.unit')
    sale_rate_ht_currency = fields.Many2one('res.currency', string='Currency')
    sale_rate_ht = fields.Float('Sale Rate HT')
    discount = fields.Float('Discount %')
    net_sale_rate = fields.Float('Net Sale Rate', compute='_amount_in_packaging_all')
    net_sale_rate_ht_currency = fields.Many2one('res.currency', string='Currency')
    profit_ht = fields.Float('Profit HT', compute='_amount_in_packaging_all')
    profit_ht_currency = fields.Many2one('res.currency', string='Currency')
    s_tot_sales_ht = fields.Float('S/Tot Sales HT', compute='_amount_in_packaging_all')
    s_tot_sales_currency = fields.Many2one('res.currency', string='Currency')
    s_tot_cost_ht = fields.Float('S/Tot Cost HT', compute='_amount_in_packaging_all')
    s_tot_cost_currency = fields.Many2one('res.currency', string='Currency')
    s_tot_net_sale_ht = fields.Float('S/Tot Net Sale HT', compute='_amount_in_packaging_all')
    s_tot_net_sale_currency = fields.Many2one('res.currency', string='Currency')
    s_profit_ht = fields.Float('S/Tot Profit HT', compute='_amount_in_packaging_all')
    s_tot_profit_currency = fields.Many2one('res.currency', string='Currency')
    packaging_amount_id = fields.Many2one('scope.type', string="Packaging Amount")
    

    def _amount_in_packaging_all(self):
        for pack in self:
            cost_rate_ht_monet = qty = sale_rate_ht = net_sale_rate = profit_ht = s_tot_sales_ht = s_tot_cost_ht = s_tot_net_sale_ht = s_profit_ht = 0.0 
            for line in pack.packaging_amount_id.packaging_amount_id_line:
                line.net_sale_rate = line.sale_rate_ht - (line.sale_rate_ht * line.discount)
                line.profit_ht = line.net_sale_rate - line.cost_rate_ht_monet
                line.s_tot_sales_ht = line.qty * line.sale_rate_ht
                line.s_tot_cost_ht = line.qty * line.cost_rate_ht_monet
                line.s_tot_sales_ht = line.qty * line.sale_rate_ht
                line.s_tot_net_sale_ht = line.qty * line.net_sale_rate
                line.s_profit_ht = line.qty * line.profit_ht
        pack.update({
                'net_sale_rate': line.net_sale_rate,
                'profit_ht': line.profit_ht,
                's_tot_sales_ht': line.s_tot_sales_ht,
                's_tot_cost_ht': line.s_tot_cost_ht,
                's_tot_sales_ht': line.s_tot_sales_ht,
                's_tot_net_sale_ht': line.s_tot_net_sale_ht,
                's_profit_ht': line.s_profit_ht,
                'net_sale_rate_ht_currency': line.sale_rate_ht_currency,
                'profit_ht_currency': line.sale_rate_ht_currency,
                's_tot_sales_currency': line.sale_rate_ht_currency,
                's_tot_cost_currency': line.sale_rate_ht_currency,
                's_tot_net_sale_currency': line.sale_rate_ht_currency,
                's_tot_profit_currency': line.sale_rate_ht_currency,
            })
    