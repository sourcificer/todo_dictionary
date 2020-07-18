from django.urls import path
from .views import home, todo

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('todo', todo.as_view(), name='todo'),
    path('todo/edit/<str:id>/', todo.as_view(), name='editEntry'),
    path('todo/<str:delete>/', todo.as_view(), name='todo')
]
