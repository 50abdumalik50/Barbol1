# from django.urls.py import path
from django.urls import include, path

from apps.products.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    # path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail')

]