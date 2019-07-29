from django.contrib import admin
from django.urls import path, include
from . import views
from bab_app import urls as bab_app_urls



urlpatterns=[
    path('', views.home, name = "home"),
    path('admin/', admin.site.urls),
    path('bab/', include(bab_app_urls)),
    
]