from django.conf.urls import include, url
from django.contrib import admin
from .views import emp_details,gen_pdf,download

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^empform/$', emp_details, name='emp'),
    url(r'^pdf/$', gen_pdf, name='empp'),
	url(r'^download/(?P<Id>[\w.@+-]+)/$', download, name='download'),

#(?P<Id>[\w.@+-]+)/


]
