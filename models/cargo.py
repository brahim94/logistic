# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class cargo(models.Model):

    _name = 'cargo.type'
    _rec_name = 'cargo_references'

    Incoterm = fields.Selection([
            ('exwork', 'ExWork'),
            ('fob', 'FOB'),
            ('fca', 'FCA'),
            ('fas', 'FAS'),
            ('cfr', 'CFR'),
            ('cif', 'CIF'),
            ('cpt', 'CPT'),
            ('cip', 'CIP'),
            ('dat', 'DAT'),
            ('dap', 'DAP'),
            ('dpu', 'DPU'),
            ('ddp', 'DDP'),
            ], string='Incoterm')
    v_incoterm = fields.Selection([
            ('exwork', 'ExWork'),
            ('fob', 'FOB'),
            ('fca', 'FCA'),
            ('fas', 'FAS'),
            ('cfr', 'CFR'),
            ('cif', 'CIF'),
            ('cpt', 'CPT'),
            ('cip', 'CIP'),
            ('dat', 'DAT'),
            ('dap', 'DAP'),
            ('dpu', 'DPU'),
            ('ddp', 'DDP'),
            ('na', 'NA'),
            ], string='V Incoterm')
    
    euro_value = fields.Float(string='Value')
    usd_value = fields.Float(string='USD')
    mad_value = fields.Float(string='Mad')
    
    Value_Class = fields.Selection([
            ('v1', 'Below 2000 mad'),
            ('v2', '2 001 to 10 000 mad'),
            ('v3', '10 001 to 30 000 mad'),
            ('v4', '30 001 to 50 000 mad'),
            ('v5', '50 001 to 100 000 mad'),
            ('v6', '100 001 to 200 000 mad'),
            ('v7', '200 001 to 500 000 mad'),
            ('v8', '500 001 to 1 000 000 mad'),
            ('v9', '1 000 001 to 2 000 000 mad'),
            ('v10', '2 000 001 to 3 000 000 mad'),
            ('v11', '3 000 001 to 5 000 000 mad'),
            ('v12', '5 000 001 to 10 000 000 mad'),
            ('v13', 'Above 10 000 000 mad'),
            ], string='Value Class')
    
    kg_value = fields.Integer('Kg')
    ton_value = fields.Integer('Ton')
    ibs_value = fields.Integer('lbs')
    
    gross_weight_class = fields.Selection([
            ('g1', 'Below 3 Kg'),
            ('g2', '3-10 Kg'),
            ('g3', '11-20 Kg'),
            ('g4', '21-50 Kg'),
            ('g5', '51-75 Kg'),
            ('g6', '76-99 Kg'),
            ('g7', '100-199 Kg'),
            ('g8', '200-299 Kg'),
            ('g9', '300-399 Kg'),
            ('g10', '400-499 Kg'),
            ('g11', '500-599 Kg'),
            ('g12', '600-850 Kg'),
            ('g13', '850-1000 Kg'),
            ('g14', '1t<...=<5t'),
            ('g15', '5t<...=<10t'),
            ('g16', '10t<....=<30t'),
            ('g17', '30t<....=<100t'),
            ('g18', '100t<....=<200t'),
            ('g19', '200t<......=<500t'),
            ('g20', '500t<.......=<1000t'),
            ('g21', '>1000t'),
            ], string='Gross Weight Class')
    
    ccm_value = fields.Integer('ccm')
    cbm_value = fields.Integer('cbm')
    cinch_value = fields.Integer('cinch')
    cfeet_value = fields.Integer('cfeet')

    volume_class = fields.Selection([
            ('c1', 'Below 250 ccm'),
            ('c2', '251-500 ccm'),
            ('c3', '501-1000 ccm'),
            ('c4', '1001-2000 ccm'),
            ('c5', '2001-4000 ccm'),
            ('c6', '4001-10 000 ccm'),
            ('c7', '10 001-100 000 ccm'),
            ('c8', '100 001-1 000 000 ccm'),
            ('c9', '1<....=<5cbm'),
            ('c10', '5<....=<10 cbm'),
            ('c11', '10<.....=<30 cbm'),
            ('c12', '30<.....=<50 cbm'),
            ('c13', '50<.....=<100 cbm'),
            ('c14', '100<...=<200 cbm'),
            ('c15', '200<...=<500 cbm'),
            ('c16', '500<....=<1 000 cbm'),
            ('c17', '1 000<....=<10 000 cbm'),
            ('c18', '10 000<....=<20 000 cbm'),
            ('c19', '20 000<......=<50 000 cbm'),
            ('c20', '50 000<.......=<100 000 cbm'),
            ('c21', '>100 000 cbm'),
            ], string='Volume Class')
    
    cargo_description = fields.Text('Cargo Description')
    cargo_references = fields.Char('Cargo References')
    new = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('used', 'Used'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='New')

    dangereux = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Dangereux')

    flammable = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Flammable')

    stackable = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Stackable')

    forkliftable = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Forkliftable')

    rolling_machine = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Rolling machine')
    
    self_proppled = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Self-proppled')

    Can_loaded = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Can be loaded on the weather deck')

    keep_dry = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Keep dry')

    keep_sec = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Keep dry')

    delicate = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Delicate')

    Vaulable = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Vaulable')

    humidity_sensitive = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Humidity sensitive')

    temperature_sensitive = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Temperature sensitive')

    perishable = fields.Selection([
            ('some', 'Some'),
            ('all', 'All'),
            ('no', 'No'),
            ('na', 'NA'),
            ('dk', 'DK'),
            ], string='Perishable', default='no')

    some = fields.Selection([
            ('frais', 'Frais'),
            ('congelé', 'Congelé'),
            ('sugelé', 'Surgelé'),
            ], string='All')

    all_selection = fields.Selection([
            ('frais', 'Frais'),
            ('congelé', 'Congelé'),
            ('sugelé', 'Surgelé'),
            ], string='Some')

    type_celsisu = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu')
    
    celsius = fields.Char('C°')

    cargo_payment = fields.Selection([
            ('with', 'With payment'),
            ('no', 'No payment'),
            ('dk', 'DK'),
            ], string='Cargo payment')
    
    with_payment = fields.Selection([
            ('no_condition', 'No conditions'),
            ('cad', 'CAD'),
            ('lc', 'LC'),
            ('other_condition', 'Other condition'),
            ('combined', 'Combined'),
            ('dk', 'DK'),
            ], string='With payment')
    no_payment = fields.Boolean(string='No Payment', default=False)
    other_conditions = fields.Text('Other condition')
    no = fields.Boolean(string='No', default=False)
    na = fields.Boolean(string='NA', default=False)
    dk = fields.Boolean(string='DK', default=False)
    #total_ids = fields.One2many('total.quantity','total_id', string='Total Quantity')
    #indication_ids = fields.One2many('cargo.indication','indication_id', string='Cargo indication')
    #packaging_ids = fields.One2many('shipping.packaging','packaging_id', string='Shipping packaging')
    #cargo_packaging_ids = fields.One2many('cargo.packaging','cargo_packaging_id', string='Cargo packaging')
    currency_unit = fields.Selection([
            ('euro', 'Euro'),
            ('usd', 'USD'),
            ('mad', 'MAD'),
            ], setting='currency', default='euro')
    weight_unit = fields.Selection([
            ('kg', 'Kg'),
            ('ton', 'Ton'),
            ('ibs', 'Ibs'),
            ], setting='Weight unit', default='kg')
    volume_unit = fields.Selection([
            ('ccm', 'Ccm'),
            ('cbm', 'Cbm'),
            ('cinh', 'Cinh'),
            ('cfeet', 'Cfeet'),
            ], setting='Volume unit', default='ccm')

#     @api.constrains('indication_ids')
#     def _check_indication_ids(self):
#             if len(self.indication_ids.ids) > 1:
#                     raise ValidationError(_('Warning! You cannot add multiple lines.'))

    teus = fields.Integer(string='Teus')
    unit = fields.Integer(string="Unit")
    up = fields.Integer(string="UP")
    ft = fields.Integer(string='FT')
    fkg = fields.Integer(string='FKG')
    cbm = fields.Integer(string='CBM')
    wm = fields.Integer(string='WM')
    truck = fields.Integer(string='Truck')
    mafi = fields.Integer(string='Mafi')
    trailer = fields.Integer(string='Trailer')
    file_id = fields.Integer(string='File')
    shipment = fields.Integer(string='Shipment')
#     Qty = fields.Integer('Qty')
#     total_id = fields.Many2one('cargo.type', string="Total ID")
                
# class Total_Quantity(models.Model):

#     _name = 'total.quantity'

#     teus = fields.Char(string='Teus')
#     unit = fields.Char(string="Unit")
#     up = fields.Char(string="UP")
#     ft = fields.Char(string='FT')
#     fkg = fields.Char(string='FKG')
#     cbm = fields.Char(string='CBM')
#     wm = fields.Char(string='WM')
#     truck = fields.Char(string='Truck')
#     mafi = fields.Char(string='Mafi')
#     trailer = fields.Char(string='Trailer')
#     file_id = fields.Char(string='File')
#     shipment = fields.Char(string='Shipment')
#     Qty = fields.Integer('Qty')
#     total_id = fields.Many2one('cargo.type', string="Total ID")

    motor_vehicule = fields.Boolean(string='Motor vehicule', default=False)
    steel_griders = fields.Boolean(string="Steel griders", default=False)
    wood = fields.Boolean(string="wood", default=False)
    machines = fields.Boolean(string='Machines', default=False)
    transformers = fields.Boolean(string='Transformers', default=False)
    animals = fields.Boolean(string='Animals', default=False)
    spare_parts = fields.Boolean(string='Spare parts', default=False)
    tools = fields.Boolean(string='Tools', default=False)
    consumable = fields.Boolean(string='Consumable', default=False)
    medecine = fields.Boolean(string='Medecine', default=False)
    books = fields.Boolean(string='Books', default=False)
    cosmetics = fields.Boolean(string='Cosmetics', default=False)
    furinture = fields.Boolean('Furinture', default=False)
    electronic = fields.Boolean(string='Electronic', default=False)
    food = fields.Boolean(string='Food', default=False)
    textile = fields.Boolean('Textile', default=False)
    agricultural_products = fields.Boolean(string='Agricultural products', default=False)
    agricultural_machines = fields.Boolean(string='Agricultural machines', default=False)
    vegetables = fields.Boolean('Vegetables', default=False)
    fruits = fields.Boolean(string='Fruits', default=False)
    health = fields.Boolean(string='Health', default=False)
    equipment = fields.Boolean(string='Equipment', default=False)
    it = fields.Boolean(string='IT', default=False)
    leather = fields.Boolean(string='Leather', default=False)
    oil = fields.Boolean(string='Oil', default=False)
    personal_effects = fields.Boolean(string='Personal effects', default=False)
    plants = fields.Boolean(string='Plants', default=False)
    pipes = fields.Boolean(string='Pipes', default=False)
    plastics = fields.Boolean(string='Plastics', default=False)
    gas = fields.Boolean(string='Gas', default=False)
    toys_and_games = fields.Boolean(string='Toys and games', default=False)
    wires_and_cables = fields.Boolean(string='Wires & Cables', default=False)
    sanitary = fields.Boolean(string='Sanitary', default=False)
    industrial_products = fields.Boolean(string='Industrial products', default=False)
    auto_parts = fields.Boolean(string='Auto parts', default=False)
    cleaning_products = fields.Boolean(string='Cleaning products', default=False)
    
    container = fields.Integer(string='Container')
    house_removal = fields.Integer(string="House Removal")
    enveloppe = fields.Integer(string="Enveloppe")
    large_enveloppe = fields.Integer(string='Large enveloppe')
    passenger_luggage = fields.Integer(string='Passenger luggage')
    cardboard_boxes = fields.Integer(string='Cardboard boxes')
    tube = fields.Integer(string='Tube')
    crates = fields.Integer(string='Crates')
    wooden_boxes = fields.Integer(string='Wooden Boxes')
    metal_boxes = fields.Integer(string='Metal boxes')
    barrels = fields.Integer(string='Barrels')
    pallets = fields.Integer(string='Pallets')
    big_bag = fields.Integer('Big Bag')
    bundle = fields.Integer('Bundle')
    drums = fields.Integer('Drums')
    bales = fields.Integer('Bales')
    shipping_sacks = fields.Integer('Shipping Sacks')
    Qty = fields.Integer('Qty')

    container_crg_packaging = fields.Integer(string='Container')
    house_removal_crg_packaging = fields.Integer(string="House Removal")
    passenger_luggage_crg_packaging = fields.Integer(string='Passenger luggage')
    cardboard_boxes_crg_packaging = fields.Integer(string='Cardboard boxes')
    crates_crg_packaging = fields.Integer(string='Crates')
    large_enveloppe_crg_packaging = fields.Integer(string='Large enveloppe')
    wooden_boxes_crg_packaging = fields.Integer(string='Wooden Boxes')
    metal_boxes_crg_packaging = fields.Integer(string='Metal boxes')
    barrels_crg_packaging = fields.Integer(string='Barrels')
    pallets_crg_packaging = fields.Integer(string='Pallets')
    big_bag_crg_packaging = fields.Integer('Big Bag')
    bundle_crg_packaging = fields.Integer('Bundle')
    drums_crg_packaging = fields.Integer('Drums')
    bales_crg_packaging = fields.Integer('Bales')
    shipping_sacks_crg_packaging = fields.Integer('Shipping Sacks')
    currency_id = fields.Many2one('res.currency', string='Currency')
# class Shipping_packaging(models.Model):

#     _name = 'shipping.packaging'

#     container = fields.Char(string='Container')
#     house_removal = fields.Char(string="House Removal")
#     enveloppe = fields.Char(string="Enveloppe")
#     large_enveloppe = fields.Char(string='Large enveloppe')
#     passenger_luggage = fields.Char(string='Passenger luggage')
#     cardboard_boxes = fields.Char(string='Cardboard boxes')
#     tube = fields.Char(string='Tube')
#     crates = fields.Char(string='Crates')
#     wooden_boxes = fields.Char(string='Wooden Boxes')
#     metal_boxes = fields.Char(string='Metal boxes')
#     barrels = fields.Char(string='Barrels')
#     pallets = fields.Char(string='Pallets')
#     big_bag = fields.Char('Big Bag')
#     bundle = fields.Char('Bundle')
#     drums = fields.Char('Drums')
#     bales = fields.Char('Bales')
#     shipping_sacks = fields.Char('Shipping Sacks')
#     Qty = fields.Integer('Qty')
#     packaging_id = fields.Many2one('cargo.type', string="Packaging ID")

    

# class Cargo_indication(models.Model):

#     _name = 'cargo.indication'

#     motor_vehicule = fields.Boolean(string='Motor vehicule', default=False)
#     steel_griders = fields.Boolean(string="Steel griders", default=False)
#     wood = fields.Boolean(string="wood", default=False)
#     machines = fields.Boolean(string='Machines', default=False)
#     transformers = fields.Boolean(string='Transformers', default=False)
#     animals = fields.Boolean(string='Animals', default=False)
#     spare_parts = fields.Boolean(string='Spare parts', default=False)
#     tools = fields.Boolean(string='Tools', default=False)
#     consumable = fields.Boolean(string='Consumable', default=False)
#     medecine = fields.Boolean(string='Medecine', default=False)
#     books = fields.Boolean(string='Books', default=False)
#     cosmetics = fields.Boolean(string='Cosmetics', default=False)
#     furinture = fields.Boolean('Furinture', default=False)
#     electronic = fields.Boolean(string='Electronic', default=False)
#     food = fields.Boolean(string='Food', default=False)
#     textile = fields.Boolean('Textile', default=False)
#     agricultural_products = fields.Boolean(string='Agricultural products', default=False)
#     agricultural_machines = fields.Boolean(string='Agricultural machines', default=False)
#     vegetables = fields.Boolean('Vegetables', default=False)
#     fruits = fields.Boolean(string='Fruits', default=False)
#     health = fields.Boolean(string='Health', default=False)
#     equipment = fields.Boolean(string='Equipment', default=False)
#     it = fields.Boolean(string='IT', default=False)
#     leather = fields.Boolean(string='Leather', default=False)
#     oil = fields.Boolean(string='Oil', default=False)
#     personal_effects = fields.Boolean(string='Personal effects', default=False)
#     plants = fields.Boolean(string='Plants', default=False)
#     pipes = fields.Boolean(string='Pipes', default=False)
#     plastics = fields.Boolean(string='Plastics', default=False)
#     gas = fields.Boolean(string='Gas', default=False)
#     toys_and_games = fields.Boolean(string='Toys and games', default=False)
#     wires_and_cables = fields.Boolean(string='Wires & Cables', default=False)
#     sanitary = fields.Boolean(string='Sanitary', default=False)
#     industrial_products = fields.Boolean(string='Industrial products', default=False)
#     auto_parts = fields.Boolean(string='Auto parts', default=False)
#     cleaning_products = fields.Boolean(string='Cleaning products', default=False)
#     indication_id = fields.Many2one('cargo.type', string="indication ID")

class Cargo_packaging(models.Model):

    _name = 'cargo.packaging'

    container = fields.Char(string='Container')
    house_removal = fields.Char(string="House Removal")
    passenger_luggage = fields.Char(string='Passenger luggage')
    cardboard_boxes = fields.Char(string='Cardboard boxes')
    crates = fields.Char(string='Crates')
    large_enveloppe = fields.Char(string='Large enveloppe')
    wooden_boxes = fields.Char(string='Wooden Boxes')
    metal_boxes = fields.Char(string='Metal boxes')
    barrels = fields.Char(string='Barrels')
    pallets = fields.Char(string='Pallets')
    big_bag = fields.Char('Big Bag')
    bundle = fields.Char('Bundle')
    drums = fields.Char('Drums')
    bales = fields.Char('Bales')
    shipping_sacks = fields.Char('Shipping Sacks')
    cargo_packaging_id = fields.Many2one('cargo.type', string="Cargo Packaging ID")
 