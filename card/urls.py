from django.conf.urls import patterns, url

from card import views

urlpatterns = patterns('',
    url(r'^operations/$', views.operations, name='operations'),
    url(r'^get_cash/$', views.get_cash, name='get_cash'),
    url(r'^get_balance/$', views.get_balance, name='get_balance'),
    url(r'^pin/$', views.pin_code, name='pin_code'),
    url(r'^$', views.index, name='index'),
)
