# -*- coding: utf-8 -*-

from odoo import models, fields, api


class forecast(models.Model):

    _name = 'forecast.type'

    f_start = fields.Date('F.Start')
    f_pick_up = fields.Date('F.Pick up')
    f_terminal_input = fields.Date('F.Terminal Input')
    f_export_cleared = fields.Date('F.Export Cleared')
    f_etd = fields.Date('F.ETD')
    f_eta = fields.Date('F.ETA')
    f_import_cleared = fields.Date('F.Import Cleared')
    f_terminal_exit = fields.Date('F.Terminal Exit')
    f_delivery = fields.Date('F.Delivery')
 




