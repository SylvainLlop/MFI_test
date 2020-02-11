from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from peak_app.views import PeakViewSet, PeaksInArea, map


router = routers.DefaultRouter()
router.register(r'peaks', PeakViewSet, basename='peaks')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    url('^api/area/(?P<coords>.+)/$', PeaksInArea.as_view()),
    url(r'^api/docs/', include_docs_urls(title='Peak API')),
    path('map/', map, name="map"),
]