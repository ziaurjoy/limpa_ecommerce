from django.urls import path
from .views import user_logout,user_login
urlpatterns = [
    path('logout', user_logout, name='user-logout'),
    path('login', user_login, name='user-login'),
]