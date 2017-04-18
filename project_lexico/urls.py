from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',
	 url(r'^admin/', include(admin.site.urls)),
	 url(r'',include('core.urls')),
	 #url(r'^$' ,'core.views.lexica', name='lexica')
	
	 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 )
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 