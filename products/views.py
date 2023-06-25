from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class SingleProductPageTemplateView(TemplateView):
    template_name = 'products/single_product.html'
