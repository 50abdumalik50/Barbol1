from django.shortcuts import render
from django.views import generic

from apps.products.models import Product
# from apps.website.models import WebsiteSettings


class CakeListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = "cakes"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['left_categories'] = Product.objects.filter(parent=None)
        # context['palto_products'] = Product.objects.filter(category__title="Пальто")[:4]
        # context['shtany_products'] = Product.objects.filter(category__title="Штаны")[:4]
        # context['crossy_products'] = Product.objects.filter(category__title="Кроссы")[:4]
        context['nav_categories'] = Product.objects.filter(parent=None)[:4]




