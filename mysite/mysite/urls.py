from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pool/', include('pool.urls')),
    path('admin/', admin.site.urls),
]
