from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('register', views.Register.as_view(), name='register'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
]
