
from django.contrib import admin
from django.urls import path
from books.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='book_list'),
    path('book-form/', book_form, name='book_form'),
    path('delete_book/<str:id>', delete_book, name='delete_book'),
    path('edit_book/<str:id>', edit_book, name='edit_book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
