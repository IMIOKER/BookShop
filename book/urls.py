from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('detail/<id>', views.Detail, name='detail'),
    path('add/<id>', views.AddToCart, name='add'),
    path('cart/', views.Cart, name='cart'),
    path('more/<slug>', views.add_more, name='more'),
    path('remove/<slug>', views.remove, name='remove'),
    path('checkout/', views.Chackout, name='check'),
    path('payed/', views.Done, name='done'),
]