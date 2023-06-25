from re import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class MainPageTemplateView(TemplateView):
    template_name = 'mainpage/index.html'

