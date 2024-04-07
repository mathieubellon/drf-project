from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   path('admin/', admin.site.urls),
    # this is module path copy this as it is
    path('auth/', include('allauth.urls')),
]