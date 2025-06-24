
from django.contrib import admin
from django.urls import path
from blog_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('all-Blogs/', allBlogs, name='allBlogs'),
    path('all-User/', allUser, name='allUser'),
    path('create-User/', createUser, name='createUser'),
    path('create-Blogs/', createBlogs, name='createBlogs'),
    path('deleteBlogs/<str:id>', deleteBlogs, name='deleteBlogs'),
]
