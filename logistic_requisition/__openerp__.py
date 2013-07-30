# -*- coding: utf-8 -*-
##############################################################################
#
#    Author:  Joël Grand-Guillaume
#    Copyright 2013 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more description.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{"name": "Logistic Requisition",
 "version": "0.1",
 "author": "Camptocamp",
 "license": "AGPL-3",
 "category": "Purchase Management",
 'complexity': "normal",
 "images": [],
 "website": "http://www.camptocamp.com",
 "description": """
This module allows you to manage your Logistic Requisitions.
============================================================

A Logistic requisition express a need that is requested somewhere.

""",
 "depends": ["transport_plan",
             "purchase",
             "purchase_requisition",
             "mail",
             "logistic_order",
             'stock_location_ownership',
             ],
 "demo": ['data/logistic_requisition_demo.xml'],
 "data": ["wizard/logistic_requisition_split_line_view.xml",
          "wizard/logistic_line_create_requisition_view.xml",
          "wizard/assign_line_view.xml",
          "wizard/transport_plan_view.xml",
          "wizard/cost_estimate_view.xml",
          "wizard/logistic_requisition_cancel_view.xml",
          "security/logistic_requisition.xml",
          "security/ir.model.access.csv",
          "data/logistic_requisition_data.xml",
          "data/logistic_requisition_sequence.xml",
          "view/logistic_requisition_view.xml",
          "view/sale_order.xml",
          "view/transport_plan.xml",
          "view/res_partner_view.xml",
          "logistic_requisition_report.xml",
          ],
 "auto_install": False,
 "test": ['test/line_assigned.yml',
          'test/requisition_create_cost_estimate.yml',
          'test/requisition_cancel_reason.yml',
          'test/requisition_confirm_bid.yml',
          'test/transport_plan.yml',
          'test/transport_plan_to_cost_estimate.yml',
          'test/logistic_requisition_onchange.yml',
          ],
 "installable": True,
 }
