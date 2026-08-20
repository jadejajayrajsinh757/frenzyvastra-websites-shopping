from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Product


class AboutPageView(TemplateView):
    template_name = "about.html"


def mens_page(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'mens.html', {'products': products})


class WomensPageView(TemplateView):
    template_name = "womens.html"
