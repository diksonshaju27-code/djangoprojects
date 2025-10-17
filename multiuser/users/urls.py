from django.urls import path
from . import views

app_name = "users"  # ✅ This registers the namespace

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('register/', views.Register.as_view(), name="register"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
#     path('adminhome',views.AdminHome.as_view(),name='adminhome'),
#     path('teachername',views.TeacherHome.as_view(),name="teacherhome"),
# path('studentname',views.StudentHome.as_view(),name="studenthome")
]
