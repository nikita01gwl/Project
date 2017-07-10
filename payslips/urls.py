from django.conf.urls import include, url
from django.contrib import admin
from .views import load_data

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^payslip$', load_data, name='sms'),
    
    



]
