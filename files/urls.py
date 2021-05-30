from django.urls import path
from files import views
from file_upload import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='index'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)