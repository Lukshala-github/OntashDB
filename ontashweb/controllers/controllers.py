# -*- coding: utf-8 -*-
from odoo import http
import werkzeug     
from werkzeug import security

class Ontashweb(http.Controller):      
    @http.route('/emaillogo/ontash.png', type='http', auth='public')
    def ontashlogo(self, debug=False, **k):
        return werkzeug.utils.redirect("/ontashweb/static/wp-content/uploads/2016/04/ontash.png", code=302)

    @http.route('/index', type='http', auth='public', website=True)
    def render_index(self):
        return http.request.render('ontashweb.home', {})       
 
    @http.route('/home', type='http', auth='public', website=True)
    def render_home(self):
        return http.request.render('ontashweb.home', {})          

    @http.route('/about', type='http', auth='public', website=True)
    def render_about(self):
        return http.request.render('ontashweb.about', {})   

    @http.route('/healthcare', type='http', auth='public', website=True)
    def render_healthcare(self):
        return http.request.render('ontashweb.healthcare', {})  

    @http.route('/government', type='http', auth='public', website=True)
    def render_government(self):
        return http.request.render('ontashweb.government', {})                               

    @http.route('/products', type='http', auth='public', website=True)
    def render_products(self):
        return http.request.render('ontashweb.products', {})          

    @http.route('/contact', type='http', auth='public', website=True)
    def render_contact(self):
        return http.request.render('ontashweb.contact', {}) 

    @http.route('/enterprise', type='http', auth='public', website=True)
    def render_enterprise(self):
        return http.request.render('ontashweb.enterprise', {})

    @http.route('/mobility', type='http', auth='public', website=True)
    def render_mobility(self):
        return http.request.render('ontashweb.mobility', {})

    @http.route('/cloud', type='http', auth='public', website=True)
    def render_cloud(self):
        return http.request.render('ontashweb.cloud', {})
    
    @http.route('/tour', type='http', auth='public', website=True)
    def render_tour(self):
        return http.request.render('ontashweb.tour', {})

    @http.route('/demo', type='http', auth='public', website=True)
    def render_demo(self):
        return http.request.render('ontashweb.demo', {})

    @http.route('/odoo_videos', type='http', auth='public', website=True)
    def render_odoo_videos(self):
        return http.request.render('ontashweb.odoo_videos', {})

    @http.route('/odoo_comparisons', type='http', auth='public', website=True)
    def render_odoo_comparisons(self):
        return http.request.render('ontashweb.odoo_comparisons', {})

    @http.route('/thank_you', type='http', auth='public', website=True)
    def render_thank_you(self):
        return http.request.render('ontashweb.thank_you', {})                


# class Ontashweb(http.Controller):
#     @http.route('/ontashweb/ontashweb/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ontashweb/ontashweb/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ontashweb.listing', {
#             'root': '/ontashweb/ontashweb',
#             'objects': http.request.env['ontashweb.ontashweb'].search([]),
#         })

#     @http.route('/ontashweb/ontashweb/objects/<model("ontashweb.ontashweb"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ontashweb.object', {
#             'object': obj
#         })
