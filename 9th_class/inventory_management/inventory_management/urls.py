
from django.contrib import admin
from django.urls import path
from inventory_management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('productList/', productList, name='productList'),
    path('addProduct/', addProduct, name='addProduct'),
    path('deleteProduct/<str:myid>', deleteProduct, name='deleteProduct'),
    path('editProduct/<str:myid>', editProduct, name='editProduct'),
    path('viewProduct/<str:myid>', viewProduct, name='viewProduct'),
]
