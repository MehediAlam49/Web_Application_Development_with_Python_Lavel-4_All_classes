
from django.contrib import admin
from django.urls import path
from productManagement.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('addProduct/', addProduct, name='addProduct'),
    path('addCustomer/', addCustomer, name='addCustomer'),
]
