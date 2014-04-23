from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('cookbook_text.views',
   url(r'^recipe/(?P<index>\d+)/$', 'recipe', name='recipe'),
)