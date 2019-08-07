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
    path('comment_create/<int:id>', views.comment_create, name = "comment_create"),
    path('shop/',views.shop, name = "shop"),
    path('shortcodes/',views.shortcodes, name = "shortcodes"),
    path('submitrecipe/',views.submitrecipe, name = "submitrecipe"),
    path('typography/',views.typography, name = "typography"),
    path('sendemail/', views.sendemail, name = "sendemail"),
    path('recipepage/<int:id>', views.recipepage, name = "recipepage"),
    path('like_toggle/<int:id>/', views.like_toggle, name="like_toggle"),
    path('post_like/', views.post_like, name="post_like"),
    path('favorite_toggle/<int:post_id>/', views.favorite_toggle, name="favorite_toggle"),
    path('favorite/<int:user_id>/', views.favorite, name="favorite"),
]

