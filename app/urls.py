from django.contrib import admin
from django.urls import path

from app.views import index,product_detail, add_customers

urlpatterns = [
    path('', index, name='index'),
    path('product-details/<int:pk>', product_detail, name='product-details'),
    path('customers/<int:pk>', add_customers, name='customers')
]
