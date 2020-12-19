# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class ModeTransport(models.Model):

    _name = 'transport.mode'
    _rec_name = 'transport_mode'

#     passenger_luggage = fields.Char('Passenger luggage')
#     postal_parcel = fields.Char('Postal Parcel')
#     bulk = fields.Char('Bulk')
#     bulk_liquid = fields.Char('Bulk liquid')
    directory_id = fields.Many2one('directory.type', 'Directory ID')
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
            ], setting='Mode of Transport', related="directory_id.transport_mode")
    mode_transport_as_line = fields.One2many('transport.as','mode_transport_as_id', string="Mode Transport AS")        
    mode_transport_lcl_line = fields.One2many('transport.lcl','mode_transport_lcl_id', string="Mode Transport LCL")        
    mode_transport_fcl_line = fields.One2many('transport.fcl','mode_transport_fcl_id', string="Mode Transport FCL")            
    mode_transport_ltl_line = fields.One2many('transport.ltl','mode_transport_ltl_id', string="Mode Transport LTL")                
    total_qty_as = fields.Float(string='Total Qty', compute='_total_as_all')
    total_gross_weight = fields.Float(string='Total Gross Weight(Kg)', compute='_total_as_all')
    total_volume_cbm = fields.Float(string='Total Volume (cbm)', compute='_total_as_all')
    total_surface = fields.Float(string='Total Surface (m²)', compute='_total_as_all')
    total_chargeable_weight = fields.Float(string='Total Chargeable Weight(Kg)', compute='_total_as_all')

    def _total_as_all(self):
        for order in self:
            total_qty_as = total_gross_weight = total_volume_cbm = total_volume_cbm = total_surface = total_chargeable_weight = 0.0
            for line in order.mode_transport_as_line:
                total_qty_as += line.qty_as
                total_gross_weight += line.s_total_gross_weight
                total_volume_cbm += line.volume_as_id
                total_surface += line.surface
                total_chargeable_weight += line.s_total_chargeable_weight
            order.update({
                'total_qty_as': total_qty_as,
                'total_gross_weight': total_gross_weight,
                'total_volume_cbm': total_volume_cbm,
                'total_surface': total_surface,
                'total_chargeable_weight': total_chargeable_weight, 

            })

    total_qty_lcl = fields.Float(string='Total Qty', compute='_total_lcl_all')
    total_gross_weight_lcl = fields.Float(string='Total Gross Weight(Kg)', compute='_total_lcl_all')
    total_volume_cbm_lcl = fields.Float(string='Total Volume (cbm)', compute='_total_lcl_all')
    total_surface_lcl = fields.Float(string='Total Surface (m²)', compute='_total_lcl_all')
    total_chargeable_weight_lcl = fields.Float(string='Total Chargeable Weight(Kg)', compute='_total_lcl_all')

    def _total_lcl_all(self):
        for order in self:
            total_qty_lcl = total_gross_weight_lcl = total_volume_cbm_lcl = total_surface_lcl = total_chargeable_weight_lcl  = 0.0
            for line in order.mode_transport_lcl_line:
                total_qty_lcl += line.qty_lcl
                total_gross_weight_lcl += line.s_total_gross_weight_lcl
                total_volume_cbm_lcl += line.volume_lcl_id
                total_surface_lcl += line.surface_lcl
                total_chargeable_weight_lcl += line.s_total_chargeable_weight_lcl
            order.update({
                'total_qty_lcl': total_qty_lcl,
                'total_gross_weight_lcl': total_gross_weight_lcl,
                'total_volume_cbm_lcl': total_volume_cbm_lcl,
                'total_surface_lcl': total_surface_lcl,
                'total_chargeable_weight_lcl': total_chargeable_weight_lcl, 

            })

    total_qty_ltl = fields.Float(string='Total Qty', compute='_total_ltl_all')
    total_gross_weight_ltl = fields.Float(string='Total Gross Weight(Kg)', compute='_total_ltl_all')
    total_volume_cbm_ltl = fields.Float(string='Total Volume (cbm)', compute='_total_ltl_all')
    total_surface_ltl = fields.Float(string='Total Surface (m²)', compute='_total_ltl_all')
    total_chargeable_weight_ltl = fields.Float(string='Total Chargeable Weight(Kg)', compute='_total_ltl_all')

    def _total_ltl_all(self):
        for order in self:
            total_qty_ltl = total_gross_weight_ltl = total_volume_cbm_ltl = total_surface_ltl = total_chargeable_weight_ltl  = 0.0
            for line in order.mode_transport_ltl_line:
                total_qty_ltl += line.qty_ltl
                total_gross_weight_ltl += line.s_total_gross_weight_ltl
                total_volume_cbm_ltl += line.volume_ltl_id
                total_surface_ltl += line.surface_ltl
                total_chargeable_weight_ltl += line.s_total_chargeable_weight_ltl
            order.update({
                'total_qty_ltl': total_qty_ltl,
                'total_gross_weight_ltl': total_gross_weight_ltl,
                'total_volume_cbm_ltl': total_volume_cbm_ltl,
                'total_surface_ltl': total_surface_ltl,
                'total_chargeable_weight_ltl': total_chargeable_weight_ltl, 

            })

    tweenty_reefer = fields.Boolean("20'Reefer")
    tweenty_reefer_qty = fields.Integer("Qty")
    tweenty_reefer_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu')
    tweenty_reefer_temperature = fields.Integer("temperature")
    fourty_reefer = fields.Boolean("40'Reefer")
    fourty_reefer_qty = fields.Integer("Qty")
    fourty_reefer_temperature = fields.Integer("temperature")
    fourty_reefer_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu')
    fourty_five_reefer = fields.Boolean("45'Reefer")
    fourty_five_reefer_qty = fields.Integer("Qty")
    fourty_five_reefer_temp = fields.Integer("Temp")
    fourty_five_reefer_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu')
    fourty_hc_reefer = fields.Boolean("40'Reefer HC")
    fourty_hc_reefer_qty = fields.Integer("Qty") 
    fourty_hc_reefer_temp = fields.Integer("Temperature")
    fourty_hc_reefer_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu') 
    fourty_five_reefer_hc = fields.Boolean("45'Reefer HC")
    fourty_five_reefer_hc_qty = fields.Integer("Qty")
    fourty_five_reefer_hc_temp = fields.Integer("Temp")
    fourty_five_reefer_hc_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu') 
    tweenty_reefer_soc = fields.Boolean("20' Reefer SOC")
    tweenty_reefer_soc_qty = fields.Integer("Qty")
    tweenty_reefer_soc_temp = fields.Integer("Temp")
    tweenty_reefer_soc_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu') 
    fourty_reefer_soc = fields.Boolean("40' Reefer SOC")
    fourty_reefer_soc_qty = fields.Integer("Qty")
    fourty_reefer_soc_temp = fields.Integer("Temp")
    fourty_reefer_soc_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu')
    fourty_five_reefer_soc = fields.Boolean("45' Reefer SOC")
    fourty_five_reefer_soc_qty = fields.Integer("Qty")
    fourty_five_reefer_soc_temp = fields.Integer("temp")
    fourty_five_reefer_soc_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu')
    fourty_reefer_hc_soc = fields.Boolean("45' Reefer HC SOC")
    fourty_reefer_hc_soc_qty = fields.Integer("Qty")
    fourty_reefer_hc_soc_temp = fields.Integer("Temp")
    fourty_reefer_hc_soc_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu')
    fourty_five_reefer_hc_soc = fields.Boolean("45' Reefer HC SOC")
    fourty_five_reefer_hc_soc_qty = fields.Integer("Qty")
    fourty_five_reefer_hc_soc_temp = fields.Integer("temp")
    fourty_five_reefer_hc_soc_selec = fields.Selection([
            ('plus', 'Plus'),
            ('minus', 'Minus'),
            ], string='type_celsisu')
    
    box = fields.Boolean('Box')
    box_qty = fields.Integer('Qty')
    side_wall = fields.Boolean('Side wall')
    sid_wall_qty = fields.Integer('Qty')
    curtain = fields.Boolean('Curtain')
    curtain_qty = fields.Integer('Qty')
    flatbed = fields.Boolean('Flatbed')
    flatbed_qty = fields.Integer('Qty')
    reefer = fields.Boolean('Reefer')
    reefer_qty = fields.Integer('Qty')
    oog_activ = fields.Boolean('OOG')
    oog = fields.Selection([
            ('true', 'True'),
            ('top_length', 'Top Length /u'),
            ('top_width', 'Top Width /u'),
            ('top_height', 'Top Height /u'),
            ('top_g_weight', 'Top G Weight /u'),
            ], string='True')
    oog_qty = fields.Integer('OOG')
    top_leng = fields.Selection([
            ('bb', 'BB: =< 12m'),
            ('ol_one', 'OL1: 12m<....=<15m'),
            ('ol_two', 'OL2: 15m<....=<20m'),
            ('ol_three', 'OL3: 20m<....=<25m'),
            ('ol_four', 'OL4: 25m<.....=<30m'),
            ('ol_five', 'OL5: >30m'),
            ], string='Top Length /u')
    top_width = fields.Selection([
            ('bb', 'BB: =< 2,5m'),
            ('ow_one', 'OW1: 2,5m<....=<3m'),
            ('ow_two', 'OW2: 3m<....=<4m'),
            ('ow_three', 'OW3: 4m<....=<5m'),
            ('ow_four', 'OW4: 5m<.....=<6m'),
            ('ow_five', 'OW5: >6m'),
            ], string='Top Width /u')
    top_heigh = fields.Selection([
            ('bb', 'BB: =< 2,9m'),
            ('oh_one', 'OH1: 2,9m<....=<3,5m'),
            ('oh_two', 'OH2: 3,5m<....=<4m'),
            ('oh_three', 'OH3: 4m<.....=<5m'),
            ('oh_four', 'OH4: 5m<.....=<6m'),
            ('oh_five', 'OH5: >6m'),
            ], string='Top Height /u')
    top_g_wei = fields.Selection([
            ('bb', 'BB: =<20t'),
            ('oh_one', 'HL1: 20t<....=<30t'),
            ('oh_two', 'HL2: 30t<....=<48t'),
            ('oh_three', 'HL3: 48t<......=<55t'),
            ('oh_four', 'HL4: 55t<.......=<72t'),
            ('oh_five', 'HL5: >72t'),
            ], string='Top G Weight /u')

    treus = fields.Selection([
            ('bb', 'TREU1: =< 1'),
            ('ol_one', 'TREU2: 1<....=<3'),
            ('ol_two', 'TREU3: 3<....=<10'),
            ('ol_three', 'TREU4: 10<....=<20'),
            ('ol_four', 'TREU5: 20<.....=<30'),
            ('ol_five', 'TREU6: >30'),
            ], string='TREUs')
    top_leng_lolo = fields.Selection([
            ('bb', 'BB: =< 12m'),
            ('ol_one', 'OL1: 12m<....=<15m'),
            ('ol_two', 'OL2: 15m<....=<20m'),
            ('ol_three', 'OL3: 20m<....=<25m'),
            ('ol_four', 'OL4: 25m<.....=<30m'),
            ('ol_five', 'OL5: >30m'),
            ], string='Top Length /u')
    top_width_lolo = fields.Selection([
            ('bb', 'BB: =< 2,5m'),
            ('ow_one', 'OW1: 2,5m<....=<3m'),
            ('ow_two', 'OW2: 3m<....=<4m'),
            ('ow_three', 'OW3: 4m<....=<5m'),
            ('ow_four', 'OW4: 5m<.....=<6m'),
            ('ow_five', 'OW5: >6m'),
            ], string='Top Width /u')
    top_heigh_lolo = fields.Selection([
            ('bb', 'BB: =< 2,9m'),
            ('oh_one', 'OH1: 2,9m<....=<3,5m'),
            ('oh_two', 'OH2: 3,5m<....=<4m'),
            ('oh_three', 'OH3: 4m<.....=<5m'),
            ('oh_four', 'OH4: 5m<.....=<6m'),
            ('oh_five', 'OH5: >6m'),
            ], string='Top Height /u')
    top_g_wei_lolo = fields.Selection([
            ('bb', 'BB: =<20t'),
            ('oh_one', 'HL1: 20t<....=<30t'),
            ('oh_two', 'HL2: 30t<....=<48t'),
            ('oh_three', 'HL3: 48t<......=<55t'),
            ('oh_four', 'HL4: 55t<.......=<72t'),
            ('oh_five', 'HL5: >72t'),
            ], string='Top G Weight /u')

    mafi = fields.Selection([
            ('all_mafi', 'All Mafi'),
            ('some_on_mafi', 'Some on Mafi'),
            ('no', 'No'),
            ('dk', 'DK'),
            ], string='Mafi')
    treus_mafi = fields.Selection([
            ('bb', 'TREU1: =< 1'),
            ('ol_one', 'TREU2: 1<....=<3'),
            ('ol_two', 'TREU3: 3<....=<10'),
            ('ol_three', 'TREU4: 10<....=<20'),
            ('ol_four', 'TREU5: 20<.....=<30'),
            ('ol_five', 'TREU6: >30'),
            ], string='TREUs')
    top_leng_roro = fields.Selection([
            ('bb', 'BB: =< 12m'),
            ('ol_one', 'OL1: 12m<....=<15m'),
            ('ol_two', 'OL2: 15m<....=<20m'),
            ('ol_three', 'OL3: 20m<....=<25m'),
            ('ol_four', 'OL4: 25m<.....=<30m'),
            ('ol_five', 'OL5: >30m'),
            ], string='Top Length /u')
    top_width_roro = fields.Selection([
            ('bb', 'BB: =< 2,5m'),
            ('ow_one', 'OW1: 2,5m<....=<3m'),
            ('ow_two', 'OW2: 3m<....=<4m'),
            ('ow_three', 'OW3: 4m<....=<5m'),
            ('ow_four', 'OW4: 5m<.....=<6m'),
            ('ow_five', 'OW5: >6m'),
            ], string='Top Width /u')
    top_heigh_roro = fields.Selection([
            ('bb', 'BB: =< 2,9m'),
            ('oh_one', 'OH1: 2,9m<....=<3,5m'),
            ('oh_two', 'OH2: 3,5m<....=<4m'),
            ('oh_three', 'OH3: 4m<.....=<5m'),
            ('oh_four', 'OH4: 5m<.....=<6m'),
            ('oh_five', 'OH5: >6m'),
            ], string='Top Height /u')
    top_g_wei_roror = fields.Selection([
            ('bb', 'BB: =<20t'),
            ('oh_one', 'HL1: 20t<....=<30t'),
            ('oh_two', 'HL2: 30t<....=<45t'),
            ('oh_three', 'HL3: 48t<......=<55t'),
            ('oh_four', 'HL4: 55t<.......=<72t'),
            ('oh_five', 'HL5: >72t'),
            ], string='Top G Weight /u')

    
    treus_charted = fields.Selection([
            ('bb', 'TREU1: =< 1'),
            ('ol_one', 'TREU2: 1<....=<3'),
            ('ol_two', 'TREU3: 3<....=<10'),
            ('ol_three', 'TREU4: 10<....=<20'),
            ('ol_four', 'TREU5: 20<.....=<30'),
            ('ol_five', 'TREU6: >30'),
            ], string='TREUs')
    top_leng_charted = fields.Selection([
            ('bb', 'BB: =< 12m'),
            ('ol_one', 'OL1: 12m<....=<15m'),
            ('ol_two', 'OL2: 15m<....=<20m'),
            ('ol_three', 'OL3: 20m<....=<25m'),
            ('ol_four', 'OL4: 25m<.....=<30m'),
            ('ol_five', 'OL5: >30m'),
            ], string='Top Length /u')
    top_width_charted = fields.Selection([
            ('bb', 'BB: =< 2,5m'),
            ('ow_one', 'OW1: 2,5m<....=<3m'),
            ('ow_two', 'OW2: 3m<....=<4m'),
            ('ow_three', 'OW3: 4m<....=<5m'),
            ('ow_four', 'OW4: 5m<.....=<6m'),
            ('ow_five', 'OW5: >6m'),
            ], string='Top Width /u')
    top_heigh_charted = fields.Selection([
            ('bb', 'BB: =< 2,9m'),
            ('oh_one', 'OH1: 2,9m<....=<3,5m'),
            ('oh_two', 'OH2: 3,5m<....=<4m'),
            ('oh_three', 'OH3: 4m<.....=<5m'),
            ('oh_four', 'OH4: 5m<.....=<6m'),
            ('oh_five', 'OH5: >6m'),
            ], string='Top Height /u')
    top_g_wei_charted = fields.Selection([
            ('bb', 'BB: =<20t'),
            ('oh_one', 'HL1: 20t<....=<30t'),
            ('oh_two', 'HL2: 30t<....=<45t'),
            ('oh_three', 'HL3: 48t<......=<55t'),
            ('oh_four', 'HL4: 55t<.......=<72t'),
            ('oh_five', 'HL5: >72t'),
            ], string='Top G Weight /u')

    treus_aircraft = fields.Selection([
            ('bb', 'TREU1: =< 1'),
            ('ol_one', 'TREU2: 1<....=<3'),
            ('ol_two', 'TREU3: 3<....=<10'),
            ('ol_three', 'TREU4: 10<....=<20'),
            ('ol_four', 'TREU5: 20<.....=<30'),
            ('ol_five', 'TREU6: >30'),
            ], string='TREUs')
    top_leng_aircraft = fields.Selection([
            ('bb', 'BB: =< 12m'),
            ('ol_one', 'OL1: 12m<....=<15m'),
            ('ol_two', 'OL2: 15m<....=<20m'),
            ('ol_three', 'OL3: 20m<....=<25m'),
            ('ol_four', 'OL4: 25m<.....=<30m'),
            ('ol_five', 'OL5: >30m'),
            ], string='Top Length /u')
    top_width_aircraft = fields.Selection([
            ('bb', 'BB: =< 2,5m'),
            ('ow_one', 'OW1: 2,5m<....=<3m'),
            ('ow_two', 'OW2: 3m<....=<4m'),
            ('ow_three', 'OW3: 4m<....=<5m'),
            ('ow_four', 'OW4: 5m<.....=<6m'),
            ('ow_five', 'OW5: >6m'),
            ], string='Top Width /u')
    top_heigh_aircraft = fields.Selection([
            ('bb', 'BB: =< 2,9m'),
            ('oh_one', 'OH1: 2,9m<....=<3,5m'),
            ('oh_two', 'OH2: 3,5m<....=<4m'),
            ('oh_three', 'OH3: 4m<.....=<5m'),
            ('oh_four', 'OH4: 5m<.....=<6m'),
            ('oh_five', 'OH5: >6m'),
            ], string='Top Height /u')
    top_g_wei_aircraft = fields.Selection([
            ('bb', 'BB: =<20t'),
            ('oh_one', 'HL1: 20t<....=<30t'),
            ('oh_two', 'HL2: 30t<....=<45t'),
            ('oh_three', 'HL3: 48t<......=<55t'),
            ('oh_four', 'HL4: 55t<.......=<72t'),
            ('oh_five', 'HL5: >72t'),
            ], string='Top G Weight /u')
    
    tweenty_active = fields.Boolean("20'")
    tweenty = fields.Integer("20'")
    tweenty_ot_active = fields.Boolean("20' OT")    
    tweenty_ot = fields.Integer("20' OT")
    tweenty_fr_active = fields.Boolean("20' FR")
    tweenty_fr = fields.Integer("20' FR")
    fourty_active = fields.Boolean("40'")
    fourty = fields.Integer("40'")
    fourty_hc_active = fields.Boolean("40' HC")
    fourty_hc = fields.Integer("40' HC")
    fourty_ot_active = fields.Boolean("40' OT")
    fourty_ot = fields.Integer("40' OT")
    fourty_fr_active = fields.Boolean("40' FR")
    fourty_fr = fields.Integer("40' FR")
    fourty_pw_active = fields.Boolean("40' PW")
    fourty_pw = fields.Integer("40' PW")
    fourty_hc_pw_active = fields.Boolean("40' HC PW")
    fourty_hc_pw = fields.Integer("40' HC PW")
    fourty_five_active = fields.Boolean("45'")
    fourty_five = fields.Integer("45'")
    tweenty_fr_og_active = fields.Boolean("20' FR OOG")
    tweenty_fr_og = fields.Integer("20' FR OOG")
    tweenty_ot_oog_active = fields.Boolean("20' OT OOG")
    tweenty_ot_oog = fields.Integer("20' OT OOG")
    fourty_ot_oog_active = fields.Boolean("40' OT OOG")
    fourty_ot_oog = fields.Integer("40' OT OOG")
    fourty_fr_oog_active = fields.Boolean("40' FR OOG")
    fourty_fr_oog = fields.Integer("40' FR OOG")
    tweenty_soc_active = fields.Boolean("20' SOC")
    tweenty_soc = fields.Integer("20' SOC")
    tweenty_ot_soc_active = fields.Boolean("20' OT SOC")
    tweenty_ot_soc = fields.Integer("20' OT SOC")
    fourty_soc_active = fields.Boolean("40' SOC")
    fourty_soc = fields.Integer("40' SOC")
    fourty_hc_soc_active = fields.Boolean("40' HC SOC")
    fourty_hc_soc = fields.Integer("40' HC SOC")
    fourty_ot_soc_active = fields.Boolean("40' OT SOC")
    fourty_ot_soc = fields.Integer("40' OT SOC")
    fourty_fr_soc_active = fields.Boolean("40' FR SOC")
    fourty_fr_soc = fields.Integer("40' FR SOC")
    fourty_pw_soc_active = fields.Boolean("40' PW SOC")
    fourty_pw_soc = fields.Integer("40' PW SOC")
    fourty_hc_pw_hoc_active = fields.Boolean("40' HC PW SOC")
    fourty_hc_pw_hoc = fields.Integer("40' HC PW SOC")
    fourty_five_soc_active = fields.Boolean("45' SOC")
    fourty_five_soc = fields.Integer("45' SOC")
    tweenty_fr_soc_oog_active = fields.Boolean("20' FR SOC OOG")
    tweenty_fr_soc_oog = fields.Integer("20' FR SOC OOG")
    tweenty_fr_soc_active = fields.Boolean("20' FR SOC")
    tweenty_fr_soc = fields.Integer("20' FR SOC")
    tweenty_ot_soc_oog_active = fields.Boolean("20' OT SOC OOG")
    tweenty_ot_soc_oog = fields.Integer("20' OT SOC OOG")
    fourty_ot_soc_oog = fields.Integer("40' OT SOC OOG")
    fourty_ot_soc_oog_active = fields.Boolean("40' OT SOC OOG")
    fourty_fr_soc_oog_active = fields.Boolean("40' FR SOC OOG")
    fourty_fr_soc_oog = fields.Integer("40' FR SOC OOG")
    



class ASTransport(models.Model):

    _name = 'transport.as'
    
    qty_as = fields.Float('Qty')
    l_as = fields.Float('L (cm)')
    w_as = fields.Float('W (cm)')
    h_as  = fields.Float('H (cm)')
    gros_weight_as = fields.Float('Gross Weight (kg)') 
    pcl_item_n = fields.Char('PCL item N°')
    packaging = fields.Selection([
            ('enveloppe', 'Enveloppe'),
            ('earge_enveloppe', 'Large enveloppe'),
            ('luggage', 'Luggage'),
            ('cardboard_boxes', 'Cardboard boxes'),
            ('tube', 'Tube'),
            ('crates', 'Crates'),
            ('wooden_boxes', 'Wooden Boxes'),
            ('eight', 'Metal boxes'),
            ('nine', 'Barrels'),
            ('teen', 'Crates'),
            ('pallets', 'Pallets'),
            ('drums', 'Drums'),
            ('bigbag', 'Big Bag'),
            ('bundle', 'Bundle'),
            ('bales', 'Bales'),
            ('shipping_sacks', 'Shipping Sacks'),
            ('parcels', 'Parcels'),
            ], setting='Packaging', default='enveloppe')
    customer_item_n = fields.Char('Customer Item N°')
    description = fields.Text('Description')
    mode_transport_as_id = fields.Many2one('transport.mode', string="Mode AS ID")
    volume_as_id = fields.Float('Volume (cbm)', compute='_volume_in_as_all')
    vsix = fields.Float('V6 (Kg)', compute='_volume_in_as_all')
    surface = fields.Float('Surface(m²)', compute='_volume_in_as_all')
    s_total_gross_weight = fields.Float('S/Total Gross Weight(Kg)', compute='_volume_in_as_all')
    s_total_volume = fields.Float('S/Total Volume (cbm)', compute='_volume_in_as_all')
    s_total_v_six = fields.Float('S/Total V6', compute='_volume_in_as_all')
    s_total_surface = fields.Float('S/Total Surface(m²)', compute='_volume_in_as_all')
    s_total_chargeable_weight = fields.Float('S/Total Chargeable Weight(Kg)', compute='_volume_in_as_all')

    def _volume_in_as_all(self):
        for order in self:
            volume_as_id = vsix = surface = s_total_gross_weight = s_total_volume = s_total_v_six = s_total_surface = s_total_chargeable_weight = 0.0 
            for line in order.mode_transport_as_id.mode_transport_as_line:
                line.volume_as_id = (line.l_as * line.w_as * line.h_as) / 1000000
                line.vsix = (line.volume_as_id / 6) * 1000
                line.surface = (line.l_as * line.w_as) / 10000
                line.s_total_gross_weight = line.qty_as * line.gros_weight_as
                line.s_total_volume = line.volume_as_id * line.qty_as
                line.s_total_v_six = line.vsix * line.qty_as
                line.s_total_surface = line.surface * line.qty_as
                if line.vsix > line.gros_weight_as:
                    line.s_total_chargeable_weight = line.s_total_v_six
                else:
                    line.s_total_chargeable_weight = line.s_total_gross_weight
            order.update({
                'volume_as_id': line.volume_as_id,
                'vsix': line.vsix,
                'surface': line.surface,
                's_total_gross_weight': line.s_total_gross_weight,
                's_total_volume': line.s_total_volume,
                's_total_v_six': line.s_total_v_six,
                's_total_surface': line.s_total_surface,
                's_total_chargeable_weight': line.s_total_chargeable_weight,  
            })

    @api.model
    def create(self, vals):
        vals['pcl_item_n'] = self.env['ir.sequence'].next_by_code('transport.as') or '/'
        return super(ASTransport, self).create(vals)


class LTLTransport(models.Model):

    _name = 'transport.ltl'
    
    qty_ltl = fields.Float('Qty')
    l_ltl = fields.Float('L (cm)')
    w_ltl = fields.Float('W (cm)')
    h_ltl  = fields.Float('H (cm)')
    gros_weight_ltl = fields.Float('Gross Weight (kg)') 
    pcl_item_n_ltl = fields.Char('PCL item N°')
    packaging_ltl = fields.Selection([
            ('enveloppe', 'Enveloppe'),
            ('earge_enveloppe', 'Large enveloppe'),
            ('luggage', 'Luggage'),
            ('cardboard_boxes', 'Cardboard boxes'),
            ('tube', 'Tube'),
            ('crates', 'Crates'),
            ('wooden_boxes', 'Wooden Boxes'),
            ('eight', 'Metal boxes'),
            ('nine', 'Barrels'),
            ('teen', 'Crates'),
            ('pallets', 'Pallets'),
            ('drums', 'Drums'),
            ('bigbag', 'Big Bag'),
            ('bundle', 'Bundle'),
            ('bales', 'Bales'),
            ('shipping_sacks', 'Shipping Sacks'),
            ('parcels', 'Parcels'),
            ], setting='Packaging', default='enveloppe')
    customer_item_n_ltl = fields.Char('Customer Item N°')
    description_ltl = fields.Text('Description')
    mode_transport_ltl_id = fields.Many2one('transport.mode', string="Mode LTL ID")
    volume_ltl_id = fields.Float('Volume (cbm)', compute='_volume_in_ltl_all')
    vthree = fields.Float('V3 (Kg)', compute='_volume_in_ltl_all')
    surface_ltl = fields.Float('Surface(m²)', compute='_volume_in_ltl_all')
    s_total_gross_weight_ltl = fields.Float('S/Total Gross Weight(Kg)', compute='_volume_in_ltl_all')
    s_total_volume_ltl = fields.Float('S/Total Volume (cbm)', compute='_volume_in_ltl_all')
    s_total_v_three = fields.Float('S/Total V3', compute='_volume_in_ltl_all')
    s_total_surface_ltl = fields.Float('S/Total Surface(m²)', compute='_volume_in_ltl_all')
    s_total_chargeable_weight_ltl = fields.Float('S/Total Chargeable Weight(Kg)', compute='_volume_in_ltl_all')

    def _volume_in_ltl_all(self):
        for order in self:
            volume_ltl_id = vthree = surface_ltl = s_total_gross_weight_ltl = s_total_volume_ltl = s_total_v_three = s_total_surface_ltl = s_total_chargeable_weight_ltl = 0.0 
            for line in order.mode_transport_ltl_id.mode_transport_ltl_line:
                line.volume_ltl_id = (line.l_ltl * line.w_ltl * line.h_ltl) / 1000000
                line.vthree = (line.volume_ltl_id / 3) * 1000
                line.surface_ltl = (line.l_ltl * line.w_ltl) / 10000
                line.s_total_gross_weight_ltl = line.qty_ltl * line.gros_weight_ltl
                line.s_total_volume_ltl = line.volume_ltl_id * line.qty_ltl
                line.s_total_v_three = line.vthree * line.qty_ltl
                line.s_total_surface_ltl = line.surface_ltl * line.qty_ltl
                if line.vthree > line.gros_weight_ltl:
                        line.s_total_chargeable_weight_ltl = line.s_total_v_three
                else:
                        line.s_total_chargeable_weight_ltl = line.s_total_gross_weight_ltl
            order.update({
                'volume_ltl_id': line.volume_ltl_id,
                'vthree': line.vthree,
                'surface_ltl': line.surface_ltl,
                's_total_gross_weight_ltl': line.s_total_gross_weight_ltl,
                's_total_volume_ltl': line.s_total_volume_ltl,
                's_total_v_three': line.s_total_v_three,
                's_total_surface_ltl': line.s_total_surface_ltl,
                's_total_chargeable_weight_ltl': line.s_total_chargeable_weight_ltl,  
            })

    @api.model
    def create(self, vals):
        vals['pcl_item_n_ltl'] = self.env['ir.sequence'].next_by_code('transport.ltl') or '/'
        return super(LTLTransport, self).create(vals)


class LCLTransport(models.Model):

    _name = 'transport.lcl'
    
    qty_lcl = fields.Float('Qty')
    l_lcl = fields.Float('L (cm)')
    w_lcl = fields.Float('W (cm)')
    h_lcl  = fields.Float('H (cm)')
    gros_weight_lcl = fields.Float('Gross Weight (kg)') 
    pcl_item_n_lcl = fields.Char('PCL item N°')
    packaging_lcl = fields.Selection([
            ('enveloppe', 'Enveloppe'),
            ('earge_enveloppe', 'Large enveloppe'),
            ('luggage', 'Passenger luggage'),
            ('cardboard_boxes', 'Cardboard boxes'),
            ('tube', 'Tube'),
            ('crates', 'Crates'),
            ('wooden_boxes', 'Wooden Boxes'),
            ('eight', 'Metal boxes'),
            ('nine', 'Barrels'),
            ('teen', 'Crates'),
            ('pallets', 'Pallets'),
            ('drums', 'Drums'),
            ('bigbag', 'Big Bag'),
            ('bundle', 'Bundle'),
            ('bales', 'Bales'),
            ('shipping_sacks', 'Shipping Sacks'),
            ('parcels', 'Parcels'),
            ], setting='Packaging', default='enveloppe')
    customer_item_n_lcl = fields.Char('Customer Item N°')
    description_lcl = fields.Text('Description')
    mode_transport_lcl_id = fields.Many2one('transport.mode', string="Mode LCL ID")
    volume_lcl_id = fields.Float('Volume (cbm)', compute='_volume_in_as_all')
    vone = fields.Float('V1 (Kg)', compute='_volume_in_as_all')
    surface_lcl = fields.Float('Surface(m²)', compute='_volume_in_as_all')
    s_total_gross_weight_lcl = fields.Float('S/Total Gross Weight(Kg)', compute='_volume_in_as_all')
    s_total_volume_lcl = fields.Float('S/Total Volume (cbm)', compute='_volume_in_as_all')
    s_total_v_one = fields.Float('S/Total V6', compute='_volume_in_as_all')
    s_total_surface_lcl = fields.Float('S/Total Surface(m²)', compute='_volume_in_as_all')
    s_total_chargeable_weight_lcl = fields.Float('S/Total Chargeable Weight(Kg)', compute='_volume_in_as_all')

    def _volume_in_as_all(self):
        for order in self:
            volume_lcl_id = vone = surface_lcl = s_total_gross_weight_lcl = s_total_volume_lcl = s_total_v_one = s_total_surface_lcl = s_total_chargeable_weight_lcl = 0.0 
            for line in order.mode_transport_lcl_id.mode_transport_lcl_line:
                line.volume_lcl_id = (line.l_lcl * line.w_lcl * line.h_lcl) / 1000000
                line.vone = line.volume_lcl_id * 1000
                line.surface_lcl = (line.l_lcl * line.w_lcl) / 10000
                line.s_total_gross_weight_lcl = line.qty_lcl * line.gros_weight_lcl
                line.s_total_volume_lcl = line.volume_lcl_id * line.qty_lcl
                line.s_total_v_one = line.vone * line.qty_lcl
                line.s_total_surface_lcl = line.surface_lcl * line.qty_lcl
                if line.vone > line.gros_weight_lcl:
                    line.s_total_chargeable_weight_lcl = line.s_total_v_one
                else:
                    line.s_total_chargeable_weight_lcl = line.s_total_gross_weight_lcl
            order.update({
                'volume_lcl_id': line.volume_lcl_id,
                'vone': line.vone,
                'surface_lcl': line.surface_lcl,
                's_total_gross_weight_lcl': line.s_total_gross_weight_lcl,
                's_total_volume_lcl': line.s_total_volume_lcl,
                's_total_v_one': line.s_total_v_one,
                's_total_surface_lcl': line.s_total_surface_lcl,
                's_total_chargeable_weight_lcl': line.s_total_chargeable_weight_lcl,  
            })

    @api.model
    def create(self, vals):
        vals['pcl_item_n_lcl'] = self.env['ir.sequence'].next_by_code('transport.lcl') or '/'
        return super(LCLTransport, self).create(vals)


class FCLTransport(models.Model):

    _name = 'transport.fcl'

    tweenty = fields.Integer("20'")
    tweenty_ot = fields.Integer("20' OT")
    tweenty_fr = fields.Integer("20' FR")
    fourty = fields.Integer("40'")
    fourty_hc = fields.Integer("40' HC")
    fourty_ot = fields.Integer("40' OT")
    fourty_fr = fields.Integer("40' FR")
    fourty_pw = fields.Integer("40' PW")
    fourty_hc_pw = fields.Integer("40' HC PW")
    fourty_five = fields.Integer("45'")
    tweenty_fr_og = fields.Integer("20' FR OOG")
    tweenty_ot_oog = fields.Integer("20' OT OOG")
    fourty_ot_oog = fields.Integer("40' OT OOG")
    fourty_fr_oog = fields.Integer("40' FR OOG")
    tweenty_soc = fields.Integer("20' SOC")
    tweenty_ot_soc = fields.Integer("20' OT SOC")
    fourty_soc = fields.Integer("40' SOC")
    fourty_hc_soc = fields.Integer("40' HC SOC")
    fourty_ot_soc = fields.Integer("40' OT SOC")
    fourty_fr_soc = fields.Integer("40' FR SOC")
    fourty_pw_soc = fields.Integer("40' PW SOC")
    fourty_hc_pw_hoc = fields.Integer("40' HC PW SOC")
    fourty_five_soc = fields.Integer("45' SOC")
    tweenty_fr_soc_oog = fields.Integer("20' FR SOC OOG")
    tweenty_ot_soc_oog = fields.Integer("20' OT SOC OOG")
    fourty_ot_soc_oog = fields.Integer("40' OT SOC OOG")
    fourty_fr_soc_oog = fields.Integer("40' FR SOC OOG")
    mode_transport_fcl_id = fields.Many2one('transport.mode', string="Mode FCL ID")




    
