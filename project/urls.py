from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import  LogoutView
from django.urls import path, include

from users import views as users_views

urlpatterns = [
    path('create-school/', users_views.create_school, name='create_school'),
    path('profile/', users_views.profile, name='profile'),
    path('login/', users_views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('school.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
