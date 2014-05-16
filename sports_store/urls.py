from django.conf.urls import patterns, url


urlpatterns = patterns('sports_store.views',
    url(r'^$', 'home', name='home'),
    url(r'^products$', 'products', name='products'),
)