from django.contrib import admin
from django.urls import path, include
from . import views
from bab_app import urls as bab_app_urls
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('', views.home, name = "home"),
    path('admin/', admin.site.urls),
    path('bab/', include(bab_app_urls)),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)