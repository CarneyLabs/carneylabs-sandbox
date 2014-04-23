from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^template_view$', TemplateView.as_view(template_name='generic_views/template_view.html')),
)