from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('new/', views.create_user_profile, name='create_user_profile')
]