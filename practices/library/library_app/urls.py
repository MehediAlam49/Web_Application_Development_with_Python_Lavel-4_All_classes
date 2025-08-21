from django.urls import path
from library_app.views import *

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('create_book/', create_book, name='create_book'),
    path('edit_book/<str:id>', edit_book, name='edit_book'),
    path('delete_book/<str:id>', delete_book, name='delete_book'),
]
