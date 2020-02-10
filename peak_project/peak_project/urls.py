from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('peaks/', include('peak_app.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns





