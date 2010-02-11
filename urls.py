from django.conf.urls.defaults import *
from django.core.paginator import Paginator
from django.contrib import admin

admin.autodiscover()

from foa.settings import MEDIA_ROOT
from foa.products.models import Product

from foa.products.views import move_to_product

urlpatterns = patterns('',
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^admin/(.*)$', admin.site.root),
    (r'^products/(?P<slug>[a-z_]+)/(?P<movement>[a-z_]+)/$', move_to_product),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template':'index.html'}, "index"),
    (r'^sitemap.xml$', 'direct_to_template', {'template':'sitemap.xml'}, "sitemap"),
    (r'^robots.txt$', 'direct_to_template', {'template':'robots.txt'}, "robots"),
    (r'^about/$', 'direct_to_template', {'template':'about.html'}, "about"),
    (r'^products/cancel/$', 'direct_to_template', {'template':'cancel.html'}, "cancel"),
    (r'^products/thanks/$', 'direct_to_template', {'template':'thanks.html'}, "thanks"),
    (r'^paypal_help/$', 'direct_to_template', {'template':'paypal_help.html'}, "paypal_help"),
    (r'^privacy_policy/$', 'direct_to_template', {'template':'privacy_policy.html'}, "privacy_policy"),
    (r'^coming_soon/$', 'direct_to_template', {'template':'coming_soon.html'}, "coming_soon"),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

all_products = Product.objects.filter(visible=True)

urlpatterns += patterns ('django.views.generic.list_detail',
    (r'^products/$', 'object_list', {'queryset': all_products,'template_name':'products.html'}, "products"),
    (r'^products/(?P<slug>[a-z_]+)/$', 'object_detail', {'queryset': all_products, 'template_name':'product_detail.html'}, "products"),
)

