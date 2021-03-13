# -*- coding: utf-8 -*-

from odoo import models, fields, api, _  


class scope(models.Model):

    _name = 'scope.type'
    _rec_name = 'comments_type'

    directory_scope_id = fields.Many2one('directory.type', 'Directory ID')
    packaging_id = fields.Boolean(string='Packaging', related="directory_scope_id.packaging")
    stuffing_id = fields.Boolean(string='Stuffing', related="directory_scope_id.stuffing")
    lsd_id = fields.Boolean(string='LSD', related="directory_scope_id.lsd")
    loading_on_track_id = fields.Boolean(string='Loading On Truck', related="directory_scope_id.loading_on_track")
    export_formalities_id = fields.Boolean(string='Export Formalities', related="directory_scope_id.export_formalities")
    pre_carriage_id = fields.Boolean(string='Pre-Carriage', related="directory_scope_id.pre_carriage")
    export_customs_id = fields.Boolean(string='Export Customs', related="directory_scope_id.export_customs")
    entry_formalities_id = fields.Boolean(string='Terminal Entry Formalities', related="directory_scope_id.entry_formalities")
    on_terminal_id = fields.Boolean(string='Unloading On Terminal', related="directory_scope_id.on_terminal")
    export_agency_id = fields.Boolean(string='Export Agency', related="directory_scope_id.export_agency")
    loading_main_transport_id = fields.Boolean(string='Loading on Main Transport', related="directory_scope_id.loading_main_transport")
    main_transport_id = fields.Boolean(string='Main Transport', related="directory_scope_id.main_transport")
    from_main_transport_id = fields.Boolean(string='Unloading From Main Transport', related="directory_scope_id.from_main_transport")
    import_agency_id = fields.Boolean(string='Import Agency', related="directory_scope_id.import_agency")
    import_formalities_id = fields.Boolean(string='Import Formalities', related="directory_scope_id.import_formalities")
    import_customs_id = fields.Boolean(string='Import Customs', related="directory_scope_id.import_customs")
    loading_from_term_id = fields.Boolean(string='Loading From Terminal', related="directory_scope_id.loading_from_term")
    terminal_exit_id = fields.Boolean(string='Terminal Exit Formalities', related="directory_scope_id.terminal_exit")
    delivery_id = fields.Boolean(string='Delivery', related="directory_scope_id.delivery")
    ulonading_site_id = fields.Boolean(string='Unloading on site', related="directory_scope_id.ulonading_site")
    unlashing_id = fields.Boolean(string='Unlashing', related="directory_scope_id.unlashing")
    stripping_id = fields.Boolean(string='Stripping', related="directory_scope_id.stripping")
    unpackaging_id = fields.Boolean(string='Unpackaging', related="directory_scope_id.unpackaging")
    other_id = fields.Boolean(string='Other Customs Formalities', related="directory_scope_id.other")
    other_requests_id = fields.Boolean(string='Other Requests', related="directory_scope_id.other_requests")
    insurance_int_id = fields.Boolean(string='Insurance Int', related="directory_scope_id.insurance_int")
    insurance_dom_id = fields.Boolean(string='Insurance Dom', related="directory_scope_id.insurance_dom")
    domestic_customs_id = fields.Boolean(string='Domestic Customs', related="directory_scope_id.domestic_customs")
    trailer_traction_id = fields.Boolean(string='Trailer Traction', related="directory_scope_id.trailer_traction")
    storage_id = fields.Boolean(string='Storage', related="directory_scope_id.storage")
    lifting_id = fields.Boolean(string='Lifting', related="directory_scope_id.lifting")
    domestic_id = fields.Boolean(string='Domestic Haulage', related="directory_scope_id.domestic")
    renting_id = fields.Boolean(string='Renting', related="directory_scope_id.renting")
    consulting_id = fields.Boolean(string='Consulting', related="directory_scope_id.consulting")
    road_surevy_id = fields.Boolean(string='Road survey', related="directory_scope_id.road_surevy")
    studies_id = fields.Boolean(string='Studies', related="directory_scope_id.studies")
    survey_report_id = fields.Boolean(string='Survey Report', related="directory_scope_id.survey_report")
    escort_id = fields.Boolean(string='Escort', related="directory_scope_id.escort")
    civil_work_id = fields.Boolean(string='Civil Work', related="directory_scope_id.civil_work")
    documents_id = fields.Boolean(string='Documents', related="directory_scope_id.documents")

    def open_assignation_total(self):
        return {
            'name': _('Balance'),
            'type': 'ir.actions.act_window',
            'res_model': 'packagin.profitablity',
            'view_mode': 'tree',
            'view_id': False,
            'target': 'new',
        }


    def open_documents_total(self):
        return {
            'name': _('Documents'),
            'type': 'ir.actions.act_window',
            'res_model': 'packagin.documents',
            'view_type': 'form',
            'view_mode': 'tree',
            'view_id': self.env.ref('tech_logistic.documents_view_tree').id,
            'target': 'new',
        }

    ############## PACKAGING ####################
    packagin_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type = fields.Text('Comments')
    forecast_from = fields.Date('Forecast From')
    forecast_unitl = fields.Date('Forecast Initll')
    price_validity_f = fields.Date('Price Validity From')
    price_validity_u = fields.Date('Price Validity Initll')
    packagin_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    
    ############## STUFFING ####################
    stuffing_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_stuffing = fields.Text('Comments')
    forecast_from_stuffing = fields.Date('Forecast From')
    forecast_unitl_stuffing = fields.Date('Forecast Initll')
    price_validity_f_stuffing = fields.Date('Price Validity From')
    price_validity_u_stuffing = fields.Date('Price Validity Initll')
    stuffing_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    
    ############## LSD ####################
    lsd_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_lsd = fields.Text('Comments')
    forecast_from_lsd = fields.Date('Forecast From')
    forecast_unitl_lsd = fields.Date('Forecast Initll')
    price_validity_f_lsd = fields.Date('Price Validity From')
    price_validity_u_lsd = fields.Date('Price Validity Initll')
    lsd_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    
   ############## Loading On Truck ####################
    loading_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_loading = fields.Text('Comments')
    forecast_from_loading = fields.Date('Forecast From')
    forecast_unitl_loading = fields.Date('Forecast Initll')
    price_validity_f_track = fields.Date('Price Validity From')
    price_validity_u_track = fields.Date('Price Validity Initll')
    loading_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')

   ############## Export Formalities ####################
    export_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_export = fields.Text('Comments')
    forecast_from_export = fields.Date('Forecast From')
    forecast_unitl_export = fields.Date('Forecast Initll')
    price_validity_f_export = fields.Date('Price Validity From')
    price_validity_u_export = fields.Date('Price Validity Initll')
    export_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
   ############## Terminal Entry Formalities ####################
    terminal_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_terminal = fields.Text('Comments')
    forecast_from_terminal = fields.Date('Forecast From')
    forecast_unitl_terminal = fields.Date('Forecast Initll')
    price_validity_f_terminal = fields.Date('Price Validity From')
    price_validity_u_terminal = fields.Date('Price Validity Initll')
    terminal_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
    ############## Export Agency ####################
    exp_agncy_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_exp_agency = fields.Text('Comments')
    forecast_from_exp_agency = fields.Date('Forecast From')
    forecast_unitl_exp_agency = fields.Date('Forecast Initll')
    price_validity_f_export = fields.Date('Price Validity From')
    price_validity_u_export = fields.Date('Price Validity Initll')
    exp_agency_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
   ############## Loading on Main Transport ####################
    load_trans_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_load_trans = fields.Text('Comments')
    forecast_from_load_trans = fields.Date('Forecast From')
    forecast_unitl_load_trans = fields.Date('Forecast Initll')
    price_validity_f_main = fields.Date('Price Validity From')
    price_validity_u_main = fields.Date('Price Validity Initll')
    load_trans_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
   ############## Unloading From Main Transport ####################
    upload_trans_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_upload_trans = fields.Text('Comments')
    forecast_from_upload_trans = fields.Date('Forecast From')
    forecast_unitl_upload_trans = fields.Date('Forecast Initll')
    price_validity_f_unloading = fields.Date('Price Validity From')
    price_validity_u_unloading = fields.Date('Price Validity Initll')
    upload_trans_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
    ############## Import Agency ####################
    imp_agency_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_imp_agency = fields.Text('Comments')
    forecast_from_imp_agency = fields.Date('Forecast From')
    forecast_unitl_imp_agency = fields.Date('Forecast Initll')
    price_validity_f_agency = fields.Date('Price Validity From')
    price_validity_u_agency = fields.Date('Price Validity Initll')
    imp_agency_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
    ############## Import Formalities ####################
    imp_form_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_imp_form = fields.Text('Comments')
    forecast_from_imp_form = fields.Date('Forecast From')
    forecast_unitl_imp_form = fields.Date('Forecast Initll')
    price_validity_f_fomra = fields.Date('Price Validity From')
    price_validity_u_forma = fields.Date('Price Validity Initll')
    imp_form_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
   ############## Terminal Exit Formalities ####################
    term_exit_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_term_exit = fields.Text('Comments')
    forecast_from_term_exit = fields.Date('Forecast From')
    forecast_unitl_term_exit = fields.Date('Forecast Initll')
    price_validity_f_exit = fields.Date('Price Validity From')
    price_validity_u_exit = fields.Date('Price Validity Initll')
    term_exit_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
   ############## Unlashing ####################
    unlash_exit_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_unlash = fields.Text('Comments')
    forecast_from_unlash = fields.Date('Forecast From')
    forecast_unitl_unlash = fields.Date('Forecast Initll')
    price_validity_f_unlashing = fields.Date('Price Validity From')
    price_validity_u_unlashing = fields.Date('Price Validity Initll')
    unlash_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
   ############## Stripping ####################
    strip_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_strip = fields.Text('Comments')
    forecast_from_strip = fields.Date('Forecast From')
    forecast_unitl_strip = fields.Date('Forecast Initll')
    price_validity_f_strip = fields.Date('Price Validity From')
    price_validity_u_strip = fields.Date('Price Validity Initll')
    strip_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
   
   ############## Unpackaging ####################
    unpack_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_unpack = fields.Text('Comments')
    forecast_from_unpack = fields.Date('Forecast From')
    forecast_unitl_unpack = fields.Date('Forecast Initll')
    price_validity_f_unpack = fields.Date('Price Validity From')
    price_validity_u_unpack = fields.Date('Price Validity Initll')
    unpack_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')

   ############## Other Customs Formalities ####################
    oth_cust_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_oth_cust = fields.Text('Comments')
    forecast_from_oth_cust = fields.Date('Forecast From')
    forecast_unitl_oth_cust = fields.Date('Forecast Initll')
    price_validity_f_cust = fields.Date('Price Validity From')
    price_validity_u_cust = fields.Date('Price Validity Initll')
    oth_cust_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
  
  ############## Other Requests ####################
    oth_req_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_oth_req = fields.Text('Comments')
    forecast_from_oth_req = fields.Date('Forecast From')
    forecast_unitl_oth_req = fields.Date('Forecast Initll')
    price_validity_f_req = fields.Date('Price Validity From')
    price_validity_u_req = fields.Date('Price Validity Initll')
    oth_req_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
  
############## Trailer Traction ####################
    trai_trac_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_trai_trac = fields.Text('Comments')
    forecast_from_trai_trac = fields.Date('Forecast From')
    forecast_unitl_trai_trac = fields.Date('Forecast Initll')
    price_validity_f_trailer = fields.Date('Price Validity From')
    price_validity_u_trailer = fields.Date('Price Validity Initll')
    trai_trac_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')

############## Storage ####################
    storage_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_storage = fields.Text('Comments')
    forecast_from_storage = fields.Date('Forecast From')
    forecast_unitl_storage = fields.Date('Forecast Initll')
    price_validity_f_storage = fields.Date('Price Validity From')
    price_validity_u_storage = fields.Date('Price Validity Initll')
    storage_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')

############## Lifting ####################
    lifting_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_lifting = fields.Text('Comments')
    forecast_from_lifting = fields.Date('Forecast From')
    forecast_unitl_lifting = fields.Date('Forecast Initll')
    price_validity_f_lifting = fields.Date('Price Validity From')
    price_validity_u_lifting = fields.Date('Price Validity Initll')
    lifting_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')

############## Consulting ####################
    consult_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_consult = fields.Text('Comments')
    forecast_from_consult = fields.Date('Forecast From')
    forecast_unitl_consult = fields.Date('Forecast Initll')
    price_validity_f_conss = fields.Date('Price Validity From')
    price_validity_u_conss = fields.Date('Price Validity Initll')
    consult_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')

############## Studies ####################
    studies_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_studies = fields.Text('Comments')
    forecast_from_studies = fields.Date('Forecast From')
    forecast_unitl_studies = fields.Date('Forecast Initll')
    price_validity_f_studies = fields.Date('Price Validity From')
    price_validity_u_studies = fields.Date('Price Validity Initll')
    studies_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')

############## Civil Work ####################
    civil_work_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_civil_work = fields.Text('Comments')
    forecast_from_civil_work = fields.Date('Forecast From')
    forecast_unitl_civil_work = fields.Date('Forecast Initll')
    price_validity_f_civil = fields.Date('Price Validity From')
    price_validity_u_civil = fields.Date('Price Validity Initll')
    civil_work_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')


############## Pre-Carriage ####################
    pre_carriage_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_pre_carriage = fields.Text('Comments')
    forecast_from_pre_carriage = fields.Date('Forecast From')
    forecast_unitl_pre_carriage = fields.Date('Forecast Initll')
    price_validity_f_carriage = fields.Date('Price Validity From')
    price_validity_u_carriage = fields.Date('Price Validity Initll')
    pre_carriage_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    pre_carriage_pickup_id = fields.Many2one('pickup.precarriage', string='Pick up Pre-carriage adress')
    pre_carriage_delivery_id = fields.Many2one('delivery.precarriage', string='Delivery Pre-carriage adress')
    distance = fields.Float('Distance Km')


############## Export Customs ####################
    pre_carriage_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_pre_carriage = fields.Text('Comments')
    forecast_from_pre_carriage = fields.Date('Forecast From')
    forecast_unitl_pre_carriage = fields.Date('Forecast Initll')
    price_validity_f_cus_ex = fields.Date('Price Validity From')
    price_validity_u_cus_ex = fields.Date('Price Validity Initll')
    pre_carriage_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    exporter = fields.Many2one('res.partner', string='Exporter')
    importer = fields.Many2one('res.partner', string='Importer')
    hs_position_id = fields.Many2one('hs.position', string='HS Position')
    items_level_id = fields.Many2one('item.levels', string='Items Level')
    regime_id = fields.Many2one('packagin.regime', string='Regime Type')
    regime_number_id = fields.Many2one('regime.number', string='Regime Number')
    added_proceders_id = fields.Many2one('added.proceders', string='Added Procedures')
    exemption_id = fields.Many2one('packagin.exemption', string='Exemption')
    duities_payment_id = fields.Many2one('res.partner', string='Duities Payment')
    payment_mode_customs_id = fields.Many2one('payment.mode.customs', string='Payment Mode To Customs')
    customs_desk_id = fields.Many2one('customs.desk', string='Customs Desk')

############## Unloading On Terminal ####################
    unload_termina_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_unload_termina = fields.Text('Comments')
    forecast_from_unload_termina = fields.Date('Forecast From')
    forecast_unitl_unload_termina = fields.Date('Forecast Initll')
    price_validity_f_un_ter = fields.Date('Price Validity From')
    price_validity_u_un_ter = fields.Date('Price Validity Initll')
    unload_termina_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    unload_terminal_id = fields.Many2one('unloading.terminal', string='Terminal')


############## Main Transport ####################
    main_transport_service_id = fields.Many2one('packagin.service', string='Service')
    packagin_pod_transport_id = fields.Many2one('packagin.pod', string='POD')
    packagin_pol_transport_id = fields.Many2one('packagin.pol', string='POL')
    comments_type_main_transport = fields.Text('Comments')
    forecast_from_main_transport = fields.Date('Forecast From')
    forecast_unitl_main_transport = fields.Date('Forecast Initll')
    price_validity_f_m_tra = fields.Date('Price Validity From')
    price_validity_u_m_tra = fields.Date('Price Validity Initll')
    main_transport_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    fret = fields.Selection([
            ('prepaid', 'Prepaid'),
            ('collect', 'Collect'),
            ], string='Fret', default='prepaid')
    requirement_id = fields.Many2one('packagin.requirement', string='Requirement')


############## Import Customs ####################
    import_customs_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_import_customs = fields.Text('Comments')
    forecast_from_import_customs = fields.Date('Forecast From')
    forecast_unitl_import_customs = fields.Date('Forecast Initll')
    price_validityf_imp_cus = fields.Date('Price Validity From')
    price_validityu_imp_cus = fields.Date('Price Validity Initll')
    import_customs_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    exporter_customs = fields.Many2one('res.partner', string='Exporter')
    importer_customs = fields.Many2one('res.partner', string='Importer')
    hs_position_customs_id = fields.Many2one('hs.position', string='HS Position')
    items_level_customs_id = fields.Many2one('item.levels', string='Items Level')
    regime_customs_id = fields.Many2one('packagin.regime', string='Regime Type')
    regime_number_customs_id = fields.Many2one('regime.number', string='Regime Number')
    added_proceders_customs_id = fields.Many2one('added.proceders', string='Added Procedures')
    exemption_customs_id = fields.Many2one('packagin.exemption', string='Exemption')
    duities_payment_customs_id = fields.Many2one('res.partner', string='Duities Payment')
    payment_mode_import_customs_id = fields.Many2one('payment.mode.customs', string='Payment Mode To Customs')
    customs_desk_customs_id = fields.Many2one('customs.desk', string='Customs Desk')


############## Loading From Terminal ####################
    load_terminal_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_load_terminal = fields.Text('Comments')
    forecast_from_load_terminal = fields.Date('Forecast From')
    forecast_unitl_load_terminal = fields.Date('Forecast Initll')
    price_validity_f_f_ter = fields.Date('Price Validity From')
    price_validity_u_f_ter = fields.Date('Price Validity Initll')
    load_terminal_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    load_terminal_id = fields.Many2one('unloading.terminal', string='Terminal')


############## Delivery ####################
    delivery_service_id = fields.Many2one('packagin.service', string='Service')
    comments_delivery = fields.Text('Comments')
    forecast_from_delivery = fields.Date('Forecast From')
    forecast_unitl_delivery = fields.Date('Forecast Initll')
    price_validity_f_deli = fields.Date('Price Validity From')
    price_validity_u_deli = fields.Date('Price Validity Initll')
    delivery_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    delivery_pickup_id = fields.Many2one('pickup.precarriage', string='Pick up Pre-carriage adress')
    delivery_delivery_id = fields.Many2one('delivery.precarriage', string='Delivery Pre-carriage adress')
    delivery_distance = fields.Float('Distance Km')

############## Unloading On Site ####################
    unload_site_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_unload_site = fields.Text('Comments')
    forecast_from_unload_site = fields.Date('Forecast From')
    forecast_unitl_unload_site = fields.Date('Forecast Initll')
    price_validity_f_lo_si = fields.Date('Price Validity From')
    price_validity_u_lo_si = fields.Date('Price Validity Initll')
    unload_site_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    unload_site_id = fields.Many2one('unloading.site', string='Unloading On Site')

############## Insurance Int ####################
    insurance_int_service_id = fields.Many2one('packagin.service', string='Service')
    comments_insurance_int = fields.Text('Comments')
    forecast_from_insurance_int = fields.Date('Forecast From')
    forecast_unitl_insurance_int = fields.Date('Forecast Initll')
    price_validity_f_insu_in = fields.Date('Price Validity From')
    price_validity_u_insu_in = fields.Date('Price Validity Initll')
    insurance_int_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    insurance_intid = fields.Many2one('insurance.int', string='Insurance Int')

############## Insurance Dom ####################
    insurance_dom_service_id = fields.Many2one('packagin.service', string='Service')
    comments_insurance_dom = fields.Text('Comments')
    forecast_from_insurance_dom = fields.Date('Forecast From')
    forecast_unitl_insurance_dom = fields.Date('Forecast Initll')
    price_validity_f_ins_do = fields.Date('Price Validity From')
    price_validity_u_ins_do = fields.Date('Price Validity Initll')
    insurance_dom_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    insurancedom_id = fields.Many2one('insurance.int', string='Insurance Int')

############## Domestic Customs ####################
    domestic_customs_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_domestic_customs = fields.Text('Comments')
    forecast_from_domestic_customs = fields.Date('Forecast From')
    forecast_unitl_domestic_customs = fields.Date('Forecast Initll')
    price_validity_f_dom_cu = fields.Date('Price Validity From')
    price_validity_u_dom_cu = fields.Date('Price Validity Initll')
    domestic_customs_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    exporter_domestic = fields.Many2one('res.partner', string='Exporter')
    importer_domestic = fields.Many2one('res.partner', string='Importer')
    hs_position_domestic_id = fields.Many2one('hs.position', string='HS Position')
    items_level_domestic_id = fields.Many2one('item.levels', string='Items Level')
    regime_domestic_id = fields.Many2one('packagin.regime', string='Regime Type')
    regime_number_domestic_id = fields.Many2one('regime.number', string='Regime Number')
    added_proceders_domestic_id = fields.Many2one('added.proceders', string='Added Procedures')
    exemption_domestic_id = fields.Many2one('packagin.exemption', string='Exemption')
    duities_payment_domestic_id = fields.Many2one('res.partner', string='Duities Payment')
    payment_mode_import_domestic_id = fields.Many2one('payment.mode.customs', string='Payment Mode To Customs')
    customs_desk_domestic_id = fields.Many2one('customs.desk', string='Customs Desk')

############## Domestic Haulage ####################
    domestic_haulage_service_id = fields.Many2one('packagin.service', string='Service')
    comments_domestic_haulage = fields.Text('Comments')
    forecast_from_domestic_haulage = fields.Date('Forecast From')
    forecast_unitl_domestic_haulage = fields.Date('Forecast Initll')
    price_validity_f_dom_ho = fields.Date('Price Validity From')
    price_validity_u_dom_ho = fields.Date('Price Validity Initll')
    domestic_haulage_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    domestic_haulage_pickup_id = fields.Many2one('pickup.precarriage', string='Pick up Pre-carriage adress')
    domestic_haulage_delivery_id = fields.Many2one('delivery.precarriage', string='Delivery Pre-carriage adress')
    domestic_haulage_distance = fields.Float('Distance Km')


############## Runting ####################
    runting_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_runting = fields.Text('Comments')
    forecast_from_runting = fields.Date('Forecast From')
    forecast_unitl_runting = fields.Date('Forecast Initll')
    price_validity_f_run = fields.Date('Price Validity From')
    price_validity_u_run = fields.Date('Price Validity Initll')
    runting_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    equipement_id = fields.Many2one('equipement.runting', string='Equipment')
    duration_id = fields.Many2one('packagin.duration', string='Duration')
    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.country.state', string='City')

############## Road survey ####################
    road_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_road = fields.Text('Comments')
    forecast_from_road = fields.Date('Forecast From')
    forecast_unitl_road = fields.Date('Forecast Initll')
    price_validity_f_ro_su = fields.Date('Price Validity From')
    price_validity_u_ro_su = fields.Date('Price Validity Initll')
    road_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    from_road = fields.Text('From')
    to_road = fields.Text('To')
    distance_road = fields.Float('Distance (Km)')
    top_length = fields.Float('Top Length (m)')
    top_width = fields.Float('Top Width (m)')
    top_height = fields.Float('Top Height (m)')
    top_wieght = fields.Float('Top Top G Weight (tons)')


############## Survey Report ####################
    report_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_report = fields.Text('Comments')
    forecast_from_report = fields.Date('Forecast From')
    forecast_unitl_report = fields.Date('Forecast Initll')
    price_validity_f_ro_re = fields.Date('Price Validity From')
    price_validity_u_ro_re = fields.Date('Price Validity Initll')
    report_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    surevy_adress = fields.Text('Survey Adress')

############## Escort ####################
    escort_service_id = fields.Many2one('packagin.service', string='Service')
    comments_type_escort = fields.Text('Comments')
    forecast_from_escort = fields.Date('Forecast From')
    forecast_unitl_escort = fields.Date('Forecast Initll')
    price_validity_f_esc = fields.Date('Price Validity From')
    price_validity_u_esc = fields.Date('Price Validity Initll')
    escort_profitability_id = fields.Many2one('packagin.profitablity', string='Profitability')
    from_escort = fields.Text('From')
    to_escort = fields.Text('To')
    distance_escort = fields.Float('Distance (Km)')
    top_length_escort = fields.Float('Top Length (m)')
    top_width_escort = fields.Float('Top Width (m)')
    top_height_escort = fields.Float('Top Height (m)')
    top_wieght_escort = fields.Float('Top Top G Weight (tons)')


############## Documents ####################
    
    packaging_documents_id = fields.Many2one('packagin.documents', string='Documents')
    

class PackagingSevice(models.Model):

    _name = 'packagin.service'
    _rec_name = 'direction'

    packagin_division_id = fields.Many2one('packagin.division', string='Division')    
    direction = fields.Selection([
            ('export', 'Export (E)'),
            ('import', 'Import (I)'),
            ('local', 'Local (L)'),
            ('off', 'OffShore (Off)'),
            ('offon', 'OffOnShore (OffOn)'),
            ('offoncl', 'OffOnShore Cleared (OffOnCl)'),
            ], string='Direction', default='export')
    
    packagin_mode_transport_id = fields.Selection([
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
    packagin_standrads_id = fields.Many2one('standard.type', string='Standars')

class PackagingDivision(models.Model):

    _name = 'packagin.division'
    _rec_name = 'division'

    division  = fields.Text('Division')
    division_n = fields.Char('Division N°')
    division_tag = fields.Text('Division Tag')
    packagin_department_id = fields.Many2one('packagin.department', string='Department')


class PackagingDocuments(models.Model):

    _name = 'packagin.documents'
    _rec_name = 'doc_name'

    doc_name = fields.Char('Doc name')
    doc = fields.Binary('Doc')


class PickupPrecarriage(models.Model):

    _name = 'pickup.precarriage'
    _rec_name = 'pick_up_preecarriage'

    pick_up_preecarriage  = fields.Text('Pick up Pre-carriage adress')
    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.country.state', string='City')

class DeliveryPrecarriage(models.Model):

    _name = 'deliveyr.precarriage'
    _rec_name = 'delivery_preecarriage'

    delivery_preecarriage  = fields.Text('Delivery Pre-carriage adress')
    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.country.state', string='City')

class HsPosition(models.Model):

    _name = 'hs.position'
    _rec_name = 'description'

    sec  = fields.Integer('SEC')
    ch  = fields.Integer('CH')
    position  = fields.Integer('Position')
    hs_code  = fields.Integer('HS Code')
    description  = fields.Text('Description')
    

class ItemLevels(models.Model):

    _name = 'item.levels'
    _rec_name = 'items_level'

    mode_transport_id = fields.Many2one('transport.mode', string='Mode Of Transport')
    items_level = fields.Text('Items Level')
    items_level_n = fields.Char('Items Level N°')

class UnloadingTerminal(models.Model):

    _name = 'unloading.terminal'
    _rec_name = 'unloading_terminal'

    unloading_terminal = fields.Text('Terminal')
    unloading_terminal_n = fields.Char('Terminal N°')    
    port_id = fields.Many2one('packagin.pod', string='Port')


class UnloadingOnSite(models.Model):

    _name = 'unloading.site'
    _rec_name = 'unloading_adress'

    unloading_adress = fields.Text('Unloading Adress')
    country_id = fields.Many2one('res.country', string='Country')
    city_id = fields.Many2one('res.country.state', string='City')

class InsuranceInt(models.Model):

    _name = 'insurance.int'
    _rec_name = 'description_insurance'

    insurance_int = fields.Text('Insurance Int')
    insurance_code  = fields.Char('Insurance Code')
    description_insurance = fields.Text('Description')

class EquipementEquipement(models.Model):

    _name = 'packagin.equipement'
    _rec_name = 'equipement'

    equipement = fields.Text('Equipment')
    equipement_n = fields.Char('Equipment N°')    

class EquipementRunting(models.Model):

    _name = 'equipement.runting'
    _rec_name = 'equipement_name'

    equipement_name = fields.Text('Equipment Name')
    capacity_eqp = fields.Text('Capacity')
    specification_eqp = fields.Text('Specification')
    equipement_code = fields.Char('Equipment Code')    
    equipement_id = fields.Many2one('packagin.equipement', string='Equipment Type')

class DurationDuration(models.Model):

    _name = 'packagin.duration'
    _rec_name = 'duration'

    duration = fields.Selection([
            ('day', 'Day(s)'),
            ('week', 'Week(s)'),
            ('month', 'Month(s)'),
            ('year', 'Years(s)'),
            ], string='Duration', default='day')
    nb_days = fields.Integer('Number of days')
    nb_weeks = fields.Integer('Number of weeks')
    nb_months = fields.Integer('Number of months')
    nb_years = fields.Integer('Number of years')


class Requirement(models.Model):

    _name = 'packagin.requirement'
    _rec_name = 'requirement'

    requirement = fields.Text('Requirement')
    requirement_n = fields.Char('Requirement N°')    
    
    @api.model
    def create(self, vals):
        vals['requirement_n'] = self.env['ir.sequence'].next_by_code('code.requirement') or '/'
        return super(Requirement, self).create(vals)


class PackagingProfitability(models.Model):

    _name = 'packagin.profitablity'
    # _rec_name = 'suppliers'

    # atc = fields.Selection([
    #         ('yes', 'Yes'),
    #         ('no', 'No'),
    #         ], string='ATC', default='no')
    currency_id = fields.Selection([
            ('mad', 'MAD'),
            ('euro', 'EURO'),
            ('usd', 'USD'),
            ], string='Currency', default='mad')
    
    # @api.onchange('packaging_amount_line')
    # def onchange_currency_id(self):
    #     for pack in self:
    #         currency_id = ''
    #         for line in pack.packaging_amount_line:
    #             self.currency_id = line.cost_rate_ht_currency
    
    # # cost_rate_ht_monet = fields.Float('Cost Rate HT')
    # suppliers = fields.Many2one('res.partner', string='Suppliers')
    packaging_amount_line = fields.One2many('packaging.amount','packaging_amount_id', string="Packaging Amount")                    
    # packaging_section = fields.Many2one('packaging.section', string='Section')
    total_cost_ht_dh = fields.Float(string='Tot Cost HT', compute='_total_packaging_all')
    total_sales_ht_dh = fields.Float(string='Tot Sales HT', compute='_total_packaging_all')
    total_net_sales_ht_dh = fields.Float(string='Tot Net Sales HT', compute='_total_packaging_all')
    total_profit_ht_dh = fields.Float(string='Tot Profit HT', compute='_total_packaging_all')
    ### EURO ###
    total_cost_ht_euro = fields.Float(string='Tot Cost HT', compute='_total_packaging_all')
    total_sales_ht_euro = fields.Float(string='Tot Sales HT', compute='_total_packaging_all')
    total_net_sales_ht_euro = fields.Float(string='Tot Net Sales HT', compute='_total_packaging_all')
    total_profit_ht_euro = fields.Float(string='Tot Profit HT', compute='_total_packaging_all')
    ### USD ###
    total_cost_ht_usd = fields.Float(string='Tot Cost HT', compute='_total_packaging_all')
    total_sales_ht_usd = fields.Float(string='Tot Sales HT', compute='_total_packaging_all')
    total_net_sales_ht_usd = fields.Float(string='Tot Net Sales HT', compute='_total_packaging_all')
    total_profit_ht_usd = fields.Float(string='Tot Profit HT', compute='_total_packaging_all')
    

    profit_dh = fields.Float(string='Profit en %', compute='_profit_dh_all')
    profit_euro = fields.Float(string='Profit en %', compute='_profit_euro_all')
    profit_usd = fields.Float(string='Profit en %', compute='_profit_usd_all')
    taux_change_euro = fields.Float(string='Taux de change (Euro)', default=10.5)
    taux_change_usd = fields.Float(string='Taux de change (USD)', default=9.8)
    
    ##### conversion Euro ####
    cost_euro_converted = fields.Float(string='Cost HT Euro', compute='_euro_convertion')
    sales_ht_euro_converted = fields.Float(string='Sales Ht Euro', compute='_euro_convertion')
    total_net_sales_ht_converted_euro = fields.Float(string='Net Sales Euro', compute='_euro_convertion')
    total_profit_ht_converted_euro = fields.Float(string='Profit Euro', compute='_euro_convertion')
       
##### conversion Usd ####
    cost_usd_converted = fields.Float(string='Cost HT USD', compute='_usd_convertion')
    sales_ht_usd_converted = fields.Float(string='Sales Ht USD', compute='_usd_convertion')
    total_net_sales_ht_converted_usd = fields.Float(string='Net Sales USD', compute='_usd_convertion')
    total_profit_ht_converted_usd = fields.Float(string='Profit USD', compute='_usd_convertion')
    
###### total #####

    total_cost_ht_converted_dh = fields.Float(string='Σ Cost HT ', compute='_total_converted')
    total_sales_ht_converted_dh = fields.Float(string='Σ Sales HT', compute='_total_converted')
    total_net_sales_ht_converted_dh = fields.Float(string='Σ Net Sales HT', compute='_total_converted')
    total_profit_ht_converted_dh = fields.Float(string='Σ Profit HT', compute='_total_converted')

    
    def _total_packaging_all(self):
        for pack in self:
            total_cost_ht_dh = total_sales_ht_dh = total_net_sales_ht_dh = total_profit_ht_dh = profit_dh  = total_cost_ht_euro = total_sales_ht_euro = total_net_sales_ht_euro = total_profit_ht_euro = profit_euro  = total_cost_ht_usd = total_sales_ht_usd = total_net_sales_ht_usd = total_profit_ht_usd = profit_usd  = 0.0
            for line in pack.packaging_amount_line:
                if line.cost_rate_ht_currency == 'mad':
                    total_cost_ht_dh += line.s_tot_cost_ht
                    total_sales_ht_dh += line.s_tot_sales_ht
                    total_net_sales_ht_dh += line.s_tot_net_sale_ht
                    total_profit_ht_dh += line.s_profit_ht
                if line.cost_rate_ht_currency == 'euro':
                    total_cost_ht_euro += line.s_tot_cost_ht
                    total_sales_ht_euro += line.s_tot_sales_ht
                    total_net_sales_ht_euro += line.s_tot_net_sale_ht
                    total_profit_ht_euro += line.s_profit_ht
                if line.cost_rate_ht_currency == 'usd':
                    total_cost_ht_usd += line.s_tot_cost_ht
                    total_sales_ht_usd += line.s_tot_sales_ht
                    total_net_sales_ht_usd += line.s_tot_net_sale_ht
                    total_profit_ht_usd += line.s_profit_ht
            pack.update({
                'total_cost_ht_dh': total_cost_ht_dh,
                'total_sales_ht_dh': total_sales_ht_dh,
                'total_net_sales_ht_dh': total_net_sales_ht_dh,
                'total_profit_ht_dh': total_profit_ht_dh,
                'total_cost_ht_euro': total_cost_ht_euro,
                'total_sales_ht_euro': total_sales_ht_euro,
                'total_net_sales_ht_euro': total_net_sales_ht_euro,
                'total_profit_ht_euro': total_profit_ht_euro,
                'total_cost_ht_usd': total_cost_ht_usd,
                'total_sales_ht_usd': total_sales_ht_usd,
                'total_net_sales_ht_usd': total_net_sales_ht_usd,
                'total_profit_ht_usd': total_profit_ht_usd,
            })

    @api.depends('total_net_sales_ht_dh', 'total_profit_ht_dh')
    def _profit_dh_all(self):
        for record in self:
            if record.total_net_sales_ht_dh > 0 and record.total_profit_ht_dh > 0:
                record.profit_dh = record.total_profit_ht_dh / record.total_net_sales_ht_dh
            else:
                record.profit_dh = 0
    
    @api.depends('total_net_sales_ht_euro', 'total_profit_ht_euro')
    def _profit_euro_all(self):
        for record in self:
            if record.total_net_sales_ht_euro > 0 and record.total_profit_ht_euro > 0:
                record.profit_euro = record.total_profit_ht_euro / record.total_net_sales_ht_euro
            else:
                record.profit_euro = 0
    
    @api.depends('total_net_sales_ht_usd', 'total_profit_ht_usd')
    def _profit_usd_all(self):
        for record in self:
            if record.total_net_sales_ht_usd > 0 and record.total_profit_ht_usd > 0:
                record.profit_usd = record.total_profit_ht_usd / record.total_net_sales_ht_usd
            else:
                record.profit_usd = 0
    
    @api.depends('total_cost_ht_euro', 'total_sales_ht_euro', 'total_net_sales_ht_euro', 'total_profit_ht_euro')
    def _euro_convertion(self):
        for record in self:
            record.cost_euro_converted = record.total_cost_ht_euro * record.taux_change_euro
            record.sales_ht_euro_converted = record.total_sales_ht_euro * record.taux_change_euro
            record.total_net_sales_ht_converted_euro = record.total_net_sales_ht_euro * record.taux_change_euro
            record.total_profit_ht_converted_euro = record.total_profit_ht_euro * record.taux_change_euro
    
    @api.depends('total_cost_ht_usd', 'total_sales_ht_usd', 'total_net_sales_ht_usd', 'total_profit_ht_usd')
    def _usd_convertion(self):
        for record in self:
            record.cost_usd_converted = record.total_cost_ht_usd * record.taux_change_usd
            record.sales_ht_usd_converted = record.total_sales_ht_usd * record.taux_change_usd
            record.total_net_sales_ht_converted_usd = record.total_net_sales_ht_usd * record.taux_change_usd
            record.total_profit_ht_converted_usd = record.total_profit_ht_usd * record.taux_change_usd
    

    @api.depends('total_cost_ht_dh', 'total_sales_ht_dh', 'total_net_sales_ht_dh', 'total_profit_ht_dh', 'cost_euro_converted', 'sales_ht_euro_converted', 'total_net_sales_ht_converted_euro', 'total_profit_ht_converted_euro', 'cost_usd_converted', 'sales_ht_usd_converted', 'total_net_sales_ht_converted_usd', 'total_profit_ht_converted_usd')
    def _total_converted(self):
        for record in self:
            record.total_cost_ht_converted_dh = record.total_cost_ht_dh + record.cost_euro_converted + record.cost_usd_converted
            record.total_sales_ht_converted_dh = record.total_sales_ht_dh + record.sales_ht_euro_converted + record.sales_ht_usd_converted
            record.total_net_sales_ht_converted_dh = record.total_net_sales_ht_dh + record.total_net_sales_ht_converted_euro + record.total_net_sales_ht_converted_usd
            record.total_profit_ht_converted_dh = record.total_profit_ht_dh + record.total_profit_ht_converted_euro + record.total_profit_ht_converted_usd
    
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
    packagin_added_proceders_id = fields.Many2one('added.proceders', string='Added Procedures')
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

    added_proceders = fields.Text('Added Procedures')
    added_proceders_n = fields.Char('Procedures N°')

class PackagingExcemption(models.Model):
 
    _name = 'packagin.exemption'
    _rec_name = 'exemption'

    exemption = fields.Text('Exemption')
    exemption_description = fields.Text('Exemption Description')
    exemption_n = fields.Char('Exemption N°')

class PaymentMode(models.Model):
 
    _name = 'payment.mode.customs'
    _rec_name = 'payment_mode_customs'

    payment_mode_customs = fields.Text('Payment Mode To Customs')
    payment_mode_customs_n = fields.Char('Payment Mode To Customs N°')


class PackagingCustomsDesk(models.Model):
 
    _name = 'customs.desk'
    _rec_name = 'customs_desk'

    customs_desk = fields.Text('Custom Desk')
    customs_desk_n = fields.Char('Custom Desk N°')
    city_id = fields.Many2one('res.country.state', string='City')
    country_id = fields.Many2one('res.country', string='Country')

class DivisionQuality(models.Model):
 
    _name = 'division.quality'
    _rec_name = 'division_n'

    division_n = fields.Char('Division')
    
class DocumentQuality(models.Model):
 
    _name = 'document.quality'
    _rec_name = 'document_name'

    div_id = fields.Many2one('division.quality', string='Division')
    document_n = fields.Char('Document N°')
    document_name = fields.Char('Document name')
    document_date = fields.Date('Document Date')
    review_doc = fields.Integer('Review')

class PrintQuality(models.Model):
 
    _name = 'print.quality'
    _rec_name = 'print_name'

    div_id = fields.Many2one('division.quality', string='Division')
    print_n = fields.Char('Print N°')
    print_name = fields.Char('Print name')
    print_date = fields.Date('Print Date')
    review_print = fields.Integer('Review')

class VideoQuality(models.Model):
 
    _name = 'video.quality'
    _rec_name = 'video_name'

    div_id = fields.Many2one('division.quality', string='Division')
    video_n = fields.Char('Document N°')
    video_name = fields.Char('Document name')
    video_date = fields.Date('Document Date')
    review_vid = fields.Integer('Review')

class ProcessesProcesses(models.Model):
 
    _name = 'processes.processes'
    _rec_name = 'processes_name'

    processes_name = fields.Text('Processes Name')
    processes_n = fields.Char('Processes N°')
    review_n = fields.Integer('Review')
    date = fields.Date('Date')
    processes = fields.Char('Processes')
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
    document_quality_id = fields.Many2one('document.quality', string='Documents')
    print_quality_id = fields.Many2one('print.quality', string='Prints')
    video_quality_id = fields.Many2one('video.quality', string='Videos')
    packagin_div_id = fields.Many2one('division.quality', string='Division')    
    

class PackagingProcesses(models.Model):
 
    _name = 'packaging.processes'
    _rec_name = 'procedure_name'

    packagin_processes_id = fields.Many2one('processes.processes', string='Processes')
    procedure_name = fields.Text('Procedure Name')
    procedure_n = fields.Char('Procedure N°')
    review = fields.Integer('Review')
    date = fields.Date('Date')
    procedures = fields.Char('Procedures')
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
    document_quali_id = fields.Many2one('document.quality', string='Documents')
    print_quali_id = fields.Many2one('print.quality', string='Prints')
    video_quali_id = fields.Many2one('video.quality', string='Videos')
    packagin_dv_id = fields.Many2one('division.quality', string='Division')    
    
class PackagingInstruction(models.Model):
 
    _name = 'packaging.instruction'
    _rec_name = 'instruction_name'

    procedures_id = fields.Many2one('packaging.processes', string='Procedures')
    instruction_name = fields.Text('Instruction Name')
    instruction_n = fields.Char('Instruction N°')
    review = fields.Integer('Review')
    date = fields.Date('Date')
    instruction = fields.Char('Instruction')
    document_quali_id = fields.Many2one('document.quality', string='Documents')
    print_quali_id = fields.Many2one('print.quality', string='Prints')
    video_quali_id = fields.Many2one('video.quality', string='Videos')
    packagin_dv_id = fields.Many2one('division.quality', string='Division')    

class Standards(models.Model):
 
    _name = 'standard.type'
    # _rec_name = 'division_n'

    procesees_id = fields.Many2one('processes.processes', string='Processes N°')
    procedures_id = fields.Many2one('packaging.processes', string='Procedures N°')
    instructions_id = fields.Many2one('packaging.instruction', string='Instructions N°')    


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

    service_id = fields.Many2one('packagin.service', string='Service')
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

    # cost_rate_ht_currency = fields.Many2one('res.currency', string='Currency')
    cost_rate_ht_currency = fields.Selection([
            ('mad', 'MAD'),
            ('euro', 'EURO'),
            ('usd', 'USD'),
            ], string='Currency', default='mad')
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
    packaging_amount_id = fields.Many2one('packagin.profitablity', string="Packaging Amount")
    atc = fields.Selection([
            ('yes', 'Yes'),
            ('no', 'No'),
            ], string='ATC', default='no')
    packaging_section = fields.Many2one('packaging.section', string='Section')
    suppliers = fields.Many2one('res.partner', string='Suppliers')
    # taux_change_euro = fields.Float(string='Taux de change (Euro)', related="packaging_section.taux_change_euro")
    # taux_change_usd = fields.Float(string='Taux de change (Usd)', related="packaging_section.taux_change_usd")
    
    def _amount_in_packaging_all(self):
        for pack in self:
            cost_rate_ht_monet = qty = sale_rate_ht = net_sale_rate = profit_ht = s_tot_sales_ht = s_tot_cost_ht = s_tot_net_sale_ht = s_profit_ht = 0.0 
            for line in pack.packaging_amount_id.packaging_amount_line:
                line.net_sale_rate = line.sale_rate_ht - (line.sale_rate_ht * (line.discount / 100))
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
        