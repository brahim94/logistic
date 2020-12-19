# -*- coding: utf-8 -*-
# from odoo import http


# class TechLogistics(http.Controller):
#     @http.route('/tech_logistics/tech_logistics/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_logistics/tech_logistics/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_logistics.listing', {
#             'root': '/tech_logistics/tech_logistics',
#             'objects': http.request.env['tech_logistics.tech_logistics'].search([]),
#         })

#     @http.route('/tech_logistics/tech_logistics/objects/<model("tech_logistics.tech_logistics"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_logistics.object', {
#             'object': obj
#         })
