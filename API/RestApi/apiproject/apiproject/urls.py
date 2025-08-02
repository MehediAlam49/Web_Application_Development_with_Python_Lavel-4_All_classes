from django.contrib import admin
from django.urls import path
from apiApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentList/', studentList, name='studentList'),
    path('addStudent/', addStudent, name='addStudent'),
    path('teachers/', TeacherAPIView.as_view(), name='TeacherAPIView'),
    path('TeacherDetails/<str:id>/', TeacherDetails.as_view(), name='TeacherDetails'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
