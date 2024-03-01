from django.urls import include, path

from apps.cakes.views import CakeListView

urlpatterns = [
    path('', CakeListView.as_view(), name='products_list'),

]