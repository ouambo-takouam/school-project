from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('new/', views.add_user, name='add'),
    path('list/', views.UserListView.as_view(), name='list'),
]