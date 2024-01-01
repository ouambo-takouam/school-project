from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('new/', views.create_user_profile, name='add'),
    path('list/', views.UsersListView.as_view(), name='list'),
]