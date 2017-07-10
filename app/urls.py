from django.conf.urls import include, url
from django.contrib import admin
from .views import hello,riderinfo,bulkriderinfo,send_sms,send_sms2,empl

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^sms$', send_sms, name='sms'),
    url(r'^hello$', hello, name='hello'),
    url(r'^addriders$', riderinfo, name='riderin'),
    url(r'^addbulkriders$', bulkriderinfo, name='riderin'),
    url(r'^admins$', send_sms2, name='admins'),
    url(r'^form$', empl, name='helloo'),


]
