
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth_app.urls')),
    path('employee/', include('employer_app.urls')),
    # path('', include('candidate_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
