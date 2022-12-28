from django.urls import path
from product.views import *


urlpatterns = [
    path('products/', get_product),
    
]