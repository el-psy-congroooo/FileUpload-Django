from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "My Admin"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to My Admin Portal" 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("files.urls")),
]
