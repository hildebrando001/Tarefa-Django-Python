from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tasks.urls')),
 #   path('accounts/', include('accounts.urls')), # add url to accounts registration
    path('accounts/', include('django.contrib.auth.urls')),
]