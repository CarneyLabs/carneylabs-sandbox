from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from django.contrib import admin


admin.autodiscover()

# Admin...
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Registration...
urlpatterns += patterns('',
    url(r'^accounts/', include('registration.backends.default.urls')),
)

# Gallery...
urlpatterns += patterns('',
    url(r'^gallery/', include('gallery.items.urls')),
)

# Generic views...
urlpatterns += patterns('',
    url(r'^generic_views/', include('generic_views.urls')),
)

# Cookbook text views...
urlpatterns += patterns('',
    url(r'^text/', include('cookbook_text.urls', namespace='text')),
)