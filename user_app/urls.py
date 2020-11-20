from django.urls import path
# from .views import user_logout,user_login,user_registration, user_profile, update_profile,password_change
from . import views
urlpatterns = [
    path('logout', views.user_logout, name='user-logout'),
    path('login', views.user_login, name='user-login'),
    path('register', views.user_registration, name='user-register'),
    path('profile', views.user_profile, name='user-profile'),
    path('update/profile', views.update_profile, name='update-profile'),
    path('password/change', views.password_change, name='password-change'),
]