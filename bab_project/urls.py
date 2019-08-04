from django.contrib import admin
from django.urls import path, include
from . import views
from bab_app import urls as bab_app_urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from bab_app import views as babviews


urlpatterns=[
    path('', views.home, name = "home"),
    path('admin/', admin.site.urls),
    path('bab/', include(bab_app_urls)),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)