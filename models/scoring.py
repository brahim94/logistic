# -*- coding: utf-8 -*-

from odoo import models, fields, api


class scoring(models.Model):

    _name = 'scoring.type'

    importance_before = fields.Selection([
            ('i1', 'I1'),
            ('i2', 'I2'),
            ('i3', 'I3'),
            ('i4', 'I4'),
            ('i5', 'I5'),
            ('i6', 'I6'),
            ('i7', 'I7'),
            ('i8', 'I8'),
            ('i9', 'I9'),
            ('i10', 'I10'),
            ], setting='Importance', default='i1')
    emergency_before = fields.Selection([
            ('e1', 'E1'),
            ('e2', 'E2'),
            ('e3', 'E3'),
            ('e4', 'E4'),
            ('e5', 'E5'),
            ('e6', 'E6'),
            ('e7', 'E7'),
            ('e8', 'E8'),
            ('e9', 'E9'),
            ('e10', 'E10'),
            ], setting='Emergency', default='e1')
    complexity_before = fields.Selection([
            ('c1', 'C1'),
            ('c2', 'C2'),
            ('c3', 'C3'),
            ('c4', 'C4'),
            ('c5', 'C5'),
            ('c6', 'C6'),
            ('c7', 'C7'),
            ('c8', 'C8'),
            ('c9', 'C9'),
            ('c10', 'C10'),
            ], setting='Complexity', default='c1')
    risk_before = fields.Selection([
            ('s1', 'S1'),
            ('s2', 'S2'),
            ('s3', 'S3'),
            ('s4', 'S4'),
            ('s5', 'S5'),
            ('s6', 'S6'),
            ('s7', 'S7'),
            ('s8', 'S8'),
            ('s9', 'S9'),
            ('s10', 'S10'),
            ], setting='Risk', default='s1')
    total_revenu_bf = fields.Selection([
            ('r1', 'R1 (<10k) mad'),
            ('r2', 'R2 (10k-30k) mad'),
            ('r3', 'R3 (30-50k) mad'),
            ('r4', 'R4 ( 50-100k) mad'),
            ('r5', 'R5 (100-200k) mad'),
            ('r6', 'R6 (200-300k) mad'),
            ('r7', 'R7 (300-500k) mad'),
            ('r8', 'R8 (500-750k) mad'),
            ('r9', 'R9 (750-1000k) mad'),
            ('r10', 'R10 (>1000k) mad'),
            ], setting='Total Revenue', default='r1')
    total_cost_bf = fields.Selection([
            ('atc1', 'AtC1 (<2k) mad'),
            ('atc2', 'AtC2 (2-5k) mad'),
            ('atc3', 'AtC3 (5k-10k) mad'),
            ('atc4', 'AtC4 (10-20k) mad'),
            ('atc5', 'AtC5 ( 20-30k) mad'),
            ('atc6', 'AtC6 (30-40k) mad'),
            ('atc7', 'AtC7 (40-50k) mad'),
            ('atc8', 'AtC8 (50-100k) mad'),
            ('atc9', 'AtC9 (100-200k) mad'),
            ('atc10', 'AtC10 (>200k) mad'),
            ], setting='Total At Cost', default='atc1')
    profitability = fields.Selection([
            ('p1', 'P1 (<5%)'),
            ('p2', 'P2 (5-10%)'),
            ('p3', 'P3 (10-15%)'),
            ('p4', 'P4 (15-20%)'),
            ('p5', 'P5 (20-25%)'),
            ('p6', 'P6 (25-30%)'),
            ('p7', 'P7 (30-35%)'),
            ('p8', 'P8 (35-40%)'),
            ('p9', 'P9 (40-50%)'),
            ('p10', 'P10 (>50%)'),
            ], setting='Profitability', default='p1')
    note_bef = fields.Text('notes')
#     importance_after = fields.Selection([
#             ('i1', 'I1'),
#             ('i2', 'I2'),
#             ('i3', 'I3'),
#             ('i4', 'I4'),
#             ('i5', 'I5'),
#             ('i6', 'I6'),
#             ('i7', 'I7'),
#             ('i8', 'I8'),
#             ('i9', 'I9'),
#             ('i10', 'I10'),
#             ], setting='Importance', default='i1')
#     emergency_after = fields.Selection([
#             ('e1', 'E1'),
#             ('e2', 'E2'),
#             ('e3', 'E3'),
#             ('e4', 'E4'),
#             ('e5', 'E5'),
#             ('e6', 'E6'),
#             ('e7', 'E7'),
#             ('e8', 'E8'),
#             ('e9', 'E9'),
#             ('e10', 'E10'),
#             ], setting='Emergency', default='e1')
#     complexity_after = fields.Selection([
#             ('c1', 'C1'),
#             ('c2', 'C2'),
#             ('c3', 'C3'),
#             ('c4', 'C4'),
#             ('c5', 'C5'),
#             ('c6', 'C6'),
#             ('c7', 'C7'),
#             ('c8', 'C8'),
#             ('c9', 'C9'),
#             ('c10', 'C10'),
#             ], setting='Complexity', default='c1')
#     risk_after = fields.Selection([
#             ('s1', 'S1'),
#             ('s2', 'S2'),
#             ('s3', 'S3'),
#             ('s4', 'S4'),
#             ('s5', 'S5'),
#             ('s6', 'S6'),
#             ('s7', 'S7'),
#             ('s8', 'S8'),
#             ('s9', 'S9'),
#             ('s10', 'S10'),
#             ], setting='Risk', default='s1')
#     total_revenu_af = fields.Selection([
#             ('r1', 'R1 (<10k) mad'),
#             ('r2', 'R2 (10k-30k) mad'),
#             ('r3', 'R3 (30-50k) mad'),
#             ('r4', 'R4 ( 50-100k) mad'),
#             ('r5', 'R5 (100-200k) mad'),
#             ('r6', 'R6 (200-300k) mad'),
#             ('r7', 'R7 (300-500k) mad'),
#             ('r8', 'R8 (500-750k) mad'),
#             ('r9', 'R9 (750-1000k) mad'),
#             ('r10', 'R10 (>1000k) mad'),
#             ], setting='Total Revenue', default='r1')
#     total_cost_af = fields.Selection([
#             ('atc1', 'AtC1 (<2k) mad'),
#             ('atc2', 'AtC2 (2-5k) mad'),
#             ('atc3', 'AtC3 (5k-10k) mad'),
#             ('atc4', 'AtC4 (10-20k) mad'),
#             ('atc5', 'AtC5 ( 20-30k) mad'),
#             ('atc6', 'AtC6 (30-40k) mad'),
#             ('atc7', 'AtC7 (40-50k) mad'),
#             ('atc8', 'AtC8 (50-100k) mad'),
#             ('atc9', 'AtC9 (100-200k) mad'),
#             ('atc10', 'AtC10 (>200k) mad'),
#             ], setting='Total At Cost', default='atc1')
#     profitability_aft = fields.Selection([
#             ('p1', 'P1 (<5%)'),
#             ('p2', 'P2 (5-10%)'),
#             ('p3', 'P3 (10-15%)'),
#             ('p4', 'P4 (15-20%)'),
#             ('p5', 'P5 (20-25%)'),
#             ('p6', 'P6 (25-30%)'),
#             ('p7', 'P7 (30-35%)'),
#             ('p8', 'P8 (35-40%)'),
#             ('p9', 'P9 (40-50%)'),
#             ('p10', 'P10 (>50%)'),
#             ], setting='Profitability', default='p1')
#     note_af = fields.Text('notes')

class scoringAfter(models.Model):

    _name = 'scoring.type.after'

    importance_after = fields.Selection([
            ('i1', 'I1'),
            ('i2', 'I2'),
            ('i3', 'I3'),
            ('i4', 'I4'),
            ('i5', 'I5'),
            ('i6', 'I6'),
            ('i7', 'I7'),
            ('i8', 'I8'),
            ('i9', 'I9'),
            ('i10', 'I10'),
            ], setting='Importance', default='i1')
    emergency_after = fields.Selection([
            ('e1', 'E1'),
            ('e2', 'E2'),
            ('e3', 'E3'),
            ('e4', 'E4'),
            ('e5', 'E5'),
            ('e6', 'E6'),
            ('e7', 'E7'),
            ('e8', 'E8'),
            ('e9', 'E9'),
            ('e10', 'E10'),
            ], setting='Emergency', default='e1')
    complexity_after = fields.Selection([
            ('c1', 'C1'),
            ('c2', 'C2'),
            ('c3', 'C3'),
            ('c4', 'C4'),
            ('c5', 'C5'),
            ('c6', 'C6'),
            ('c7', 'C7'),
            ('c8', 'C8'),
            ('c9', 'C9'),
            ('c10', 'C10'),
            ], setting='Complexity', default='c1')
    risk_after = fields.Selection([
            ('s1', 'S1'),
            ('s2', 'S2'),
            ('s3', 'S3'),
            ('s4', 'S4'),
            ('s5', 'S5'),
            ('s6', 'S6'),
            ('s7', 'S7'),
            ('s8', 'S8'),
            ('s9', 'S9'),
            ('s10', 'S10'),
            ], setting='Risk', default='s1')
    total_revenu_af = fields.Selection([
            ('r1', 'R1 (<10k) mad'),
            ('r2', 'R2 (10k-30k) mad'),
            ('r3', 'R3 (30-50k) mad'),
            ('r4', 'R4 ( 50-100k) mad'),
            ('r5', 'R5 (100-200k) mad'),
            ('r6', 'R6 (200-300k) mad'),
            ('r7', 'R7 (300-500k) mad'),
            ('r8', 'R8 (500-750k) mad'),
            ('r9', 'R9 (750-1000k) mad'),
            ('r10', 'R10 (>1000k) mad'),
            ], setting='Total Revenue', default='r1')
    total_cost_af = fields.Selection([
            ('atc1', 'AtC1 (<2k) mad'),
            ('atc2', 'AtC2 (2-5k) mad'),
            ('atc3', 'AtC3 (5k-10k) mad'),
            ('atc4', 'AtC4 (10-20k) mad'),
            ('atc5', 'AtC5 ( 20-30k) mad'),
            ('atc6', 'AtC6 (30-40k) mad'),
            ('atc7', 'AtC7 (40-50k) mad'),
            ('atc8', 'AtC8 (50-100k) mad'),
            ('atc9', 'AtC9 (100-200k) mad'),
            ('atc10', 'AtC10 (>200k) mad'),
            ], setting='Total At Cost', default='atc1')
    profitability_aft = fields.Selection([
            ('p1', 'P1 (<5%)'),
            ('p2', 'P2 (5-10%)'),
            ('p3', 'P3 (10-15%)'),
            ('p4', 'P4 (15-20%)'),
            ('p5', 'P5 (20-25%)'),
            ('p6', 'P6 (25-30%)'),
            ('p7', 'P7 (30-35%)'),
            ('p8', 'P8 (35-40%)'),
            ('p9', 'P9 (40-50%)'),
            ('p10', 'P10 (>50%)'),
            ], setting='Profitability', default='p1')
    note_af = fields.Text('notes')

