from django.urls import path
from .views import product_list
from .views import home

urlpatterns = [
    path('products/', product_list),
    path('', home), 
]