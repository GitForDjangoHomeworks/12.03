from django.urls import path
from .views import SingleProductPageTemplateView
app_name = 'products'

urlpatterns = [
    path('single_product', SingleProductPageTemplateView.as_view(), name='show_single_product_page')
    
]