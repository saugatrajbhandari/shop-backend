from django.urls import path 
from .views import (ProductListView, ProductDetailView)

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('<str:_id>/', ProductDetailView.as_view(), name='product_detail'),
]
