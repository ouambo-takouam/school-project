from django.urls import path

from . import views

from .views import UserCreateView, UserUpdateView, UserDeleteView, UserListView

app_name = 'users'

urlpatterns = [
    path('new/', UserCreateView.as_view(), name='new'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
    path('list/', UserListView.as_view(), name='list'),
]