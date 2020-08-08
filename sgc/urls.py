from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tasks.urls')),
    path('accounts/', include('accounts.urls')), # when there are two or more URLs with the same name, django obeys from top to bottom
    path('accounts/', include('django.contrib.auth.urls')),
]