from django.conf.urls.defaults import handler404, handler500, patterns, include

from django.contrib import admin

admin.autodiscover()

#------------------------------------------------------------------------------
urlpatterns = patterns('',

    (r'^', 'django_zendesk.views.authorize'),
)