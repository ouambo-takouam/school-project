from django.urls import path

from . import views

from .views import UserCreateView, UserUpdateView, UserListView

app_name = 'users'

urlpatterns = [
    path('new/', UserCreateView.as_view(), name='new'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('list/', UserListView.as_view(), name='list'),
]