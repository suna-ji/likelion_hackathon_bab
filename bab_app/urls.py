"""bab_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = "bab"
# bab:browserecipes처럼 해주는 역할

urlpatterns = [
    path('browserecipes/',views.browserecipes, name = "browserecipes"),
    path('contact/',views.contact, name = "contact"),
    path('productpage/',views.productpage, name = "productpage"),
    path('postcreate/', views.postcreate, name = "postcreate"),
    path('shop/',views.shop, name = "shop"),
    path('shortcodes/',views.shortcodes, name = "shortcodes"),
    path('submitrecipe/',views.submitrecipe, name = "submitrecipe"),
    path('typography/',views.typography, name = "typography"),
    path('sendemail/', views.sendemail, name = "sendemail"),
    path('recipepage/<int:id>', views.recipepage, name = "recipepage"),
]

