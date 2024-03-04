from django.urls import include, path

from apps.cakes.views import CakeListView

urlpatterns = [
    path('', CakeListView.as_view(), name='cake_list'),

]