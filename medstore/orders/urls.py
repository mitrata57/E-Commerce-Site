from django.urls import path
from .views import add_to_cart, view_cart

urlpatterns = [
    path('cart/add/', add_to_cart),
    path('cart/', view_cart),
]