# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from todo_api import urls as todo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include(todo_urls)),
]

from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
]