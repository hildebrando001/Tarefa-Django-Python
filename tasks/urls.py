from django.urls import path

from . import views

urlpatterns = [
    path('', views.tasklist, name="task-list"),
    path('task/<int:id>',views.taskview,name="task-view")
]
