from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import logout

handler404 = 'error_handlers.handler404'

urlpatterns = patterns('',
    url(r'^', include('card.urls')),
    url(r'^logout/$', logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
