from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from foa.products.models import Product

urlpatterns = patterns('django.views.generic.simple',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'direct_to_template', {'template':'index.html'}, "index"),
    (r'^about/$', 'direct_to_template', {'template':'about.html'}, "about"),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

urlpatterns += patterns ('django.views.generic.list_detail',
    (r'^products/$', 'object_list', {'queryset':Product.objects.all(),'template_name':'products.html'}, "products"),
)
